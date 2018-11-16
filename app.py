import os
from tornado.ioloop import IOLoop
from tornado.web import Application, RequestHandler
import json

companies = addresses = people = files = departments = contacts = employees \
 = spectrum = type_approval = numbering = broadcasting = postal = telecom = []

info_dir = os.path.join(os.path.dirname(__file__), "mock_data")


class BaseHandler(RequestHandler):
    pass


class MainHandler(BaseHandler):
    def get(self):
        self.write("API is running at port 8888...")


class Companies(BaseHandler):
    """ Model for Company data """
    def get(self):
        name = "companies"
        data = open(os.path.join(info_dir, "%s.json" % name), 'r')
        companies = json.load(data)
        self.write({"companies": companies})

    def post(self):
        pass


class Addresses(BaseHandler):
    """ Model for Address data """
    def get(self):
        name = "locations"
        data = open(os.path.join(info_dir, "%s.json" % name), 'r')
        addresses = json.load(data)
        self.write({"addresses": addresses})

    def post(self):
        pass


class People(BaseHandler):
    """ Model for People data """
    def get(self):
        name = "people"
        data = open(os.path.join(info_dir, "%s.json" % name), 'r')
        people = json.load(data)
        self.write({"people": people})

    def post(self):
        pass


class Files(BaseHandler):
    """ Model for Files data """
    def get(self):
        name = "files"
        data = open(os.path.join(info_dir, "%s.json" % name), 'r')
        files = json.load(data)
        self.write({"files": files})

    def post(self):
        pass


class Departments(BaseHandler):
    """ Model for Departments data """
    def get(self):
        name = "departments"
        data = open(os.path.join(info_dir, "%s.json" % name), 'r')
        departments = json.load(data)
        self.write({"department": departments})

    def post(self):
        pass


class Contacts(BaseHandler):
    """ Model for Contacts data """
    def get(self):
        name = "contacts"
        data = open(os.path.join(info_dir, "%s.json" % name), 'r')
        contacts = json.load(data)
        self.write({"contacts": contacts})

    def post(self):
        pass


class Employees(BaseHandler):
    """ Model for Employees data """
    def get(self):
        name = "employees"
        data = open(os.path.join(info_dir, "%s.json" % name), 'r')
        employees = json.load(data)
        self.write({"employees": employees})

    def post(self):
        pass


class Spectrum(BaseHandler):
    """ Model for Spectrum data """
    def get(self):
        name = "spectrum"
        data = open(os.path.join(info_dir, "%s.json" % name), 'r')
        spectrum = json.load(data)
        self.write({"spectrum": spectrum})

    def post(self):
        pass


class TypeApproval(BaseHandler):
    """ Model for Type Approval data """
    def get(self):
        name = "type_approval"
        data = open(os.path.join(info_dir, "%s.json" % name), 'r')
        type_approval = json.load(data)
        self.write({"type_approval": type_approval})

    def post(self):
        pass


class Numbering(BaseHandler):
    """ Model for Numbering data """
    def get(self):
        name = "numbering"
        data = open(os.path.join(info_dir, "%s.json" % name), 'r')
        numbering = json.load(data)
        self.write({"numbering": numbering})

    def post(self):
        pass


class Broadcasting(BaseHandler):
    """ Model for Broadcasting data """
    def get(self):
        name = "broadcasting"
        data = open(os.path.join(info_dir, "%s.json" % name), 'r')
        broadcasting = json.load(data)
        self.write({"broadcasting": broadcasting})

    def post(self):
        pass


class Postal(BaseHandler):
    """ Model for Postal data """
    def get(self):
        name = "postal"
        data = open(os.path.join(info_dir, "%s.json" % name), 'r')
        postal = json.load(data)
        self.write({"postal": postal})

    def post(self):
        pass


class Telecom(BaseHandler):
    """ Model for Technical Telecom data """
    def get(self):
        name = "telecom"
        data = open(os.path.join(info_dir, "%s.json" % name), 'r')
        telecom = json.load(data)
        self.write({"telecom": telecom})

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


def make_app():
    """ instantiate application """
    return Application(HANDLERS, debug=True)

if __name__ == "__main__":
    app = make_app()
    app.listen(8888)
    IOLoop.current().start()
