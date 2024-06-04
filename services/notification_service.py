import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from config import EMAIL_CONFIG

class NotificationService:
    def __init__(self):
        self.smtp_server = EMAIL_CONFIG['smtp_server']
        self.smtp_port = EMAIL_CONFIG['smtp_port']
        self.sender_email = EMAIL_CONFIG['sender_email']
        self.receiver_email = EMAIL_CONFIG['receiver_email']
        self.password = EMAIL_CONFIG['password']

    def send_notification(self, message):
        msg = MIMEMultipart()
        msg['From'] = self.sender_email
        msg['To'] = self.receiver_email
        msg['Subject'] = 'New Findings Notification'

        msg.attach(MIMEText(message, 'plain'))

        server = smtplib.SMTP(self.smtp_server, self.smtp_port)
        server.starttls()
        server.login(self.sender_email, self.password)
        text = msg.as_string()
        server.sendmail(self.sender_email, self.receiver_email, text)
        server.quit()
