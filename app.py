from flask import Flask, escape, url_for, render_template
import generate

#__special python flask notes so it knows where to look for
app = Flask(__name__)

post = [generate.generateOutput("have you ever noticed",300)]
#post = ["Hello!"]

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html', posts = post[0]);


@app.route('/showwords')
def showwords():
	return post


if __name__ == "__main__":
    app.run(debug=True)

