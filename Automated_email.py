import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from_addr='brian.testemail007@gmail.com'
to_addr=['jgduyfh@gmail.com','hisbdcuegf.@gmail.com']

msg=MIMEMultipart()
msg['From']=from_addr
msg['To']=" ,".join(to_addr)
msg['subject']='Test Email'

body='Hello! This is an Automated Email'

msg.attach(MIMEText(body,'plain'))

email='brian.testemail007@gmail.com'
password='Applepie123'

mail=smtplib.SMTP('smtp.gmail.com',587)
mail.ehlo()
mail.starttls()
mail.login(email,password)

text=msg.as_string()
mail.sendmail(from_addr,to_addr,text)
mail.quit()
