from flask import Flask, escape, url_for, render_template, jsonify, request, render_template_string
import os
import json
import generate

app = Flask(__name__)

# reading json file that stores all the lines
filename = os.path.join(app.static_folder, 'store.json')
with open(filename) as blog_file:
    data = json.load(blog_file)
lines = [data]

# generate func global variable
post = {'user': "computer",
        'line': generate.generateOutput("it is quite the shame", 100)[0]}

# default display page
@app.route('/', methods=['GET'])
@app.route('/index')
def index():
    with open(filename) as blog_file:
        data = json.load(blog_file)
    lines = [data]
    return render_template('index.html', posts=lines)

# get list
@app.route('/showwords', methods=['GET'])
def showwords():
    return jsonify({'lines': lines})

# generate
@app.route('/generate', methods=['GET', 'POST'])
def generateStuff():
    send = post
    num = str(len(lines[0]))
    #lines[0]['all'][num] = send
    newline = {num: send}
    # write to json
    with open('static/store.json', 'r') as f:
        currentList = json.load(f)
    currentList.update(newline)
    with open(filename, 'w') as fp:
        json.dump(currentList, fp)
    with open(filename) as blog_file:
        data = json.load(blog_file)
    return data


# write to the list
@app.route('/writeTo', methods=['POST'])
def writeTo():
    request_data = request.get_json()
    newLine = {
        'turn': request_data['turn'],
        'line': request_data['line']
    }
    num = str(len(lines[0]['all']))
    lines[0]['all'][num] = newLine
    return jsonify(lines)


if __name__ == "__main__":
    app.run(port=5000, threaded=True, debug=True)


# lines = [{
#     'all':
#     {
#         0: {
#             'turn': 'computer',
#             'line': 'have you ever noticed that it is the voracious eater that has the most calories? We’ve got the most calories of any food, the most calories of any animal.” And it’s true that, with all the calories we burn, we can’t do anything about that. We just lose it. “We’ll eat all the calories that we have.” That’s true. That’s true. If you’ve ever done anything to lose weight, you’ve seen that he’ve got a really good grip on the food, he’s got a really good hand on the food. He’s got a real grip on the food, and he’s got a real hand on the food. You look at a bowl here, and you think, “Wow, I’ve got a bowl of macaroni and cheese. Do I have to add water?'
#         },
#         1: {
#             'turn': 'human',
#             'line': 'NOTHING'
#         },
#         2: {
#             'turn': 'computer',
#             'line': 'Sweet Caroline'
#         }

#     }
# }]

def compile():
    para = ""
    for i in range(len(lines[0])):
        text = lines[0][i]['line']
        para += text
    return para


def genAgin():
    post = {'user': "computer",
            'line': generate.generateOutput("have you ever noticed", 300)[0]}
    return post
