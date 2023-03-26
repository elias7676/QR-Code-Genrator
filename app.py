import qrcode

def generate_qr_code(data):
    qr = qrcode.QRCode(
        version=1,
        box_size=10,
        border=4,
    )
    qr.add_data(data)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white")
    return img

# Generate QR code image to open app with package name cn.tydic.ethiopay
#img = generate_qr_code("androidapp://cn.tydic.ethiopay")
scheme = "linkedin"
url = "profile"
user_id = "elias-ibrahim-3305a1244"
uri = f"{app_scheme}://{package_name}/{user_id}"

scheme = "tg"
url = "resolve?domain="
user_id = "NFTsworld7"
uri = f"{scheme}://{url}{user_id}"

scheme = "fb"
url = "marketplace/item"
user_id = "557772906404314"
uri = f"{scheme}://{url}/{user_id}"

scheme = "snssdk1233"
url = "vm.tiktok.com/video"
user_id = "7195301523767774469"
uri = f"{scheme}://{url}/{user_id}"



#img = generate_qr_code(uri)
img = generate_qr_code(uri)
#img = generate_qr_code("intent://android.intent.action.MAIN/#Intent;scheme=http;package=cn.tydic.ethiopay;end")
img.save("qr_code.png")
