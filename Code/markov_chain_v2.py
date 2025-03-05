import random
from collections import defaultdict

class MarkovChain:
    def __init__(self):
        self.chain = defaultdict(list)

    def read_corpus(self, filename):
        """Reads a file and splits its content into a list of words."""
        with open(filename, 'r') as file:
            text = file.read()
            corpus = text.split()

        return corpus
    
    def learn(self, corpus):
        """Builds a Markov chain from a list of words."""

        for i in range(len(corpus) - 1):
            self.chain[corpus[i]].append(corpus[i + 1])

    def generate_sentence(self, length=10):
        """Generates a sentence using the Markov Chain."""

        if not self.chain:
            return ""
        
        word = random.choice(list(self.chain.keys()))
        sentence = [word]

        for _ in range(length - 1):
            next_words = self.chain.get(word, [])
            if not next_words:
                break

            word = random.choice(next_words)
            sentence.append(word)

        return " ".join(sentence)
    

if __name__ == "__main__":
    
    filename = 'Code/filename.txt'
    markov = MarkovChain()

    corpus = markov.read_corpus(filename)
    markov.learn(corpus)

    generate_sentence = markov.generate_sentence(length=10)
    print("Generated Sentence: ", generate_sentence)





# class MarkovChain:

#     def __init__(self, order=2):
#         """Initializes the Markov chain with a given order (n)."""
#         self.order = order
#         self.chain = defaultdict(lambda: defaultdict(int))

#     def learn(self, corpus):
#         """Builds an n-th order Markov chain from a list of words."""
#         history = []

#         for word in corpus:
#             if len(history) == self.order:
#                 ngram = tuple(history)
#                 self.chain[ngram][word] += 1

#                 history.pop(0)

#             history.append(word)

#         if len(history) == self.order:
#             ngram = tuple(history)
#             self.chain[ngram][None] += 1


#     def generate_sentence(self, start_tokens=None, length=30):
#         """Generates a sentence using the Markov chain based on the given start tokens."""

#         if not self.chain:
#             return ""
        
#         if start_tokens is None:
            
#             start_tokens = random.choice(list(self.chain.keys()))
        
#         if not isinstance(start_tokens, (list, tuple)):
#             raise TypeError("start_tokens must be a list or a tuple of words.")
        
#         if len(start_tokens) > self.order:
            
#             start_tokens = tuple(start_tokens[-self.order:])


#         sentence = list(start_tokens)

#         for _ in range(length - self.order):

#             ngram = tuple(sentence[-self.order:])
#             next_word = self.get_next_word(ngram)
            
#             if next_word is None:
#                 break

#             sentence.append(next_word)

#         return " ".join(sentence)
    
#     def get_next_word(self, ngram):
#         """Helper method to pick the next word based on the current n-gram."""

#         next_words = self.chain[ngram]
#         total_count = sum(next_words.values())

#         if total_count == 0:
#             return None
        
#         rand_choice = random.randint(1, total_count)
#         cumulative = 0

#         for word, count in next_words.items():
            
#             cumulative += count
            
#             if cumulative >= rand_choice:
#                 return word
            
#         return None
    

# if __name__ == "__main__":
#     filename = 'Code/filename.txt'
#     with open(filename, 'r') as file:
#         text = file.read()
#         corpus = text.split()

#     markov_chain = MarkovChain(order=2)
#     markov_chain.learn(corpus)

#     generated_sentence = markov_chain.generate_sentence(start_tokens=["I"], length = 10)
#     print("Generated Sentence: ", generated_sentence)