
import os
import webapp2
import json
import httplib2
import requests
import pprint
from weather import get_all_weather as get_all_weather

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
        hourly_url = "http://api.wunderground.com/api/%s/hourly10day/q/autoip.json?geo_ip=%s" % (KEY, TEST_IP)
        h = httplib2.Http()
        hourly_result = json.loads(h.request(hourly_url,'GET')[1])

        if hourly_result.get('error') is not None:
            response = make_response(json.dumps(hourly_result.get('error')), 500)
            response.heads['Content-Type'] = 'application/json'
            return response

        forecast_url = "http://api.wunderground.com/api/%s/forecast10day/q/autoip.json?geo_ip=%s" % (KEY, TEST_IP)
        j = httplib2.Http()
        forecast_result = json.loads(j.request(forecast_url,'GET')[1])

        if forecast_result.get('error') is not None:
            response = make_response(json.dumps(forecast_result.get('error')), 500)
            response.heads['Content-Type'] = 'application/json'
            return response


        get_all_weather(hourly_result, forecast_result)





        today = []
        rest = []




        return self.render("front.html", today=today, rest=rest)




app = webapp2.WSGIApplication([ ("/", MainPage),
                                ],
                                debug=True)
