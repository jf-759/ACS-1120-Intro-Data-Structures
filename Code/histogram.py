import string

def histogram (filename):
    histogram = {}
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            for line in f:
                for word in line.split():
                    word = word.lower()
                    histogram[word] = histogram.get(word, 0) + 1
    
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
        return{}
    return histogram

def unique_words(histogram):
    return len (histogram)

def frequency(word, histogram):
    return histogram.get(word, 0)

def clean_word(word):
    return word.translate(str.maketrans('', '', string.punctuation.lower()))


if __name__ == '__main__':

    filename = 'Code/filename.txt'
    hist = histogram(filename)

    print(f'Total unique words: {unique_words(hist)}')
    print(f"Frequency of 'the': {frequency('the', hist)}")
 

    