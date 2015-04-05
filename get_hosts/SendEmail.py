#coding=utf-8
__author__ = 'Hanz'
import smtplib
from email.mime.text import MIMEText

def send_mail(sender='wanghantest@163.com', password='zhongsou',
              receiver='wanghan@zhongsou.com', content='', smtpserver = 'smtp.163.com',
              subject='Error'):
	username = sender
	msg = MIMEText(content,'html','utf-8')
	# msg['subject'] = Header(subject, 'utf-8')
	msg['subject'] = subject
	smtp = smtplib.SMTP()
	smtp.connect(smtpserver)
	smtp.login(username,password)
	smtp.sendmail(sender, receiver, msg.as_string())
	smtp.quit()
