import os
import jinja2
import webapp2

template_dir = os.path.join(os.path.dirname(__file__), 'templates')
jinja_env = jinja2.Environment(loader = jinja2.FileSystemLoader(template_dir),
                                autoescape = True)



class Handler(webapp2.RequestHandler):

    '''
    This class is the parent handler class
    '''

    def write(self, *a, **keywords):
        """
        write:  Method for writing an html response.
        Args:
            *a (data type: str):
            **keywords (data type: str):
        Returns:
            Does not return a value
        """
        return self.response.out.write(*a, **keywords)


    def render_str(self, template, **params):
        """
        render_str:  Method for writing an html response.
        Args:
            template (data type: str): Name of html template file.
            **params (data type: list): Parameters and their values.
        Returns:
            Returns a template rendered with the specified parameters as well as
            the user params.
        """
        temp = jinja_env.get_template(template)
        return temp.render(params)


    def render(self, template, **keywords):
        """
        render: Method for rendering html page
        Args:
            template (data type: str):  Name of html template file.
            **keywords (data type: list): List of keywords and their values.
        Returns:
            Returns a rendered html template.
        """
        return self.write(self.render_str(template, **keywords))
