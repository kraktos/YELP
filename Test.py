# import json_to_csv_converter as j2c
import pandas as pd

if __name__ == '__main__':
    json_file = "world_bank.json"

    # read the entire file into a python array
    with open(json_file, 'rb') as f:
        data = f.readlines()

    # remove the trailing "\n" from each line
    data = map(lambda x: x.rstrip(), data)

    # each element of 'data' is an individual JSON object.
    # i want to convert it into an *array* of JSON objects
    # which, in and of itself, is one large JSON object
    # basically... add square brackets to the beginning
    # and end, and have all the individual business JSON objects
    # separated by a comma
    data_json_str = "[" + ','.join(data) + "]"

    df = pd.read_json(data_json_str)
    print df.shape
    #
    # column_names = j2c.get_superset_of_column_names_from_file(json_file_path=json_file)
    # j2c.read_and_write_file("world_bank.json", "world_bank.csv", column_names)

    print("Done..")