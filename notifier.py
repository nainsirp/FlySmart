import smtplib
from email.mime.text import MIMEText
from config import EMAIL, EMAIL_PASSWORD, SMTP_SERVER, SMTP_PORT

def send_email_alert(to_mail,price, source, destination):
    subject = "✈️ Flight Price Alert"
    body = f"""
Good News!

Flight from {source} to {destination}
Current Price: ₹{price}

Book now before price increases!
"""

    msg = MIMEText(body)
    msg["Subject"] = subject
    msg["From"] = EMAIL
    msg["To"] = to_mail

    with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
        server.starttls()
        server.login(EMAIL, EMAIL_PASSWORD)
        server.send_message(msg)
