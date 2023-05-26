import email, smtplib, ssl
from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import time

# EAMIL SETUP
sender_email = "<youremail@gmail.com>"
password = "<yourpassword>"


# if your cv name is not c.pdf then change the filename parameter
def send_email(subject, receiver_email, body, filename="cv.pdf"):
    try:
        time.sleep(20)
        # Create a multipart message and set headers
        message = MIMEMultipart()
        message["From"] = sender_email
        message["Subject"] = subject
        message["To"] = receiver_email
        # Add body to email
        message.attach(MIMEText(body, "plain"))
        filename = filename
        # Open PDF file in binary mode
        with open(filename, "rb") as attachment:
            # Add file as application/octet-stream
            # Email client can usually download this automatically as attachment
            part = MIMEBase("application", "octet-stream")
            part.set_payload(attachment.read())  # In same directory as script
        # Encode file in ASCII characters to send by email    
        encoders.encode_base64(part)
        # Add header as key/value pair to attachment part
        part.add_header(
            "Content-Disposition",
            f"attachment; filename= {filename}",
        )
        # Add attachment to message and convert message to string
        message.attach(part)
        text = message.as_string()
        # Log in to server using secure context and send email
        context = ssl.create_default_context()
        with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
            server.login(sender_email, password)
            server.sendmail(sender_email, receiver_email, text)
        print("Email sent to:", receiver_email)
    except Exception as e:
        print("Problem sending email to:", receiver_email)
