from pprint import pprint

def load_words(filename):
    with open(filename) as f:
        return f.read().splitlines()


def print_unordered_letter_frequency(words, alphabet):
    frequency = {l: 0 for l in alphabet}

    for word in words:
        for letter in word:
            frequency[letter] += 1

    print("\n-- Unordered frequencies!! --\n")
    pprint(frequency)

    # Ordered by value (highest frequency at the top, and vice versa).
    ordered_frequency = {
        k: v for k, v in sorted(
            frequency.items(), key=lambda item: -item[1]
        )
    }
    print("\n-- Ordered frequencies!! --\n")
    pprint(ordered_frequency, sort_dicts=False)


def print_positioned_letter_frequency(words, alphabet):
    posfrequency = {p: {l: 0 for l in alphabet} for p in range(5)}
    
    for word in words:
        assert len(word) == 5, "There is a word that does not have 5 letters!"
        for pos in range(5):
            letter = word[pos]
            posfrequency[pos][letter] += 1

    print("\n-- Unordered positioned frequencies!! --\n")
    pprint(posfrequency)

    # Ordered by value (highest frequency at the top, and vice versa).
    for pos in range(5):
        posfrequency[pos] = {
           k: v for k, v in sorted(
                posfrequency[pos].items(), key=lambda item: -item[1]
            )
        }
    print("\n-- Ordered positioned frequencies!! --\n")
    pprint(posfrequency, sort_dicts=False)



def main():
    WORDS_PATH = 'words.txt'
    alphabet = [
        'a','b','c','d','e','f','g',
        'h','i','j','k','l','m','n',
        'o','p','q','r','s','t','u',
        'v','w','x','y','z'
    ]

    words = load_words(WORDS_PATH)
    print_unordered_letter_frequency(words, alphabet)
    print_positioned_letter_frequency(words, alphabet)

if __name__ == '__main__':
    main()