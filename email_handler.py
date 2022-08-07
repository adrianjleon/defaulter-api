import email, smtplib, ssl
from re import S
from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import os

# this module is used to store variables securely
from dotenv import load_dotenv
load_dotenv()




def send_email(subject = "email for test", 
               body :str = "For more information, contact the API administrator", 
               to_email = "4devstestemail5676577ghyjugtyu@gmail.com" , 
               from_email = "4devstestemail@gmail.com", 
               filename = None) -> None:
    
    """
    Send email with an attachment passing the filename as a parameter
    if no parameter is sent, the email will be sent as a test email
    """
    
    html = f"""\
    <html>
    <body>
        <p>Hi,<br>
        {body}  <br>
        <a href="https://www.youtube.com.com">youtube</a> 
        
        </p>
    </body>
    </html>
    """
    password =  os.environ.get('email_password') # input("Type your password and press enter:")

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
    
    if filename:
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
        try:
            server.login(from_email, password)
        except smtplib.SMTPAuthenticationError as e:
            #print(e)
            print("Connection failed or Wrong User/Password")
            return

        try:
            
            server.sendmail(from_email, to_email, text)
        except smtplib.SMTPRecipientsRefused as e:
            print(f"Wrong recipient: {e} \nNot an email address?")
        except Exception as e:
            print(e)
        


