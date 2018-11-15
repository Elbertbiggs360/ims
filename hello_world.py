import tornado.ioloop
from tornado.web import Application, RequestHandler

class BaseHandler(RequestHandler):
  pass

class MainHandler(BaseHandler):
  def get(self):
    self.write({'message': 'API is running...'})

def make_app():
  return Application([
    (r"/", MainHandler)
  ], debug=True)

if __name__ == "__main__":
    app = make_app()
    app.listen(8888)
    tornado.ioloop.IOLoop.current().start()
