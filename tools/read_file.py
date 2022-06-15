import app
import json


def read_txt(filename):
    filepath = app.BASE_DIR + "/data/" + filename
    with open(filepath, "r", encoding="utf-8") as f:
        return f.readlines()


def read_json(attr):
    arr = list()
    with open(app.BASE_DIR + "/data/test_data.json", "r", encoding="utf-8") as f:
        result = json.load(f)
        for i in result[attr]:
            row = i.values()
            arr.append(list(row))
        return arr
