import os
from tornado.ioloop import IOLoop
from tornado.web import Application, RequestHandler
from utils import load_json_data, find_resource

info_dir = os.path.join(os.path.dirname(__file__), "mock_data")


class BaseHandler(RequestHandler):
    pass


class MainHandler(BaseHandler):
    def get(self):
        self.write("API is running at port 8888...")


class Companies(BaseHandler):
    """ Model for All Company data """
    def get(self, id):
        companies = datastore["companies"]
        if id:
            return self.write(find_resource(companies, "id", int(id)))
        self.write({"companies": companies})

    def post(self):
        pass


class Addresses(BaseHandler):
    """ Model for Address data """
    def get(self, id):
        addresses = datastore["addresses"]
        if id:
            return self.write(find_resource(addresses, "id", int(id)))
        self.write({"addresses": addresses})

    def post(self):
        pass


class People(BaseHandler):
    """ Model for People data """
    def get(self, id):
        people = datastore["people"]
        if id:
            return self.write(find_resource(people, "id", int(id)))
        self.write({"people": people})

    def post(self):
        pass


class Files(BaseHandler):
    """ Model for Files data """
    def get(self, id):
        files = datastore["files"]
        if id:
            return self.write(find_resource(files, "id", int(id)))
        self.write({"files": files})

    def post(self):
        pass


class Departments(BaseHandler):
    """ Model for Departments data """
    def get(self, id):
        departments = datastore["departments"]
        if id:
            return self.write(find_resource(departments, "id", int(id)))
        self.write({"departments": departments})

    def post(self):
        pass


class Contacts(BaseHandler):
    """ Model for Contacts data """
    def get(self, id):
        contacts = datastore["contacts"]
        if id:
            return self.write(find_resource(contacts, "id", int(id)))
        self.write({"contacts": contacts})

    def post(self):
        pass


class Employees(BaseHandler):
    """ Model for Employees data """
    def get(self, id):
        employees = datastore["employees"]
        if id:
            return self.write(find_resource(employees, "id", int(id)))
        self.write({"employees": employees})

    def post(self):
        pass


class Spectrum(BaseHandler):
    """ Model for Spectrum data """
    def get(self, id):
        spectrum = datastore["spectrum"]
        if id:
            return self.write(find_resource(spectrum, "id", int(id)))
        self.write({"spectrum": spectrum})

    def post(self):
        pass


class TypeApproval(BaseHandler):
    """ Model for Type Approval data """
    def get(self, id):
        typeapproval = datastore["typeapproval"]
        if id:
            return self.write(find_resource(files, "id", int(id)))
        self.write({"typeapproval": typeapproval})

    def post(self):
        pass


class Numbering(BaseHandler):
    """ Model for Numbering data """
    def get(self, id):
        numbering = datastore["numbering"]
        if id:
            return self.write(find_resource(numbering, "id", int(id)))
        self.write({"numbering": numbering})

    def post(self):
        pass


class Broadcasting(BaseHandler):
    """ Model for Broadcasting data """
    def get(self, id):
        broadcasting = datastore["broadcasting"]
        if id:
            return self.write(find_resource(broadcasting, "id", int(id)))
        self.write({"broadcasting": broadcasting})

    def post(self):
        pass


class Postal(BaseHandler):
    """ Model for Postal data """
    def get(self, id):
        postal = datastore["postal"]
        if id:
            return self.write(find_resource(postal, "id", int(id)))
        self.write({"postal": postal})

    def post(self):
        pass


class Telecom(BaseHandler):
    """ Model for Technical Telecom data """
    def get(self, id):
        telecom = datastore["telecom"]
        if id:
            return self.write(find_resource(telecom, "id", int(id)))
        self.write({"telecom": telecom})

    def post(self):
        pass


# Define constant with handlers for different routes
HANDLERS = [
        (r"/", MainHandler),
        ("/companies/([^/]+)?", Companies),
        ("/addresses/([^/]+)?", Addresses),
        ("/people/([^/]+)?", People),
        ("/files/([^/]+)?", Files),
        ("/departments/([^/]+)?", Departments),
        ("/contacts/([^/]+)?", Contacts),
        ("/employees/([^/]+)?", Employees),
        ("/spectrum/([^/]+)?", Spectrum),
        ("/typeapproval/([^/]+)?", TypeApproval),
        ("/numbering/([^/]+)?", Numbering),
        ("/broadcasting/([^/]+)?", Broadcasting),
        ("/postal/([^/]+)?", Postal),
        ("/telecom/([^/]+)?", Telecom)
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
