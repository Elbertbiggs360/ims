""" File to hold handlers """
from tornado.web import RequestHandler
import json


class BaseHandler(RequestHandler):
    def prepare(self):
        if self.request.headers.get(
                                    "Content-Type", ""
                                    ).startswith("application/json"):
            self.json_args = json.loads(self.request.body)
        else:
            self.json_args = None

    def update_values(self, item):
        for key, value in self.json_args:
            item[key] = value


class MainHandler(BaseHandler):
    def get(self):
        self.write("API is running at port 8888...")


class Companies(BaseHandler):
    """ Model for All Company data """
    name = "Companies"

    def get(self):
        companies = datastore["companies"]
        self.write({"companies": companies})

    def post(self):
        companies = datastore["companies"]
        item = find_resource(companies, "name", self.json_args["name"])
        if item:
            return self.write("Item {} already exists!".format(item["name"]))
        self.json_args["id"] = companies[-1]["id"]+1
        try:
            temp = companies
            temp.append(self.json_args)
            if write_json_data(info_dir, self.name.lower(), temp):
                companies = temp
                self._status_code = 201
                return self.write(self.json_args)
        except Exception as e:
            self.write(
                "Error adding new company.\n{}".format(e)
                )


class Company(BaseHandler):
    """
        model for individual company data
    """
    name = "Company"

    def get(self, id):
        companies = datastore["companies"]
        if id:
            try:
                return self.write(find_resource(companies, "id", int(id)))
            except Exception as e:
                self._status_code = 404
                return self.write("{} not found".format(self.name))
        self.redirect("/companies")

    def put(self, id):
        companies = datastore["companies"]
        if id:
            try:
                temp = companies
                item = find_resource(temp, "id", int(id))
                if write_json_data(info_dir, self.name.lower(), temp):
                    companies = temp
                    self._status_code = 200
                    res = "Item with id {} updated successfully!".format(id)
                    return self.write(res)
            except Exception as e:
                self._status_code = 404
                return self.write("Resource does not exist -> {}".format(e))
        self.write("No id specified!")

    def post(self, id):
        self.redirect("/companies", permanent=True)

    def delete(self, id):
        companies = datastore["companies"]
        if id:
            try:
                temp = companies
                item = find_resource(temp, "id", int(id))
                del temp[item["id"]]
                if write_json_data(info_dir, self.name.lower(), temp):
                    companies = temp
                    self._status_code = 200
                    res = "Item with id {} deleted successfully!".format(id)
                    return self.write(res)
            except Exception as e:
                self._status_code = 404
                return self.write("Resource does not exist")
        self.write("No id specified!")


class Addresses(BaseHandler):
    """ Model for Address data """
    def get(self):
        addresses = datastore["addresses"]
        self.write({"addresses": addresses})


class Address(BaseHandler):
    """ Model for Address data """
    def get(self, id):
        companies = datastore["companies"]
        if id:
            try:
                return self.write(find_resource(companies, "id", int(id)))
            except Exception as e:
                self._status_code = 404
                return self.write("{} not found".format(self.name))
        self.redirect("/companies")

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