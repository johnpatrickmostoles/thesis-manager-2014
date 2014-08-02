import os
import urllib

from google.appengine.api import users
from google.appengine.ext import ndb

import jinja2
import webapp2

JINJA_ENVIRONMENT = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)

# Adviser Module



class Adviser(ndb.Model):
    Title = ndb.StringProperty(indexed=False)
    First_name = ndb.StringProperty(indexed=False)
    Last_name = ndb.StringProperty(indexed=False)
    Email = ndb.StringProperty(indexed=False)
    Phone_number = ndb.StringProperty(indexed=False)
    Department = ndb.StringProperty(indexed=False)

class AdviserListHandler(webapp2.RequestHandler):
    def get(self):
        adviser = Adviser.query().fetch()
        template_values = {
             "all_adviser": adviser
                }
        template = JINJA_ENVIRONMENT.get_template('adviser_list.html')
        self.response.write(template.render(template_values))


class AdviserSuccessHandler(webapp2.RequestHandler):

    def get(self):
        template = JINJA_ENVIRONMENT.get_template('adviser_success.html')
        self.response.write(template.render())

    def post(self):
        adviser = Adviser()
        adviser.Title = self.request.get('Title')
        adviser.First_name = self.request.get('First_name')
        adviser.Last_name = self.request.get('Last_name')
        adviser.Email = self.request.get('Email')
        adviser.Phone_number = self.request.get('Phone_number')
        adviser.Department = self.request.get('Department')
        adviser.put()
        self.redirect("/adviser/success") 

class ThesisSuccessHandler(webapp2.RequestHandler):
    def get(self):
        template = JINJA_ENVIRONMENT.get_template('thesis_success.html')
        self.response.write(template.render())

    def post(self):
        thesis = Thesis()
        thesis.Thesis_Title = self.request.get('Thesis_Name')
        thesis.Description = self.request.get('Description')
        thesis.School_Year = self.request.get('School_Year')
        thesis.Status = self.request.get('Status')
        thesis.put()
        self.redirect('/thesis/success')



class ModuleThreeMainPage(webapp2.RequestHandler):
    def get(self):
        user = users.get_current_user()
        if user:
            url = users.create_logout_url(self.request.uri)
            url_linktext = 'Logout'
            name = 'Logged in as '+user.nickname()
        else:
            url = users.create_login_url(self.request.uri)
            url_linktext = 'Login'
            name = ''
        template_values = {
        'name': name,
        'url': url,
        'url_linktext': url_linktext
        }
        template = JINJA_ENVIRONMENT.get_template('module_three.html')
        self.response.write(template.render(template_values))

class AdviserNewHandler(webapp2.RequestHandler):
    def get(self):
        user = users.get_current_user()
        if user:
            url = users.create_logout_url(self.request.uri)
            url_linktext = 'Logout'
            name = 'Logged in as '+user.nickname()
            template_values = {
            'name': name,
            'url': url,
            'url_linktext': url_linktext
            }
            template = JINJA_ENVIRONMENT.get_template('adviser_new.html')
            self.response.write(template.render(template_values))
        else:
            url = users.create_login_url(self.request.uri)
            url_linktext = 'Login'
            name = ''
            template_values = {
            'name': name,
            'url': url,
            'url_linktext': url_linktext
            }
            template = JINJA_ENVIRONMENT.get_template('sample.html')
            self.response.write(template.render(template_values))

    def post(self):
        adviser = Adviser()
        adviser.Title = self.request.get('Title')
        adviser.First_name = self.request.get('First_name')
        adviser.Last_name = self.request.get('Last_name')
        adviser.Email = self.request.get('Email')
        adviser.Phone_number = self.request.get('Phone_number')
        adviser.Department = self.request.get('Department')
        adviser.put()
        self.redirect('/success')

class AdviserViewHandler(webapp2.RequestHandler):
    def get(self, id):
        adviser = Adviser.get_by_id(long(id))
        template_values  = {
            "adviser" : adviser
        }

        template = JINJA_ENVIRONMENT.get_template('adviser_view.html')
        self.response.write(template.render(template_values))
        pass

#Mem1 Module
class MemberOnePage(webapp2.RequestHandler):

    def get(self):
        guestbook_name = self.request.get('guestbook_name',
                                          DEFAULT_GUESTBOOK_NAME)
        greetings_query = Greeting.query(
            ancestor=guestbook_key(guestbook_name)).order(-Greeting.date)
        greetings = greetings_query.fetch(10)

        if users.get_current_user():
            url = users.create_logout_url(self.request.uri)
            url_linktext = 'Logout'
        else:
            url = users.create_login_url(self.request.uri)
            url_linktext = 'Login'

        template_values = {
            'greetings': greetings,
            'guestbook_name': urllib.quote_plus(guestbook_name),
            'url': url,
            'url_linktext': url_linktext,
        }

        template = JINJA_ENVIRONMENT.get_template('member_one.html')
        self.response.write(template.render(template_values)) 
        
