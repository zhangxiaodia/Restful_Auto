import unittest
import requests
import json

base_url='http://dev.muggle-inc.com/api/user/register'

class register(unittest.TestCase):
#	def f1():
#		print("f1被执行")
	@staticmethod
	def post_request(url,data):
		response=requests.post(url,data=data)
		print(response.text)
		response_json=response.text
		j=json.loads(response_json)
		return j
	def json_data(self,pwd):
		data={
		'phone':'13000000191',
		'code':'8888',
		'password':pwd
		}
		return data
	def test_register1(self):
		self.pwd='123456'
		data=self.json_data(self.pwd)
		j=self.post_request(base_url,data)
		self.assertEqual(j['errcode'],400,msg='test')
		self.assertIn(j['errmsg'],"密码需要6-16位数字与字母组合####",msg='test')
	def test_register2(self):
		self.pwd='1234567890123456'
		data=self.json_data(self.pwd)
		j=self.post_request(base_url,data)
		self.assertEqual(j['errcode'],400,msg='test')
	def test_register3(self):
		self.pwd='qq123456'
		data=self.json_data(self.pwd)
		j=self.post_request(base_url,data)
		self.assertEqual(j['errcode'],400,msg='test')

