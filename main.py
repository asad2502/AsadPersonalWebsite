# you have to import flask or install if not installed already
import flask

# make app using flask
app = flask.Flask(__name__)




# make function

@app.route('/')
def mainpage():
    return '<h1>Good morning, world</h1>'




# run app
if __name__ == '__main__':
    app.run(debug=True)