# Michael Snider (mas3ym) - CS 4740 PA4
from flask import Flask, render_template, request
import grader

# Define flask app
app = Flask(__name__)

# Constants
STORED_FILENAME = "walk.cc"

@app.route('/', methods=['POST', 'GET'])
def index():
    """ Render index page """
    # Data to pass to the page
    uploaded = False
    errors = []
    compiled = False
    score = 0
    text = ""
    
    # Check uploaded file
    if request.method == 'POST':
        codeFile = request.files["codeFile"]
        uploaded = codeFile.filename != ""
    
    # Handle uploaded file
    if request.method == 'POST' and not uploaded:
        # Push error
        errors.append("You forgot to upload the file!")
    elif uploaded:
        # Save file
        codeFile.save(STORED_FILENAME)
        # Test code
        results = grader.test_submission(STORED_FILENAME)
        # Set results
        compiled = results["compiled"]
        score = results["score"]
        has_file = results["has_file"]
        text = results["text"]
        # In case no file now...
        if not has_file:
            errors.append("Unable to process the uploaded file.")
            uploaded = False
    
    # Render page
    return render_template('index.html', uploaded=uploaded, errors=errors, \
                           compiled=compiled, score=score, text=text)

# Run app
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80)