#mem2 module
class MemberTwoPage(webapp2.RequestHandler):

    def get(self):
        guestbook_name = self.request.get('guestbook_name',
                                          DEFAULT_GUESTBOOK_NAME)
        greetings_query = Greeting.query(
            ancestor=guestbook_key(guestbook_name)).order(-Greeting.date)
        greetings = greetings_query.fetch(10)

        if users.get_current_user():
            url = users.create_logout_url(self.request.uri)
            url_linktext = 'Logout'
        else:
            url = users.create_login_url(self.request.uri)
            url_linktext = 'Login'

        template_values = {
            'greetings': greetings,
            'guestbook_name': urllib.quote_plus(guestbook_name),
            'url': url,
            'url_linktext': url_linktext,
        };

        template = JINJA_ENVIRONMENT.get_template('member_two.html')
        self.response.write(template.render(template_values))                     

#Thesis Module
class Thesis(ndb.Model):
    Thesis_Title = ndb.StringProperty(indexed=False)
    Description = ndb.StringProperty(indexed=False)
    School_Year = ndb.StringProperty(indexed=False)
    Status = ndb.StringProperty(indexed=False)        

class ThesisListHandler(webapp2.RequestHandler):
    def get(self):
        thesis = Thesis.query().fetch()
        template_values = {
            "all_thesis": thesis
                }
        template = JINJA_ENVIRONMENT.get_template('thesis_list.html')
        self.response.write(template.render(template_values))

class thesisNewHandler(webapp2.RequestHandler):
    def get(self):
        user = users.get_current_user()
        if user:
            url = users.create_logout_url(self.request.uri)
            url_linktext = 'Logout'
            name = 'Logged in as '+user.nickname()
            template_values = {
            'name': name,
            'url': url,
            'url_linktext': url_linktext
            }
            template = JINJA_ENVIRONMENT.get_template('thesis_new.html')
            self.response.write(template.render(template_values))
        else:
            url = users.create_login_url(self.request.uri)
            url_linktext = 'Login'
            name = ''
            template_values = {
            'name': name,
            'url': url,
            'url_linktext': url_linktext
            }
            template = JINJA_ENVIRONMENT.get_template('sample.html')
            self.response.write(template.render(template_values))

    

class ThesisViewHandler(webapp2.RequestHandler):
    def get(self, id):
        thesis = Thesis.get_by_id(long(id))
        template_values  = {
            "thesis" : thesis
        }

        template = JINJA_ENVIRONMENT.get_template('thesis_view.html')
        self.response.write(template.render(template_values))
        pass
      



class StudentListHandler(webapp2.RequestHandler):
    def get(self):
        student = Student.query().fetch()
        template_values = {
            "all_student": student 
        }

        template = JINJA_ENVIRONMENT.get_template('student_list.html')
        self.response.write(template.render(template_values))   


class StudentViewHandler(webapp2.RequestHandler):
    def get(self, id):
        student = Student.get_by_id(long(id))
        template_values  = {
            "student" : student
        }

        template = JINJA_ENVIRONMENT.get_template('student_view.html')
        self.response.write(template.render(template_values))
        pass    

class Student(ndb.Model):
    first_name = ndb.StringProperty(indexed=False)
    last_name = ndb.StringProperty(indexed=False)
    email = ndb.StringProperty(indexed=False)
    student_number = ndb.StringProperty(indexed=False)

class StudentNewHandler(webapp2.RequestHandler):
    def get(self):
        user = users.get_current_user()
        if user:
            url = users.create_logout_url(self.request.uri)
            url_linktext = 'Logout'
            name = 'Logged in as '+user.nickname()
            template_values = {
            'name': name,
            'url': url,
            'url_linktext': url_linktext
            }
            template = JINJA_ENVIRONMENT.get_template('student_new.html')
            self.response.write(template.render(template_values))
        else:
            url = users.create_login_url(self.request.uri)
            url_linktext = 'Login'
            name = ''
            template_values = {
            'name': name,
            'url': url,
            'url_linktext': url_linktext
            }
            template = JINJA_ENVIRONMENT.get_template('sample.html')
            self.response.write(template.render(template_values))

class StudentNewSuccess(webapp2.RequestHandler):

    def get(self):
        template = JINJA_ENVIRONMENT.get_template('student_success.html')
        self.response.write(template.render())

    def post(self):
        student = Student()
        student.first_name = self.request.get('first_name')
        student.last_name = self.request.get('last_name')
        student.email = self.request.get('email')
        student.student_number = self.request.get('student_number')
        student.put()
        self.redirect("/student/success") 

