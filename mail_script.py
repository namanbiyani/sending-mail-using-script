import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

s = smtplib.SMTP('smtp.cc.iitk.ac.in',25)
s.starttls()
s.login("namanb","password")

sender="namanb@iitk.ac.in"
receiver="namanb@iitk.ac.in"
msg=MIMEMultipart()
msg['From'] = sender
msg['To'] = receiver
msg['Subject'] = "Python test email"
msg_body="email sent using python script"
msg.attach(MIMEText(msg_body,'plain'))

message=msg.as_string()
s.sendmail(sender,receiver,message)
s.quit()
