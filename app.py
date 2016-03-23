# Michael Snider (mas3ym) - CS 4740 PA4

from flask import Flask, render_template

# Define flask app
app = Flask(__name__)

@app.route('/')
def index():
    """ Render index page """
    return render_template('index.html')

# Run app
if __name__ == "__main__":
    app.run(host="0.0.0.0")
