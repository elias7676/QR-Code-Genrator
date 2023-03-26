import qrcode
from qrcode.constants import ERROR_CORRECT_H, ERROR_CORRECT_L
from PIL import Image

def event():
    summary = "AFRICOM Learning Forum"
    description = "Everyone is Invited"
    location = "Africom Technologies, ICT Park"
    start = "20230203T100000Z"
    end = "20230203T140000Z"
    
    ical = f"BEGIN:VEVENT\nSUMMARY:{summary}\nLOCATION:{location}\nDTSTART:{start}\nDTEND:{end}\nEND:VEVENT"

    qr = qrcode.QRCode(
        version=None,
        error_correction=ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(ical)
    qr.make(fit=True)

    img = qr.make_image(fill_color="#171f78", back_color="white")
    img.save('codes/event.png')

def sms(phone_number,message):
    sms_uri = f"sms:{phone_number}?body={message}"
    qr = qrcode.QRCode(
        version=None,
        error_correction=ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(sms_uri)
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")
    img.save('codes/sms.png')

def vcard(last_name,first_name,phone,email):
    vcard = f"BEGIN:VCARD\nVERSION:3.0\nN:{last_name};{first_name}\nTEL;TYPE=WORK:{phone}\nEMAIL;TYPE=WORK:{email}\nEND:VCARD"
    qr = qrcode.QRCode(
        version=None,
        error_correction=ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(vcard)
    qr.make(fit=True)

    img = qr.make_image()
    img.save('codes/vcard.png')

def location(longitude, latitude):
    geo = f"geo:{latitude},{longitude}?q={latitude},{longitude}({name})"
    #else:
    #    geo = f"geo:{latitude},{longitude}?q={latitude},{longitude}"
    qr = qrcode.QRCode(
        version=None,
        error_correction=ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(geo)
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")
    img.save('codes/location.png')



def insert_image_in_qr(qr_data, image_path):
    qr = qrcode.QRCode(
        version=None,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(qr_data)
    qr.make(fit=True)

    img = qr.make_image(fill_color="blue", back_color="black")

    # Open the image to be inserted
    icon = Image.open(image_path)

    # Resize the image to fit in the middle of the QR code
    icon_size = int((img.size[0] - 4 * qr.border) / 4)
    icon = icon.resize((icon_size, icon_size))

    # Calculate the position of the image in the QR code
    icon_pos = ((img.size[0] - icon_size) // 2, (img.size[1] - icon_size) // 2)

    # Paste the image onto the QR code
    img.paste(icon, icon_pos)

    return img
def with_icon():
    data = "https://www.example.com"
    img = insert_image_in_qr(data, "icon.png")
    img.save('codes/dec.png')
