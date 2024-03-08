from __future__ import print_function

import base64
import os.path
import smtplib

# from email import message
from email.mime.text import MIMEText
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow

#modifying these scope, delete the file token.json
SCOPES = ['https://mail.google.com/']

#user token storage
USER_TOKENS = 'token.json'

#application credentials
CREDENTIALS = '' #file location

def getToken() -> str:
    creds = None

    #File token.json stores the user's access and refresh tokens, and is created automatically when the authorization flow completes for the first time

    if os.path.exists(USER_TOKENS):
        creds = Credentials.from_authorized_user_file(USER_TOKENS, SCOPES)
        creds.refresh(Request())
        # If there are no (valid) credentials available, let the user log in.
        if not creds or not creds.valid:
            if creds and creds.expired and creds.refresh_token:
                creds.refresh(Request())
            else:
                flow = InstalledAppFlow.from_client_secrets_file(CREDENTIALS, SCOPES)
                creds = flow.run_local_server(port=0)
                # Save the credentials for the next run
                with open(USER_TOKENS, 'w') as token:
                    token.write(creds.to_json())

    return creds.token


def generate_oauth2_string(username, access_token) -> str:
    auth_string = 'user=' + username + '\1auth=Bearer ' + access_token + '\1\1'
    return base64.b64encode(auth_string.encode('ascii')).decode('ascii')

def send_email (host, port, subject, msg, sender, recipients):
    access_token = getToken()
    auth_string = generate_oauth2_string(sender, access_token)

    msg = MIMEText(msg)
    msg['Subject'] = subject
    msg['From'] = sender
    msg['To'] = ', '.join(recipients)

    server = smtplib.SMTP(host, port)
    server.starttls()
    server.docmd('AUTH', 'XOAUTH2' + auth_string)
    server.sendmail(sender, recipients, msg.as_string())
    server.quit()

def main():
    host = 'smtp.gmail.com'
    port = 587

    user = "khrade75@gmail.com"
    recipient = "advinculacon@gmail.com"
    subject = "Gwapo imo uyab"
    msg = "Hello World"
    sender = user
    recipients = [recipient]
    send_email(host, port, subject, msg, sender, recipients)
    
if __name__ == '__main__':
    main()
# LESS SECURED EMAILS
    
# from_addr = 'khrade75@gmail.com'
# to_addr = 'advinculacon@gmail.com'
# subject = 'This is a testing'
# body = 'Gwapo imo uyab'

# msg = message.Message()
# msg.add_header('from', from_addr)
# msg.add_header('to', to_addr)
# msg.add_header('subject', subject)
# msg.set_payload(body)

# server = smtplib.SMTP('smtp.gmail.com', 587)
# server.connect("smtp.gmail.com", 587)
# server.ehlo()
# server.starttls()
# server.ehlo()
# server.login(from_addr, 'kronos12')
# server.send_message(msg, from_addr=from_addr, to_addr=to_addr)