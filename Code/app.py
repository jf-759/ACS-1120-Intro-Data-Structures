"""Main script, uses other modules to generate sentences."""
from flask import Flask
from histogram import histogram
from markov_chain import MarkovChain
from markov_chain_v2 import MarkovChain
from sentence import create_sentence
import cleanup
import tokens
import word_count
import random

app = Flask(__name__)

mc = MarkovChain()

def load_histogram_and_train_markov(filename='Code/filename.txt'):
    """Load and process the text file to generate a histogram and train MarkovChain."""
    global mc

    if mc.chain: 
        return
    
    try:
        text = cleanup.read_file(filename)
        clean_text = cleanup.clean_text(text)
        word_list = tokens.tokenize(clean_text)
        histogram = word_count.build_histogram(word_list)

        mc.learn(word_list)

        if not histogram:
            print("Warning: Histogram is empty!")

        return histogram

    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")
        return None
    
    except Exception as e:
        print(f"An error occured: {e}")
        return None

@app.route("/")
def home():
    """Route that returns a web page containing the generated sentences."""
    hist = load_histogram_and_train_markov()

    if not mc.chain: # if file is not found
        return "<p>Error: No data found in filename.txt</p>"
    
    sentence = mc.generate_sentence(10)

    return f"<p>{sentence}<p>"

if __name__ == "__main__":
    """To run the Flask server, execute `python app.py` in your terminal.
       To learn more about Flask's DEBUG mode, visit
       https://flask.palletsprojects.com/en/2.0.x/server/#in-code"""
    app.run(debug=True)
