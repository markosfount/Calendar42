from django.shortcuts import render
from django.http import HttpResponse
from .Request import Request
from .RequestData import *
from django.views.decorators.cache import cache_page


@cache_page(60 * 4.2)
def basic(request,eventid):

    #check to see if the event id entered is the one that
    #corresponds to

    if eventid == default_event_id:

        # create instances of classes for making and handling requests
        # to api_proxy server

        request = Request(url, eventid, headers)
        requestdata = RequestData(request, eventid)
        title_code, title=requestdata.get_title()
        names_code, names=requestdata.get_subs()
        if title_code == 200 and names_code == 200:
            response = requestdata.make_jason(title, names)
        else:
            response = 'Could not find event information'
        return HttpResponse(response)
    else:
        return HttpResponse("Please provide a valid event id")


def noid(request):
    return HttpResponse("Please provide an event id")