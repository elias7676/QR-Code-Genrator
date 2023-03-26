from flask import Flask, request
import json
import qrcode
from qrcode.constants import ERROR_CORRECT_H, ERROR_CORRECT_L
from PIL import Image
import time
import datetime
from datetime import datetime
from flask_cors import CORS
app = Flask(__name__)
CORS(app)

@app.route('/sms', methods=['POST'])
def sms():
    data = request.get_json()
    if "latitude" in data and data["latitude"] != '0':
        latitude = data.get("latitude")
        longitude = data.get("longitude")
        uri = f"geo:{latitude},{longitude}?q={latitude},{longitude}"
    if "firstName" in data and data["firstName"] != '0':
        firstname = data.get("firstName")
        lastname = data.get("lastName")
        phone = data.get("phone")
        email = data.get("email")
        uri = f"BEGIN:VCARD\nVERSION:3.0\nN:{lastname};{firstname}\nTEL;TYPE=WORK:{phone}\nEMAIL;TYPE=WORK:{email}\nEND:VCARD"
    if "summary" in data and data["summary"] != '0':
        date_format = "%Y-%m-%dT%H:%M"
        new_date_format = "%Y%m%dT%H%M%SZ"
        summary = data.get("summary")
        location = data.get("location")
        description = data.get("description")
        start = data.get("start")
        dt_start = datetime.strptime(start, date_format)
        new_dt_start = dt_start.strftime(new_date_format)
        #dt_start = datetime.strptime(start, "%Y-%m-%dT%H:%M")
# Convert the datetime object to an ISO 8601 string
        iso_8601 = dt_start.isoformat()
        end = data.get("end")
        dt_end = datetime.strptime(end, date_format)
        new_dt_end = dt_end.strftime(new_date_format)
        #dt_end = datetime.strptime(end, "%Y-%m-%dT%H:%M")
# Convert the datetime object to an ISO 8601 string
        iso_8601 = dt_end.isoformat()
        uri = f"BEGIN:VEVENT\nSUMMARY:{summary}\nLOCATION:{location}\nDTSTART:{new_dt_start}\nDTEND:{new_dt_end}\nEND:VEVENT"

    if "phone_number" in data and data["phone_number"] != '0':
        phone_number = data.get("phone_number")
        message = data.get("message")
        uri = f"sms:{phone_number}?body={message}"
    if "ssid" in data and data["ssid"] != '0':
        ssid = data.get("ssid")
        password = data.get("password")
        uri= f"WIFI:T:WPA;S:{ssid};P:{password};;"
    if "url" in data and data["url"] != '0':
        url = data.get("url")
        uri = url
    if "linkedin" in data and data["linkedin"] != '0':
        scheme = "linkedin"
        url = "profile"
        user_id = data.get("linkedin")
        uri = f"{scheme}://{url}/{user_id}"
    if "marketplace" in data and data["marketplace"] != '0':
        scheme = "fb"
        url = "marketplace/item"
        user_id = data.get("marketplace")
        uri = f"{scheme}://{url}/{user_id}"
    if "telegram" in data and data["telegram"] != '0':
        scheme = "tg"
        url = "resolve?domain="
        user_id = data.get("telegram")
        uri = f"{scheme}://{url}{user_id}"

    if "tiktok" in data and data["tiktok"] != '0':
        scheme = "snssdk1233"
        url = "vm.tiktok.com/video"
        user_id = data.get("tiktok")
        uri = f"{scheme}://{url}/{user_id}"

    qr = qrcode.QRCode(
        version=None,
        error_correction=ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(uri)
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")
    img.save('codes/sms.png')
    time.sleep(1)
    return(uri)

if __name__ == '__main__':
    app.run(debug=True)
