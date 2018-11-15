import tornado.ioloop
from tornado.web import Application, RequestHandler

companies=addresses=people=files=departments=contract = []

class BaseHandler(RequestHandler):
  pass

class MainHandler(BaseHandler):
  def get(self):
    self.write('API is running at port 8888...')

class Companies(BaseHandler):
  def get(self):
    pass
  def post(self):
    pass

class Addresses(BaseHandler):
  def get(self):
    pass
  def post(self):
    pass

class People(BaseHandler):
  def get(self):
    pass
  def post(self):
    pass

class Files(BaseHandler):
  def get(self):
    pass
  def post(self):
    pass

class Departments(BaseHandler):
  def get(self):
    pass
  def post(self):
    pass

class Contacts(BaseHandler):
  def get(self):
    pass
  def post(self):
    pass

class Employees(BaseHandler):
  def get(self):
    pass
  def post(self):
    pass

class Spectrum(BaseHandler):
  def get(self):
    pass
  def post(self):
    pass

class TypeApproval(BaseHandler):
  def get(self):
    pass
  def post(self):
    pass

class Numbering(BaseHandler):
  def get(self):
    pass
  def post(self):
    pass

class Broadcasting(BaseHandler):
  def get(self):
    pass
  def post(self):
    pass

class Postal(BaseHandler):
  def get(self):
    pass
  def post(self):
    pass
    
class Telecom(BaseHandler):
  def get(self):
    pass
  def post(self):
    pass

def make_app():
  return Application([
    (r"/", MainHandler),
    ('/companies', Companies),
    ('/addresses', Addresses),
    ('/people', People),
    ('/files', Files),
    ('/departments', Departments),
    ('/contacts', Contacts),
    ('/employees', Employees),
    ('/spectrum', Employees),
    ('/typeapproval', TypeApproval),
    ('/numbering', Numbering),
    ('/broadcasting', Broadcasting),
    ('/postal', Postal),
    ('/telecom', Telecom)
  ], debug=True)

if __name__ == "__main__":
    app = make_app()
    app.listen(8888)
    tornado.ioloop.IOLoop.current().start()
