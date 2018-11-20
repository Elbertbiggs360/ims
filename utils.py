""" Helper methods """
import os
import json


def load_json_data(file_path, file_name):
    """
        this function loads JSON blobs from files on the path
    """
    # TODO create a read-safe method
    with open(os.path.join(file_path, "%s.json" % file_name), "r") as data:
        json_data = json.load(data)
    return json_data


def find_resource(source, key, target):
    """
        method to find target by given key in a source
    """
    for item in source:
        if item[key] is target:
            return item


def write_json_data(file_path, file_name, data):
    """
        write json data to file
    """
    path_to_file = os.path.join(file_path, "%s.json" % file_name)
    with open(path_to_file, "w") as target:
        json.dump(data, target)
        return True
    return False
