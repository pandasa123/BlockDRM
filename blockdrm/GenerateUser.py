import json
import requests
from .StringDict import MyDict
"""Uses the REST api to add a user to hyperledger"""

class GenerateUser(object):
    url = ""
    def __init__(self, settings):
        self.url = settings.getURL()
    
    def addUser(self, userID, firstName, lastName):
        print("\n\nadding user----------")
        url = self.url + ".User"
        jsonPreFormat ={
             "$class" : "org.acme.trading.User",
             "userId" : userID,
             "firstName" : firstName,
             "lastName" : lastName
        }
        json = MyDict(jsonPreFormat)
        requests.post(url, json)
        print("request sent to:\n" + url)
        print("json data:")
        print(json)