import requests


# check status
class Request:
    def __init__(self, url, event_id, headers):
        self.url = url
        self.event_id = event_id
        self.headers = headers

    def req_event_ID(self):
        url = self.url + "events/" + self.event_id
        r = requests.get(url, headers=self.headers)
        return r

    def req_event_subs(self):
        url = self.url + "event-subscriptions/?event_ids=" + \
              "["+self.event_id+"]"
        r = requests.get(url,headers=self.headers)
        return r


