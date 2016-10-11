"""
pre-process all data formats
"""
import pandas as pd
import mmap
import json


def json_to_dataframe(json_object):
    """
    takes as input a json file and creates a dataframe object from it
    """
    # # read the entire file into a python array
    with open(json_object, 'rb') as f:
        data = f.readlines()

    # data_json_str = []

    # with open(json_object, 'rb') as f:
    #     # Size 0 will read the ENTIRE file into memory!
    #     m = mmap.mmap(f.fileno(), 0, access=mmap.PROT_READ)  # File is open read-only
    #
    #     # Proceed with your code here -- note the file is already in memory
    #     # so "readine" here will be as fast as could be
    #     data = m.readline()
    #     while data:
    #         # remove the trailing "\n" from each line
    #         # data = map(lambda x: x.rstrip(), data)
    #         data_json_str.append(json.loads(data))
    #         data = m.readline()

    # remove the trailing "\n" from each line
    data = map(lambda x: x.rstrip(), data)

    # each element of 'data' is an individual JSON object.
    # i want to convert it into an *array* of JSON objects
    # which, in and of itself, is one large JSON object
    # basically... add square brackets to the beginning
    # and end, and have all the individual business JSON objects
    # separated by a comma
    data_json_str = "[" + ','.join(data) + "]"

    data = None

    # return pd.DataFrame(data_json_str)
    return pd.read_json(data_json_str)