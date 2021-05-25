import requests

cookie = {'visit-month': 'February'}
response = requests.get('http://rahulshettyacademy.com', allow_redirects=False, cookies=cookie, timeout=1)
# 301 -> 200
#print(response.history)  # This will return redirection code. Like if there is any redirection or not
print(response.status_code)


session = requests.session()
session.cookies.update({'visit-month': 'February'})
res = session.get('https://httpbin.org/cookies', cookies={'visit-year':'2022'})
print(res.text)

#Attachment
# D:\Learnings\Python\PyCharm\PycharmProjects\BackEndAutomation\Sample.jpg
url = 'https://petstore.swagger.io/v2/pet/9843217/uploadImage'
file = {'file': open('D:\\Learnings\\Python\\PyCharm\\PycharmProjects\\BackEndAutomation\\Sample.jpg', 'rb')}
res = requests.post(url, files=file)
print(res.status_code)
print(res.text)

