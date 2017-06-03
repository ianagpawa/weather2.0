
import webapp2
from Handler import Handler

class MainPage(Handler):
    """
    This class is a child of Handler and is for FrontPage.
    """
    def get(self):

        return self.render("main_page.html")



app = webapp2.WSGIApplication([ ("/", MainPage),
                                ],
                                debug=True)
