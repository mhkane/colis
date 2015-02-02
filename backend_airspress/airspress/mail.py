#!/usr/bin/python

import smtplib

email_to = 'team@airspress.com'
username = 'team@airspress.com'
password = '@1rm@r$i@'

smtpserver = smtplib.SMTP("mail.airspress.com",26)
smtpserver.ehlo()
smtpserver.login(username,password)
header = 'To:' + email_to + '\n' + 'From: ' + username + '\n' + 'Subject: Python SMTP Auth\n'
msg = header + '\n\n This is a test message generated from python script \n\n'
smtpserver.sendmail(username, email_to, msg)
smtpserver.close()
print 'Email sent successfully'
