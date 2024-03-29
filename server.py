from flask import Flask
from flask import render_template

app = Flask(__name__)


@app.route("/")
def hello(name=None):
    return render_template('index.html', name=name)

@app.route("/project")
def project(name=None):
    return render_template('project.html', name=name)