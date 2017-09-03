
import os
import webapp2
import json
import httplib2
import requests
import pprint
from weather import get_all_weather as get_all_weather

from Handler import Handler

def casing(name):
    words = name.split(" ")
    return " ".join(list(map(lambda x: x[0].capitalize()+x[1:],words)))


class MainPage(Handler):
    """
    This class is a child of Handler and is for FrontPage.
    """
    def get(self):

        KEY = json.loads(open('client_secrets.json', 'r').read())['UNDERGROUND']

        # USING IP ADDRESS, NOT RELIABLE
        # TEST_IP = json.loads(open('client_secrets.json', 'r').read())['TEST_IP']
        # ip = self.request.remote_addr

        # USING GEO COORDINATES
        geo = json.loads(open('client_secrets.json', 'r').read())['TEST_GEO']

        # geo = self.request.headers['X-Appengine-CityLatLong']

        # city_name = self.request.headers['X-AppEngine-City']

        hourly_url = "http://api.wunderground.com/api/%s/hourly10day/q/%s.json" % (KEY, geo)

        h = httplib2.Http()
        hourly_result = json.loads(h.request(hourly_url,'GET')[1])


        if hourly_result.get('error') is not None:
            response = make_response(json.dumps(hourly_result.get('error')), 500)
            response.heads['Content-Type'] = 'application/json'
            return response


        forecast_url = "http://api.wunderground.com/api/%s/forecast10day/q/%s.json" % (KEY, geo)
        j = httplib2.Http()
        forecast_result = json.loads(j.request(forecast_url,'GET')[1])

        if forecast_result.get('error') is not None:
            response = make_response(json.dumps(forecast_result.get('error')), 500)
            response.heads['Content-Type'] = 'application/json'
            return response


        today, rest = get_all_weather(hourly_result, forecast_result)

        city_name = "New York, NY"
        return self.render("main_page.html", today=today, rest=rest, city_name=city_name)



    def post(self):
        if self.request.get("city"):
            city = self.request.get('city')
            city_n = "_".join(city.split(" "))

            state = self.request.get('state')
            location = ",".join([city_n, state])

            city = casing(city)
            city_name = ", ".join([city, state])

            KEY = json.loads(open('client_secrets.json', 'r').read())['UNDERGROUND']


            hourly_url = "http://api.wunderground.com/api/%s/hourly10day/q/%s.json" % (KEY, location)


            h = httplib2.Http()
            hourly_result = json.loads(h.request(hourly_url,'GET')[1])

            if hourly_result.get('error') is not None:
                response = make_response(json.dumps(hourly_result.get('error')), 500)
                response.heads['Content-Type'] = 'application/json'
                return response


            forecast_url = "http://api.wunderground.com/api/%s/forecast10day/q/%s.json" % (KEY, location)


            j = httplib2.Http()
            forecast_result = json.loads(j.request(forecast_url,'GET')[1])



            if forecast_result.get('error') is not None:
                response = make_response(json.dumps(forecast_result.get('error')), 500)
                response.heads['Content-Type'] = 'application/json'
                return response


            today, rest = get_all_weather(hourly_result, forecast_result)
            if today == None:
                return self.redirect('/')
            else:
                return self.render("main_page.html", today=today, rest=rest, city_name=city_name)

#
# class TestPage(Handler):
#         def get(self):
#             ip = self.request.remote_addr
#             test = self.request.headers['X-Appengine-CityLatLong']
#
#
#             return self.render("test.html", ip=ip, test=test)




app = webapp2.WSGIApplication([ ("/", MainPage)
                                ])
                                # debug=True)
