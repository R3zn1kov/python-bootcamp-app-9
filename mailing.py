import smtplib
import imghdr
from email.message import EmailMessage

# insert Gmail app password below
password = ""
sender = "ldlreznikov@gmail.com"
receiver = "ldlreznikov@gmail.com"


def send_email(image_path):

    email_message = EmailMessage()
    email_message["Subject"] = "New customer showed up!"
    email_message.set_content("Hey, we just saw a new customer!")

    with open(image_path, "rb") as file:
        content = file.read()
    email_message.add_attachment(content, maintype="image", subtype=imghdr.what(None, content))

    gmail = smtplib.SMTP("smtp.gmail.com", 587)
    gmail.ehlo()
    gmail.starttls()
    gmail.login(sender, password, )
    gmail.sendmail(sender, receiver, email_message.as_string())
    gmail.quit()


if __name__ == "__main__":
    send_email(image_path="images/19.png")
