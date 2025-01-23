import random

def random_rearrange():
    rearranged = []
    while words:
        rand_index = random.randint(0, len(words) -1)
        rearranged.append(words.pop(rand_index))
    return rearranged

if __name__ == '__main__':
    words = ["how", "now", "brown", "cow"]
    random.shuffle(words)
    print(words)