""" Helper methods """
import os
import json


def load_json_data(file_path, file_name):
    """
        this function loads JSON blobs from files on the path
    """
    # TODO create a read-safe method
    data = open(os.path.join(file_path, "%s.json" % file_name), 'r')
    json_data = json.load(data)
    return json_data


def find_resource(source, key, target):
    """
        method to find target by given key in a source
    """
    for item in source:
        if item[key] is target:
            return item
