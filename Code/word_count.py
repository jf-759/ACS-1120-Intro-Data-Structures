from collections import Counter

def build_histogram(word_list):
    """Creates a histogram (word frequency dictionary) from a list of words."""
    return Counter(word_list)