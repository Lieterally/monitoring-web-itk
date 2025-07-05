from flask import Flask, render_template, jsonify
import requests
import os
import json
# from flask_sqlalchemy import SQLAlchemy
# from sqlalchemy.exc import OperationalError
from datetime import datetime
import urllib3
from flask import make_response
from concurrent.futures import ThreadPoolExecutor
from models import db, Website, Page

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root@localhost/monitoring_web_itk'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


db.init_app(app)

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


# When using sites.json ------------------

BASE_DIR = os.path.dirname(os.path.abspath(__file__))


def load_sites():
    with open(os.path.join(BASE_DIR, "sites.json")) as f:
        return json.load(f)



# When using db --------------------

# def load_sites():
#     with app.app_context():
#         websites = Website.query.all()
#         sites = []
#         for site in websites:
#             sites.append({
#                 "nama_web": site.nama_web,
#                 "link_web": site.link_web,
#                 "halaman_web": [page.halaman_web for page in site.pages]
#             })
#         return sites

def check_site(link_web, halaman_web):
    statuses = []
    total_time = 0
    count = 0
    login_down = False
    utama_down = False
  
    
    headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
    }

    for halaman in halaman_web:
        url = link_web + halaman
        try:
            
          
            r = requests.get(url, headers=headers, timeout=5, verify=False)
            
            elapsed = r.elapsed.total_seconds()
            print(f"⏱️ Checked {url} in {elapsed} seconds")
            total_time += elapsed
            count += 1
            if r.status_code == 200:
                status = "✅ UP"
            else:
                status = f"⚠️ {r.status_code}"
                if halaman == "/login":
                    login_down = True
                else:
                    utama_down = True
        except requests.RequestException:
            status = "❌ DOWN"
            if halaman == "/login":
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


@app.route("/full")
def indexFull():
    return render_template("indexFull.html")

@app.route("/status")
def status():
    try:
        sites = load_sites()
        print("✅ sites loaded")
    except Exception as e:
        print("❌ error in /status:", e)
        return jsonify({"error": str(e)}), 500

    def monitor(site):
        statuses, overall_status, avg_response_time = check_site(site["link_web"], site["halaman_web"])
        return {
            "nama_web": site["nama_web"],
            "link_web": site["link_web"],
            "overall_status": overall_status,
            "avg_response_time": avg_response_time,
            "statuses": statuses
        }

    with ThreadPoolExecutor(max_workers=10) as executor:
        monitored = list(executor.map(monitor, sites))

    response = make_response(jsonify({
        "last_check": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "monitored": monitored
    }))
    response.headers["Cache-Control"] = "no-store, no-cache, must-revalidate, max-age=0"
    return response

# if __name__ == "__main__":
#     app.run(debug=True)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))

