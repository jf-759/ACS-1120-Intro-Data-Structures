"""Main script, uses other modules to generate sentences."""
from flask import Flask
from .histogram import histogram
import random

app = Flask(__name__)

hist = histogram('Code/filename.txt') # instantiate

@app.route("/")
def home():
    """Route that returns a web page containing the generated text."""
    if not hist: # if file is not found
        return "<p>Error: No data found in filename.txt</p>"
    
    keys = list(hist.keys())
    index = random.randint(0, len(keys) - 1)
    word = keys[index]

    return f"<p>{word}<p>"

if __name__ == "__main__":
    """To run the Flask server, execute `python app.py` in your terminal.
       To learn more about Flask's DEBUG mode, visit
       https://flask.palletsprojects.com/en/2.0.x/server/#in-code"""
    app.run(debug=True)
