import json
from flask import request

from flask import Flask
app = Flask(__name__)


@app.route("/")
def hello():
    return "Hello World!"


@app.route("/addmoredogs", methods=['POST'])
def add_more_dogs():
    document = request.get_json()
    result = {
        "total": 0
    }

    for dog in document["dogs"]:

        # Increment the total.
        result["total"] += 1

        thisDogsSize = dog["size"]

        # Ensure this dog's size is represented in the result.
        if thisDogsSize not in result:
            result[thisDogsSize] = 0

        # Increment the number of dogs of this size.
        result[thisDogsSize] += 1

    # do some magic here to create output dict
    return json.dumps(result)

if __name__ == "__main__":
    app.debug = True
    app.run()

