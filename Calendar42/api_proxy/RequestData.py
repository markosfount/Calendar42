import json


url = "https://demo.calendar42.com/api/v2/"
default_event_id = "296fb2daa6b4a4429032ae41e3ba07d2_14770339037084"
headers = {'Accept': 'application/json', 'Content-type': 'application/json',
           'Authorization': 'Token 1e855f0e9c80439e98dd518f15cca5df59bc9737'}


class RequestData():
    def __init__(self,request,event_id):
        self.request = request
        self.event_id = event_id

    # get data that contains event title

    def get_title(self):
        event = self.request.req_event_ID()
        event_title = ''
        if event.status_code == 200:
            data = event.json()['data']
            event_title = data[0]['title']
        return event.status_code, event_title

    # get data that contains event subscriptions

    def get_subs(self):
        event_subs = self.request.req_event_subs()
        mylist = []
        if event_subs.status_code == 200:
            data=event_subs.json()['data']

            # iterate over subscriptions to get first names
            # and insert to mylist

            for diction in data:
                mylist.append((diction['subscriber']['first_name']))
        return event_subs.status_code, mylist

    # encode values into a json

    def make_jason(self, title, list_of_names):
        return json.dumps({"id": self.event_id, "title": title, "names": list_of_names})




