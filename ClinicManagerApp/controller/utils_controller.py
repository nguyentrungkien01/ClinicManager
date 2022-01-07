import json
import os

from ClinicManagerApp import app


def readJsonFile(filename):
    if filename:
        with open(os.path.join(app.root_path, 'data/{}'.format(filename)),
                  encoding='utf-8') as f:
            return json.load(f)


def writeJsonFile(filename, data):
    if filename:
        with open(os.path.join(app.root_path, 'data/{}'.format(filename)), 'w',
                  encoding='utf-8') as f:
            return json.dump(data, f, ensure_ascii=True, indent=4)
