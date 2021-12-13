from flask import Flask
from flask import render_template  # Using for html templates
from flask import url_for

app = Flask(__name__)


@app.route('/')  # '@' is a decorator. In brackets path to a specific page on a website.
@app.route('/home')
def index():
    return render_template("index.html")  # Show specific page from 'templates' directory on domain name '.../home'


@app.route('/about')
def about():
    return render_template("about.html")


@app.route('/user/<string:name>/<int:id>')  # <string:name> is name of a unique user.
def user(name, id):
    return "User page: " + name + " - " + str(id)


if __name__ == '__main__':
    app.run(debug=True)
