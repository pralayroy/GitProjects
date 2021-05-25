import requests

from payLoads import *
from utilities.configurations import getConfig
from utilities.resources import ApiResources


def after_scenario(context, scenario):
    if "bookAPI" in scenario.tags:
        config = getConfig()
        url_del = config['API']['endpoint'] + ApiResources.deleteBook
        deleteBook_response = requests.post(url_del, json={'ID': context.book_ID}, headers=context.header, )
        assert deleteBook_response.status_code == 200
        res_json = deleteBook_response.json()
        print(res_json["msg"])
        assert res_json["msg"] == "book is successfully deleted"
