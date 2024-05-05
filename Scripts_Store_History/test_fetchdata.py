# # test_fetchdata.py
# import subprocess

# def test_fetchdata_with_urls():
#     urls = [
#         "https://policies.google.com/privacy?hl=en-US",
#         "https://privacy.umbc.edu/web-site-privacy-statement/",
#         "https://github.com/about/developer-policy"
#     ]

#     # Run fetchdata.py with the URLs
#     process = subprocess.run(['python', 'fetchdata.py'] + urls, capture_output=True, text=True)

#     # Check the output or return code
#     if process.returncode == 0:
#         print("fetchdata.py ran successfully.")
#         print(process.stdout)
#     else:
#         print("fetchdata.py encountered an error.")
#         print(process.stderr)

# if __name__ == "__main__":
#     test_fetchdata_with_urls()


import smtplib
from email.mime.text import MIMEText

subject = "Email Subject"
body = "This is the body of the text message"
sender = "saikrupar82@gmail.com"
recipients = "saikrus1@umbc.edu"
password = "vbdd sxlv kdug pwes"


def send_email(subject, body, sender, recipients, password):
    msg = MIMEText(body)
    msg['Subject'] = subject
    msg['From'] = sender
    msg['To'] = ', '.join(recipients)
    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp_server:
       smtp_server.login(sender, password)
       smtp_server.sendmail(sender, recipients, msg.as_string())
    print("Message sent!")


send_email(subject, body, sender, recipients, password)