import json

from flask import Flask
app = Flask(__name__)


@app.route("/")
def hello():
    return "Hello World!"


@app.route("/addmoredogs", methods=['POST'])
def add_more_dogs():
    result = {
        "result": 0
    }
    # do some magic here to create output dict
    return json.dumps(result)

if __name__ == "__main__":
    app.debug = True
    app.run()

