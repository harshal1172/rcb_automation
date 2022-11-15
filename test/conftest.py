import json
import pytest
import requests

driver = None


@pytest.fixture(scope="class")
def setup(request):
    global log, jsondata
    with open('jsonfile/TeamRCB.json') as team:
        dict_data = requests.session()
        dict_data.jsondata = json.load(team)
        request.cls.jsondata = dict_data.jsondata
    yield
    dict_data.close()




