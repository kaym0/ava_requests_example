"""
Avabur HTTP(s) example.

We will use this to retrieve data from Avabur.

To upload this data into google sheets you can add to this script using the
Google Sheets python API
https://developers.google.com/sheets/api/quickstart/python
"""
#   We will use requests since it has a Session handler automatically taking care
#   Of any cookies
import requests
import json


class Avabur(object):
    """avabur"""
    def __init__(self, username, password, base_url="https://pendoria.net/"):
        """__init__

        :param username: kaymo
        :param password: xxxxxxxxx
        """
        #   Setup URLs
        self.base_url = base_url
        self.login_url = self.base_url + "login"
        self.copper = self.base_url + "market/api/display/copper"
        self.food = self.base_url + "market/api/display/food"

        #   Create Session to magically handle our cookies and stuff
        self.session = requests.Session()

        #   Authenticate!
        self.authenticate(username, password)

    def authenticate(self, username, password):
        #   Vsyn does his stuff here, uses a single dictionary entry and has the data under "info"
        #   Normally a payload would look like:
        #   {"USERNAME": "figgis", "PASSWORD": "THISISTOTALLYMYPASSWORD"}
        payload = {"username": "{}", "password": "{}", "login": "login".format(username, password)}
        response = self.session.post(self.login_url, data=payload)
        #   We can return the response in case we want to poke at this later.
        #   Probably would be best just returning nothing in practice though.
        print(response.content)
        # return response

    def get_copper(self):
        #  payload = {"clan": clan_id}
        return self.session.post(self.copper)

    def get_food(self):

        #  payload = {"clan": clan_id}
        return self.session.post(self.food)


def example_usage(username: str, password: str):
    """example_usage"""
    #   Create class which logs us in.
    ava = Avabur(username, password)

    #   lets get data and format it as json
    #   We need to use the ".content" to get data out of a requests(imported module) response
    copper = json.loads(ava.get_copper().content)
    food = json.loads(ava.get_food().content)

    #   lets write this data to a file
    with open("donations.json", "w+") as file:
        file.write(json.dumps(copper))
    with open("funds.json", "w+") as file:
        file.write(json.dumps(food))

    #   This is the point where we would do something with the Google Sheets API
    #   Uploading the content, etc. Their guide walks through it and super easy.


example_usage("kaymo", "xxxx")
