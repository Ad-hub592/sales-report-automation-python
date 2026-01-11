from datetime import datetime
import smtplib
from email.message import EmailMessage
import config as cfg

emailfrom = cfg.EMAIL_FROM
emailpass = cfg.EMAIL_PASS
emailto = cfg.EMAIL_TO

def send_email(cfg_analysis_file):
    with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
        smtp.starttls()
        smtp.login(emailfrom, emailpass)

        msg = EmailMessage()
        msg['Subject'] = f"Business Analysis Report - {datetime.now().date()}"
        msg['From'] = emailfrom
        msg['To'] = emailto
        body = '''Please find the attached Business Analysis Report.\n
-"This is a system generated email. Please do not reply.'''
        msg.set_content(body)
        with open(cfg_analysis_file, "r") as f:
            data = f.read()
            msg.add_attachment(data, filename="Analysis.txt")

        smtp.send_message(msg)