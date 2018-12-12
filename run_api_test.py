from HTMLTestRunner import HTMLTestRunner
from email.mime.text import MIMEText
from email.header import Header
import smtplib
import unittest
import time
import os
def send_mail(file_new):
	f = open(file_new,'rb')
	mail_boby = f.read()
	f.close()

	sender = 'zhangmengdi929@163.com'
	password = 'zmdluckystar90'
	receiver = '1172533210@qq.com'

	msg = MIMEText(mail_boby,'html','utf-8')
	msg['Subject'] = Header('API自动化测试报告','utf-8')
	msg['From'] = sender
	msg['To'] = receiver

	smtp = smtplib.SMTP()
	smtp.connect('smtp.163.com')
	smtp.login(sender,password)
	smtp.sendmail(sender,receiver,msg.as_string())
	smtp.quit()
	print('email has send out!')
if __name__ == '__main__':
	filename='./result/result.html'
	fp = open(filename,'wb')
	runner = HTMLTestRunner(stream=fp,title='Fanscub项目API自动化测试报告',description='环境：windows10')
	discover = unittest.defaultTestLoader.discover('./test_case',pattern='*_test.py')
	runner.run(discover)
	fp.close()
	send_mail(filename)







'''
#查找测试报告目录，找到最新生成的测试报告
def new_report(testreport):
	lists = os.listdir(testreport)
	lists.sort(key=lambda fn: os.path.getmtime(testreport + "\\" + fn))
	file_new = os.path.join(testreport,lists[-1])
	print(file_new)
	return file_new
'''