DEFAULT_GUESTBOOK_NAME = 'default_guestbook'

# We set a parent key on the 'Greetings' to ensure that they are all in the same
# entity group. Queries across the single entity group will be consistent.
# However, the write rate should be limited to ~1/second.

def guestbook_key(guestbook_name=DEFAULT_GUESTBOOK_NAME):
    """Constructs a Datastore key for a Guestbook entity with guestbook_name."""
    return ndb.Key('Guestbook', guestbook_name)

# [START greeting]
class Greeting(ndb.Model):
    """Models an individual Guestbook entry."""
    author = ndb.UserProperty()
    content = ndb.StringProperty(indexed=False)
    date = ndb.DateTimeProperty(auto_now_add=True)
# [END greeting]

class MainPage(webapp2.RequestHandler):

    def get(self):
        guestbook_name = self.request.get('guestbook_name',
                                          DEFAULT_GUESTBOOK_NAME)
        greetings_query = Greeting.query(
            ancestor=guestbook_key(guestbook_name)).order(-Greeting.date)
        greetings = greetings_query.fetch(10)

        if users.get_current_user():
            url = users.create_logout_url(self.request.uri)
            url_linktext = 'Logout'
        else:
            url = users.create_login_url(self.request.uri)
            url_linktext = 'Login'

        template_values = {
            'greetings': greetings,
            'guestbook_name': urllib.quote_plus(guestbook_name),
            'url': url,
            'url_linktext': url_linktext,
        }

        template = JINJA_ENVIRONMENT.get_template('index.html')
        self.response.write(template.render(template_values))
class Guestbook(webapp2.RequestHandler):
    def post(self):
        # We set the same parent key on the 'Greeting' to ensure each Greeting
        # is in the same entity group. Queries across the single entity group
        # will be consistent. However, the write rate to a single entity group
        # should be limited to ~1/second.
        guestbook_name = self.request.get('guestbook_name',
                                          DEFAULT_GUESTBOOK_NAME)
        greeting = Greeting(parent=guestbook_key(guestbook_name))

        if users.get_current_user():
            greeting.author = users.get_current_user()

        greeting.content = self.request.get('content')
        greeting.put()

        query_params = {'guestbook_name': guestbook_name}
        self.redirect('/?' + urllib.urlencode(query_params))

class SignModuleOneOne(webapp2.RequestHandler):
    def post(self):
        # We set the same parent key on the 'Greeting' to ensure each Greeting
        # is in the same entity group. Queries across the single entity group
        # will be consistent. However, the write rate to a single entity group
        # should be limited to ~1/second.
        guestbook_name = self.request.get('guestbook_name',
                                          DEFAULT_GUESTBOOK_NAME)
        greeting = Greeting(parent=guestbook_key(guestbook_name))

        if users.get_current_user():
            greeting.author = users.get_current_user()

        greeting.content = self.request.get('content')
        greeting.put()

        query_params = {'guestbook_name': guestbook_name}
        self.redirect('/module-1/1?' + urllib.urlencode(query_params))

class SignModuleOneTwo(webapp2.RequestHandler):    
    def post(self):
        # We set the same parent key on the 'Greeting' to ensure each Greeting
        # is in the same entity group. Queries across the single entity group
        # will be consistent. However, the write rate to a single entity group
        # should be limited to ~1/second.
        guestbook_name = self.request.get('guestbook_name',
                                          DEFAULT_GUESTBOOK_NAME)
        greeting = Greeting(parent=guestbook_key(guestbook_name))

        if users.get_current_user():
            greeting.author = users.get_current_user()

        greeting.content = self.request.get('content')
        greeting.put()

        query_params = {'guestbook_name': guestbook_name}
        self.redirect('/module-1/2?' + urllib.urlencode(query_params))   

# [END guestbook]



        
application = webapp2.WSGIApplication([
    ('/module/three', ModuleThreeMainPage),

    ('/adviser/new', AdviserNewHandler),
    ('/adviser/list', AdviserListHandler),
    ('/adviser/view/(.*)',AdviserViewHandler),
    ('/adviser/success', AdviserSuccessHandler),
    
    ('/thesis/success',ThesisSuccessHandler),
    ('/thesis/new', thesisNewHandler),
    ('/thesis/list', ThesisListHandler),
    ('/thesis/view/(.*)',ThesisViewHandler),
    
    ('/student/new', StudentNewHandler),
    ('/student/list', StudentListHandler),
    ('/student/success', StudentNewSuccess),
    ('/student/view/(.*)', StudentViewHandler),

    ('/module-1/1', MemberOnePage),
    ('/module-1/2', MemberTwoPage),
    ('/sign', Guestbook),
    ('/', MainPage),
], debug=True)









