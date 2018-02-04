import json

class Settings(object):
    """usage: field 1; url"""
    url = ""
    def __init__(self):
        settingData = json.load(open('settings.json'))
        self.url = settingData["baseAddress"]
        print("active url is: " + self.url)
    
    def getURL(self):
        return self.url