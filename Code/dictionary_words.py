import random
import sys

dictionary_words = '/usr/share/dict/words'
number_of_words = int(sys.argv[1])
words_selected = []

with open(dictionary_words, 'r') as f:
    words = f.readlines()
    for i in range(number_of_words):
        words_selected.append(random.choice(words).strip())

print(" ".join(words_selected))