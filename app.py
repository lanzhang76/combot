from flask import Flask, escape, url_for, render_template, jsonify, request, render_template_string
import os
import json
import generate
import writeTojson

app = Flask(__name__)

# default display page
@app.route('/', methods=['GET'])
@app.route('/index')
def index():
    return render_template('index.html', posts=writeTojson.giveList())

# get list
@app.route('/showwords', methods=['GET'])
def showwords():
    return jsonify({'lines': writeTojson.giveList()})

# generate
@app.route('/generate', methods=['GET', 'POST'])
def generateStuff():
    if request.method == 'GET':
        return jsonify({'lines':  writeTojson.passGen("")})
    elif request.method == 'POST':
        if request.headers['Content-Type'] == 'application/json':
            request_data = request.json
            prefix = request_data["prefix"]
        return jsonify({'lines':  writeTojson.passGen(prefix)})
    else:
        return "415 Unsupported Media Type ;)"


# write to the list
@app.route('/writeto', methods=['POST'])
def writeTo():
    if request.headers['Content-Type'] == 'application/json':
        request_data = request.json
        return writeTojson.userAdd(request_data)
    else:
        return "415 Unsupported Media Type ;)"


if __name__ == "__main__":
    app.run(port=5000, threaded=True, debug=True)
