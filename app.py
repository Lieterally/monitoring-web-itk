from flask import Flask, render_template, jsonify
import requests
import os
import json
from datetime import datetime

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

app = Flask(__name__)

def load_sites():
    with open(os.path.join(BASE_DIR, "sites.json")) as f:
        return json.load(f)

def check_site(base_url, menus):
    statuses = []
    total_time = 0
    count = 0
    login_down = False
    utama_down = False

    for menu in menus:
        url = base_url + menu
        try:
            r = requests.get(url, timeout=5, verify=False)  # 🛡️ Disable SSL verification
            elapsed = r.elapsed.total_seconds()
            total_time += elapsed
            count += 1
            if r.status_code == 200:
                status = "✅ UP"
            else:
                status = f"⚠️ {r.status_code}"
                if menu == "/login":
                    login_down = True
                else:
                    utama_down = True
        except requests.RequestException as e:
            print(f"❌ Request failed for {url}: {e}")
            status = "❌ DOWN"
            elapsed = 0
            if menu == "/login":
                login_down = True
            else:
                utama_down = True

        statuses.append({
            "url": url,
            "status": status,
            "response_time": round(elapsed, 3)
        })

    if not login_down and not utama_down:
        overall_status = "✅ UP"
    else:
        details = []
        if utama_down:
            details.append("Utama")
        if login_down:
            details.append("Login")
        overall_status = f"❌ {' & '.join(details)}"

    avg_response_time = round(total_time / count, 3) if count > 0 else "N/A"

    return statuses, overall_status, avg_response_time

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/status")
def status():
    try:
        sites = load_sites()
        print("✅ sites loaded")
        monitored = []
        for site in sites:
            statuses, overall_status, avg_response_time = check_site(site["base_url"], site["menus"])
            monitored.append({
                "name": site["name"],
                "base_url": site["base_url"],
                "overall_status": overall_status,
                "avg_response_time": avg_response_time,
                "statuses": statuses
            })
        return jsonify({
            "last_check": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "monitored": monitored
        })
    except Exception as e:
        print("❌ Error in /status:", e)
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)
