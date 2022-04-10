from functools import cmp_to_key
from pprint import pprint

def load_words(filename):
    with open(filename) as f:
        return f.read().splitlines()


def get_positional_frequency(words, alphabet, k=5):
    positional_frequency = {
        position: {
            letter: 0 for letter in alphabet
        } for position in range(k)
    }
    
    for word in words:
        assert len(word) == k, f"There is a word that does not have {k} letters!"
        for position in range(k):
            letter = word[position]
            positional_frequency[position][letter] += 1
    
    positional_total_frequency = {
        position: sum(positional_frequency[position].values()) for position in range(k)
    }

    relative_positional_frequency = {
        position: {
            letter: (positional_frequency[position][letter] / positional_total_frequency[position]) for letter in alphabet
        } for position in range(k)
    }

    return relative_positional_frequency


def get_positional_coverage(relative_positional_frequency, words, k=5):
    positional_coverage = {}

    for word in words:
        positional_coverage[word] = 0

        for position, letter in enumerate(word):
            positional_coverage[word] += relative_positional_frequency[position][letter]

        # Get relative coverage.
        positional_coverage[word] /= k
    
    def compare_word_coverage(a, b):
        """ If two words have the same coverage,
        then prioritize the one that has less duplicate
        letters.  
        """
        word_a, freq_a = a
        word_b, freq_b = b
        if abs(freq_a - freq_b) <= 0.00001:
            return len(set(word_a)) - len(set(word_b))
        else:
            return freq_a - freq_b

    positional_coverage = dict(sorted(
        positional_coverage.items(),
        key=cmp_to_key(compare_word_coverage),
        reverse=True
    ))

    # Find only words where all K letters are distinct,
    # since that maximizes the probability of "hitting"
    # a correct letter (albeit, not necessarily in
    # the right position).
    positional_coverage = dict(
        filter(
            lambda coverage: len(set(coverage[0])) == k,
            positional_coverage.items()
        )
    )

    return positional_coverage


def main():
    WORDS_PATH = 'words.txt'
    ALPHABET = [
        'a','b','c','d','e','f','g',
        'h','i','j','k','l','m','n',
        'o','p','q','r','s','t','u',
        'v','w','x','y','z'
    ]

    words = load_words(filename=WORDS_PATH)
    # alphabet = "abc"
    # words = ["aaa", "abb", "abc", "cba"]

    # 1. Find relative positional frequency.
    relative_positional_frequency = get_positional_frequency(words, alphabet=ALPHABET)

    # 2. Get the positional "coverage" of each word (sorted in descending order).
    positional_coverage = get_positional_coverage(relative_positional_frequency, words)
    pprint(positional_coverage, sort_dicts=False)

if __name__ == '__main__':
    main()