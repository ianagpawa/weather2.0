
import os
import webapp2
import json
import httplib2
import requests

from Handler import Handler

class MainPage(Handler):
    """
    This class is a child of Handler and is for FrontPage.
    """
    def get(self):
        ip = self.request.remote_addr
        KEY = json.loads(open('client_secrets.json', 'r').read())['UNDERGROUND']
        url = "http://api.wunderground.com/api/%s/forecast/q/autoip.json?geo_ip=%s.json" % (KEY, ip)

        h = httplib2.Http()
        result = json.loads(h.request(url,'GET')[1])

        if result.get('error') is not None:
            response = make_response(json.dumps(result.get('error')), 500)
            response.heads['Content-Type'] = 'application/json'
            print response
            return response
        print result

        return self.render("main_page.html")



app = webapp2.WSGIApplication([ ("/", MainPage),
                                ],
                                debug=True)
