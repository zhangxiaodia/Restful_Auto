from test_case.register_test import register

base_url='http://dev.muggle-inc.com/api/user/register'
def f2():
	passsword='1111'
#	register.f1()
	data=register().json_data(passsword)
	register.post_request(base_url,data)
	print("f2执行")

if __name__ == '__main__':
	f2()

