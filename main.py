
import os
import webapp2
import json
import httplib2
import requests
import pprint
from Weather import WeatherDay as WeatherDay, get_forecast as get_forecast, get_hourly as get_hourly

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

        hourly_forecast = hourly_result['hourly_forecast']

        test = get_hourly(hourly_forecast)
        for i in test:
            print i


        forecast_10day = get_forecast(forecast_result)



        today_forecast = forecast_10day[0]
        rest_forecast = forecast_10day[1:]
        today = []
        rest = []




        return self.render("front.html", today=today, rest=rest)




app = webapp2.WSGIApplication([ ("/", MainPage),
                                ],
                                debug=True)
