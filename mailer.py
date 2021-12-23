import smtplib
import ssl

from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

subject = "CONGRATULATIONS!!! You have been selected for the COGAAN 2022!!"
body = "This is a test email sent from the certigen pre_alpha_nightly_build(1.0.2) please ignore !!!"
sender_email = "sender_email"
participant_email = "participant_email"
password = "supersecretpassword"


def certimailer(subject, body, sender_email, participant_email, password):
    message = MIMEMultipart()
    message["From"] = sender_email
    message["To"] = participant_email
    message["Subject"] = subject
    message["Bcc"] = participant_email

    message.attach(MIMEText(body, "plain"))

    filename = "certi.pdf"

    with open(filename, "rb") as attachment:
        part = MIMEBase("application", "octet-stream")
        part.set_payload(attachment.read())
    encoders.encode_base64(part)
    part.add_header(
        "Content-Disposition",
        f"attachment; filename= {filename}",
    )

    message.attach(part)
    text = message.as_string()

    context = ssl.create_default_context()
    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
        server.login(sender_email, password)
        server.sendmail(sender_email, participant_email, text)
        print("Mail sent successfully to", participant_email)


certimailer(subject, body, sender_email, participant_email, password)
