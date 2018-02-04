import json
class MyDict(dict):
    """writes json files in double quotes"""
    def __str__(self):
        return json.dumps(self)