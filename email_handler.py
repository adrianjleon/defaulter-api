import email, smtplib, ssl
from re import S
from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import os




def send_email(subject = "Monthly report", 
               body :str = "For more information, contact the API administrator", 
               to_email = "4devstestemail@gmail.com" , 
               from_email = "4devstestemail@gmail.com", 
               filename = "example.txt"):
    
    """
    Send email with attachment
    """
    
    html = f"""\
    <html>
    <body>
        <p><h2>Hi</h2>,<br>
        {body}  <br>
        <a href="https://www.youtube.com.com">youtube</a> 
        
        </p>
    </body>
    </html>
    """
    password = "mfthlcvzzqjjzcgw" # input("Type your password and press enter:")

    # Create a multipart message and set headers
    message = MIMEMultipart()
    message["From"] = from_email
    message["To"] = to_email
    message["Subject"] = subject
    message["Bcc"] = to_email  # Recommended for mass emails

    # Add body to email
    message.attach(MIMEText(html, "html"))

    
    basepath = os.path.dirname(os.path.abspath(__file__))
    filepath = os.path.join(basepath, f"output/{filename}")
    #/home/limitado/Documents/adrian-python/proyectos/morosidad/output/example.txt

    # Open txt file in binary mode
    with open(filepath, "rb") as attachment:
        # Add file as application/octet-stream
        # Email client can usually download this automatically as attachment
        part = MIMEBase("application", "octet-stream")
        part.set_payload(attachment.read())

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
        server.login(from_email, password)
        server.sendmail(from_email, to_email, text)


send_email()