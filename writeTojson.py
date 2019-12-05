import json
import os
from flask import jsonify, request
import generate

# reading json file that stores all the lines
site_root = os.path.realpath(os.path.dirname(__file__))
filename = os.path.join(site_root, "static", 'store.json')

# return the json in a list format


def giveList():
    with open(filename) as blog_file:
        data = json.load(blog_file)
    lines = [data]
    return lines

# return the length of the index


def lenList():
    with open(filename) as blog_file:
        data = json.load(blog_file)
    lines = [data]
    num = str(len(lines[0]))
    return num

# append new info to the current json


def updateList(newline):
    with open('static/store.json', 'r') as f:
        currentList = json.load(f)
    currentList.update(newline)
    with open(filename, 'w') as fp:
        json.dump(currentList, fp)
    with open(filename) as blog_file:
        data = json.load(blog_file)
    return data

# pass the generated content to update


def passGen(prefix):
    text = generate.generateOutput(prefix, 100)
    textClean = text[0].strip(prefix)
    textClean = textClean.replace('\n', '')
    post = {'turn': "com-com agent",
            'line': textClean}
    num = lenList()
    newline = {num: post}
    data = updateList(newline)
    return data

# pass user created content to update


def userAdd(request_data):
    send = {
        'turn': request_data["turn"],
        'line': request_data["line"]
    }
    num = lenList()
    newline = {num: send}
    data = updateList(newline)
    return jsonify(data)
