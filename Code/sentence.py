import random

def weighted_random(histogram):
    """Manually selects a word based on its frequency (weight)."""
    total_weight = sum(histogram.values())
    rand_value = random.randint(1, total_weight)
    cumulative_weight = 0

    for word, weight in histogram.items():
        cumulative_weight += weight
        if rand_value <= cumulative_weight:
            return word
        
def create_sentence(histogram, word_limit = 10):
    """Generates a random sentence from the histogram using weighted random selection."""

    if len(histogram) == 0:
        return "Error: No words available to generate a sentence."
    
    sentence = []
    for _ in range(word_limit):
        sentence.append(weighted_random(histogram))

        sentence = ' '.join(sentence) + '.'

        return sentence.capitalize()