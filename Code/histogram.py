import string

def clean_word(word):
    """Remove punctuation from a word and convert it to lowercase."""
    return word.translate(str.maketrans('', '', string.punctuation)).lower()

def dictogram (filename):
    """Read a file and create a histogram (word frequency dictionary)."""
    histogram = {}
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            for line in f:
                for word in line.split():
                    cleaned_word = clean_word(word)
                    if cleaned_word:
                        histogram[cleaned_word] = histogram.get(cleaned_word, 0) + 1
    
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
        return{}
    return histogram

def unique_words(histogram):
    """Return the number of unique words in the histogram."""
    return len (histogram)

def frequency(word, histogram):
    """Return the frequency count of a word in the histogram."""
    cleaned_word = clean_word(word)
    return histogram.get(cleaned_word, 0)


if __name__ == '__main__':

    filename = 'Code/filename.txt'
    dict = dictogram(filename)

    print(f'Total unique words: {unique_words(dict)}')
    print(f"Frequency of 'the': {frequency('the', dict)}")
 

    