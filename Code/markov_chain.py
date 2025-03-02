import random
from collections import defaultdict

class MarkovChain:
    def __init__(self):
        self.chain = defaultdict(list)
    def learn(self, corpus):
        """Builds a Markov chain from a list of words."""
        for i in range(len(corpus) - 1):
            self.chain[corpus[i]].append(corpus[i + 1])
    def generate_sentence(self, length=10):
        """Generates a sentence using the Markov chain."""
        if not self.chain:
            return ""
        
        word = random .choice(list(self.chain.keys()))
        sentence = [word]

        for _ in range(length - 1):
            next_words = self.chain.get(word, [])
            if not next_words:
                break
            word = random.choice(next_words)
            sentence.append(word)

        return " ".join(sentence)
    