import json

"""Uses the REST api to add a user to hyperledger"""

class GenerateUser(object):
    url = ""
    def __init__(self, settings):
        self.url = settings.getURL()
    
    def addUser(self, userID, firstName, lastName):
        