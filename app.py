from flask import Flask, render_template, jsonify
import requests
import json
from datetime import datetime

app = Flask(__name__)

def load_sites():
    with open("sites.json") as f:
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
            r = requests.get(url, timeout=5)
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
        except requests.RequestException:
            status = "❌ DOWN"
            if menu == "/login":
                login_down = True
            else:
                utama_down = True
            elapsed = 0

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
    sites = load_sites()
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

if __name__ == "__main__":
    app.run(debug=True)
