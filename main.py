
import os
import webapp2
import json
import httplib2
import requests
import pprint
from Weather import get_weather

from Handler import Handler


class MainPage(Handler):
    """
    This class is a child of Handler and is for FrontPage.
    """
    def get(self):
        ip = self.request.remote_addr
        KEY = json.loads(open('client_secrets.json', 'r').read())['UNDERGROUND']
        TEST_IP = json.loads(open('client_secrets.json', 'r').read())['TEST_IP']
        # NEED TO CHANGE IP
#
#
#
#
#
        url = "http://api.wunderground.com/api/%s/forecast10day/q/autoip.json?geo_ip=%s" % (KEY, ip)
#
#
#
#
#
#
        h = httplib2.Http()
        result = json.loads(h.request(url,'GET')[1])

        if result.get('error') is not None:
            response = make_response(json.dumps(result.get('error')), 500)
            response.heads['Content-Type'] = 'application/json'
            return response

        weather_days = get_weather(result)
        today = weather_days[0]
        rest = weather_days[1:]



        return self.render("main_page.html", today=today, rest=rest)




app = webapp2.WSGIApplication([ ("/", MainPage),
                                ],
                                debug=True)
