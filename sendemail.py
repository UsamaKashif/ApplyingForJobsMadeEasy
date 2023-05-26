from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import re


regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'  
def check_email_valid(email):   
    if(re.search(regex,email)):
        return True  
    else:
        return False

# if your cv name is not c.pdf then change the filename parameter
def send_email(sender_email, subject, receiver_email, body, filename="cv.pdf"):
    if not check_email_valid(receiver_email):
        print("Invalid sender email:", receiver_email)
        return
    try:
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
    except Exception as e:
        print("prolem creating the Message", e)
        exit()

    return text
