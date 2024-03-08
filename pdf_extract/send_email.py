import smtplib
from email import message

from_addr = 'khrade75@gmail.com'
to_addr = 'advinculacon@gmail.com'
subject = 'This is a testing'
body = 'Gwapo imo uyab'

msg = message.Message()
msg.add_header('from', from_addr)
msg.add_header('to', to_addr)
msg.add_header('subject', subject)
msg.set_payload(body)

server = smtplib.SMTP('smtp.gmail.com', 587)
server.connect("smtp.gmail.com", 587)
server.ehlo()
server.starttls()
server.ehlo()
server.login(from_addr, 'kronos12')
server.send_message(msg, from_addr=from_addr, to_addr=to_addr)