import json

import requests

#response = requests.get('http://216.10.245.166/Library/GetBook.php', params={'AuthorName': 'pralay roy'},)
response = requests.get('http://216.10.245.166/Library/GetBook.php', params={'AuthorName': 'Rahul Shetty'},)
#print(response.text)
#print(type(response.text))
#dict_response = json.loads(response.text)
#print(type(dict_response))
#print(dict_response[0]['isbn'])

json_response = response.json()
print(type(json_response))
print(json_response[0]['isbn'])
assert response.status_code == 200
print(response.headers)
assert response.headers['Content-Type'] == 'application/json;charset=UTF-8'

for actual_book in json_response:
    if actual_book['isbn'] == 'aw2c':
        break

expected_book = {
        "book_name": "REST Assured Learning 1",
        "isbn": "aw2c",
        "aisle": "123"
    }
assert actual_book == expected_book


