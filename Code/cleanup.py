import string
import re

def read_file(filename):
    """Reads text from a file and returns it as a string."""
    with open (filename, 'r', encoding='utf-8') as f:
        return f.read()
    
def clean_text(text):
    """Removes punctuation and converts text to lowercase."""
    text = text.lower()
    text = text.translate(str.maketrans('', '', string.punctuation))

    return text