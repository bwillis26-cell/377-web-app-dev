import qrcode

qr = qrcode.QRCode(
    version=1,
    box_size=5,
    border=10,
)

data = f"tel:{}" #'https://www.duckduckgo.com'

qr.add_data(data)
qr.make(fit=True)

img = qr.make_image()
# img.save('qr-duckduckgo.png')
img.save('qr-phonecall.png')

def generate_calendar_qr(summary, start_time, end_time, location, description, filename):
    # 1. Format the event data into VCALENDAR (.ics) format
    # Times must be in UTC format: YYYYMMDDTHHMMSSZ
    ical = f"""BEGIN:VCALENDAR
VERSION:2.0
BEGIN:VEVENT
SUMMARY:{summary}
DTSTART:{start_time}
DTEND:{end_time}
LOCATION:{location}
DESCRIPTION:{description}
END:VEVENT
END:VCALENDAR"""

    # 2. Configure QR Code settings
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )

    # 3. Add data and make the code
    qr.add_data(ical)
    qr.make(fit=True)

    # 4. Create image and save
    img = qr.make_image(fill_color="black", back_color="white")
    img.save(filename)
    print(f"QR Code saved as {filename}")

# --- Example Usage ---
# Start and End Time format: YYYYMMDDTHHMMSSZ (UTC)
generate_calendar_qr(
    summary="Barstow Village",
    start_time="20260318T100000Z", # Feb 15, 2026, 10:00 AM UTC
    end_time="20260318T110000Z",   # Feb 15, 2026, 11:00 AM UTC
    location="Conference Room A",
    description="Monthly project sync.",
    filename="event_qr.png"
)