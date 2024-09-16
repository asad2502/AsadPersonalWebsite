# you have to import flask or install if not installed already
import flask
from flask import render_template

# make app using flask
app = flask.Flask(__name__)




# make function

@app.route('/extra')
def mainpage():
    return '<h1>Good morning, world</h1>'

@app.route('/')
def landingpage():
    return render_template('landingpage.html')
@app.route('/about')
def aboutpage():
    return render_template('aboutpage.html')
@app.route('/todolist')
def todolist():
    return render_template('todolist.html')
@app.route('/calculator')
def calculator():
    return render_template('calculator.html')
@app.route('/projects')
def projects():
    return render_template('projects.html')

# run app
if __name__ == '__main__':
    app.run(debug=True)