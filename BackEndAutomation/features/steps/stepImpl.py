import requests
from behave import *

from payLoads import addBookPayLoad
from payLoads import *
from utilities.configurations import getConfig
from utilities.resources import ApiResources


@given('The Book details which needs to be added to Library')
def step_Impl(context):  # context variable activates features level in BDD. This context variable will send to all
    # methods
    config = getConfig()
    # context.url means we are assigning new(url property) property to context object
    context.url = config['API']['endpoint'] + ApiResources.addBook
    context.header = {'Content-Type': 'application/json'}
    context.payLoad = addBookPayLoad('pral10', '1999 '
                                               '')


@when('We execute the AddBook PostAPI method')
def step_impl(context):
    context.response = requests.post(context.url, json=context.payLoad, headers=context.header, )


@then('Book is successfully added')
def step_impl(context):
    print(context.response.json())
    response_json = context.response.json()
    context.book_ID = response_json['ID']
    print(context.book_ID)
    assert response_json['Msg'] == 'successfully added'


@given('The Book details with {isbn} and {aisle}')
def step_impl(context, isbn, aisle):
    config = getConfig()
    context.url = config['API']['endpoint'] + ApiResources.addBook
    context.header = {'Content-Type': 'application/json'}
    context.payLoad = addBookPayLoad(isbn, aisle)


@given(u'I have Github auth credentials')
def step_impl(context):
    # head = {'Authorization': 'Bearer bac99b33b9e1e8a4499f54daa4651d7b541ceef1'}
    context.session = requests.session()
    context.session.t = head = {'Authorization': 'Bearer bac99b33b9e1e8a4499f54daa4651d7b541ceef1'}
    requests.packages.urllib3.disable_warnings()


@when(u'I hit getRepo API of Github')
def step_impl(context):
    context.response = context.session.get(ApiResources.gitHubRepo, verify=False)


@then(u'Status code of response should be {statusCode:d}')
def step_impl(context, statusCode):
    print(context.response.status_code)
    assert context.response.status_code == statusCode
