
import os
import webapp2
import json
import httplib2
import requests
import pprint
from Weather import get_weather

import urllib, json

from Handler import Handler
import pprint


class MainPage(Handler):
    """
    This class is a child of Handler and is for FrontPage.
    """
    def get(self):

        # KEY = json.loads(open('client_secrets.json', 'r').read())['UNDERGROUND']
        # NEED TO CHANGE IP
        # url = "http://api.wunderground.com/api/%s/forecast10day/q/autoip.json?geo_ip=%s" % (KEY, ip)

        ip = self.request.remote_addr
        TEST_IP = json.loads(open('client_secrets.json', 'r').read())['TEST_IP']

        location_get_url = "http://ip-api.com/json/" + TEST_IP
        response = urllib.urlopen(location_get_url)
        data = json.loads(response.read())
        longitude, latitude, city = data['lon'], data['lat'], data['city']

        KEY = json.loads(open('client_secrets.json', 'r').read())['OPENWEATHER']
        url = "http://api.openweathermap.org/data/2.5/forecast?lat=%s&lon=%s&APPID=%s" % (latitude, longitude, KEY)

        response = urllib.urlopen(url)
        data = json.loads(response.read())

        thing = get_weather(data)
        pprint.pprint(thing)
        # thing = pprint.pprint(data)


        # h = httplib2.Http()
        # result = json.loads(h.request(url,'GET'))

        # print result
        #
        # if result.get('error') is not None:
        #     response = make_response(json.dumps(result.get('error')), 500)
        #     response.heads['Content-Type'] = 'application/json'
        #     return response
        #
        # weather_days = get_weather(result)
        # today = weather_days[0]
        # rest = weather_days[1:]
        #
        #
        today = {}
        rest = {}

        return self.render("main_page_revamp.html", today=today, rest=rest)
        # return self.write(thing)




app = webapp2.WSGIApplication([ ("/", MainPage),
                                ],
                                debug=True)
