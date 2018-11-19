import os
from tornado.ioloop import IOLoop
from tornado.web import Application, RequestHandler
from utils import load_json_data

info_dir = os.path.join(os.path.dirname(__file__), "mock_data")


class BaseHandler(RequestHandler):
    pass


class MainHandler(BaseHandler):
    def get(self):
        self.write("API is running at port 8888...")


class Companies(BaseHandler):
    """ Model for Company data """
    def get(self):
        self.write({"companies": datastore["companies"]})

    def post(self):
        pass


class Addresses(BaseHandler):
    """ Model for Address data """
    def get(self):
        self.write({"addresses": datastore["addresses"]})

    def post(self):
        pass


class People(BaseHandler):
    """ Model for People data """
    def get(self):
        self.write({"people": datastore["people"]})

    def post(self):
        pass


class Files(BaseHandler):
    """ Model for Files data """
    def get(self):
        self.write({"files": datastore["files"]})

    def post(self):
        pass


class Departments(BaseHandler):
    """ Model for Departments data """
    def get(self):
        self.write({"departments": datastore["departments"]})

    def post(self):
        pass


class Contacts(BaseHandler):
    """ Model for Contacts data """
    def get(self):
        self.write({"contacts": datastore["contacts"]})

    def post(self):
        pass


class Employees(BaseHandler):
    """ Model for Employees data """
    def get(self):
        self.write({"employees": datastore["employees"]})

    def post(self):
        pass


class Spectrum(BaseHandler):
    """ Model for Spectrum data """
    def get(self):
        self.write({"spectrum": datastore["spectrum"]})

    def post(self):
        pass


class TypeApproval(BaseHandler):
    """ Model for Type Approval data """
    def get(self):
        self.write({
                "type_approval": datastore["typeapproval"]
            })

    def post(self):
        pass


class Numbering(BaseHandler):
    """ Model for Numbering data """
    def get(self):
        self.write({"numbering": datastore["numbering"]})

    def post(self):
        pass


class Broadcasting(BaseHandler):
    """ Model for Broadcasting data """
    def get(self):
        self.write({"broadcasting": datastore["broadcasting"]})

    def post(self):
        pass


class Postal(BaseHandler):
    """ Model for Postal data """
    def get(self):
        self.write({"postal": datastore["postal"]})

    def post(self):
        pass


class Telecom(BaseHandler):
    """ Model for Technical Telecom data """
    def get(self):
        self.write({"telecom": datastore["telecom"]})

    def post(self):
        pass


# Define constant with handlers for different routes
HANDLERS = [
        (r"/", MainHandler),
        ("/companies", Companies),
        ("/addresses", Addresses),
        ("/people", People),
        ("/files", Files),
        ("/departments", Departments),
        ("/contacts", Contacts),
        ("/employees", Employees),
        ("/spectrum", Spectrum),
        ("/typeapproval", TypeApproval),
        ("/numbering", Numbering),
        ("/broadcasting", Broadcasting),
        ("/postal", Postal),
        ("/telecom", Telecom)
    ]
datastore = {}


def make_app():
    """ instantiate application """
    app = Application(HANDLERS, debug=True)
    for handler in HANDLERS:
        name = handler[0].split("/")[1]
        item = name
        if not item.strip():
            continue
        item = load_json_data(info_dir, name)
        datastore[name] = item
    return app

if __name__ == "__main__":
    app = make_app()
    app.listen(8888)
    IOLoop.current().start()
