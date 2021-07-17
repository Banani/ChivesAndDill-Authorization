from os.path import join, dirname

from flask import Flask

from chives.map.map import gamemap

app = Flask(__name__)


@app.route('/')
def hello_world():
    return {}


@app.route('/map')
def get_map():
    try:
        return gamemap(resource('maps/root.svg'))
    except FileNotFoundError:
        return {}, 404


def resource(filename: str) -> str:
    with open(join(dirname(__file__), '..', 'resources', filename)) as file:
        return file.read()


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')
