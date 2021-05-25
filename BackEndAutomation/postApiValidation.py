import requests
import configparser
from payLoads import *
from utilities.configurations import *
from utilities.resources import *
import urllib3
from requests.auth import HTTPBasicAuth

# Add book
config = getConfig()
url = config['API']['endpoint'] + ApiResources.addBook
header = {'Content-Type': 'application/json'}
addBook_response = requests.post(url, json=addBookPayLoad('pral7'), headers=header, )

print(addBook_response.json())
response_json = addBook_response.json()
print(type(response_json))
# print(response_json['ID'])
book_ID = response_json['ID']
# Delete Book
url_del = config['API']['endpoint'] + ApiResources.deleteBook
deleteBook_response = requests.post(url_del, json={'ID': book_ID}, headers=header, )

assert deleteBook_response.status_code == 200
res_json = deleteBook_response.json()
print(res_json["msg"])
assert res_json["msg"] == "book is successfully deleted"

# Authentication
url = "https://api.github.com/user"
#head = {'Authorization': 'Bearer bac99b33b9e1e8a4499f54daa4651d7b541ceef1'}
session = requests.session()
session.t = head = {'Authorization': 'Bearer bac99b33b9e1e8a4499f54daa4651d7b541ceef1'}
requests.packages.urllib3.disable_warnings()
gitHub_response = requests.get(url, verify=False, headers=head)
gitHub_response = session.get(url, verify=False)
print(gitHub_response.status_code)
