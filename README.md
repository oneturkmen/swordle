# Swordle

Basic analysis of 5-letter words. Inspired by [Wordle](https://www.nytimes.com/games/wordle/index.html).

**Note:** there are only 5757 words in the dataset from [the Stanford GraphBase](https://www-cs-faculty.stanford.edu/~knuth/sgb.html). 

## Analysis 

#### General letter frequency

Frequency of letters in all 5-letter words (counting duplicate letters within each word):

```
{
    'a': 2348, 'b': 715, 'c': 964, 'd': 1181,
    'e': 3009, 'f': 561, 'g': 679, 'h': 814,
    'i': 1592, 'j': 89,  'k': 596, 'l': 1586,
    'm': 843,  'n': 1285,'o': 1915,'p': 955,
    'q': 53,   'r': 1910,'s': 3033,'t': 1585,
    'u': 1089, 'v': 318, 'w': 505, 'x': 139,
    'y': 886,  'z': 135
}
```

#### Letter frequency at each position

```
{
    0: {
        'a': 296, 'b': 432, 'c': 440, 'd': 311,
        'e': 129, 'f': 318, 'g': 279, 'h': 239,
        'i': 74,  'j': 73,  'k': 91,  'l': 271,
        'm': 298, 'n': 118, 'o': 108, 'p': 386,
        'q': 39,  'r': 268, 's': 724, 't': 376,
        'u': 75,  'v': 109, 'w': 228, 'x': 4,
        'y': 47,  'z': 24
    },
    1: {
        'a': 930, 'b': 32,  'c': 82,  'd': 43,
        'e': 660, 'f': 12,  'g': 24,  'h': 271,
        'i': 673, 'j': 4,   'k': 29,  'l': 360,
        'm': 71,  'n': 168, 'o': 911, 'p': 113,
        'q': 10,  'r': 456, 's': 40,  't': 122,
        'u': 534, 'v': 27,  'w': 81,  'x': 33,
        'y': 65,  'z': 6
    },
    2: {
        'a': 605, 'b': 128, 'c': 184, 'd': 178,
        'e': 397, 'f': 87,  'g': 139, 'h': 39,
        'i': 516, 'j': 8,   'k': 90,  'l': 388,
        'm': 209, 'n': 410, 'o': 484, 'p': 169,
        'q': 4,   'r': 475, 's': 248, 't': 280,
        'u': 313, 'v': 121, 'w': 98,  'x': 67,
        'y': 68,  'z': 52
    },
    3: {
        'a': 339, 'b': 99,  'c': 210, 'd': 218,
        'e': 1228,'f': 100, 'g': 176, 'h': 73,
        'i': 284, 'j': 4,   'k': 243, 'l': 365,
        'm': 188, 'n': 386, 'o': 262, 'p': 196,
        'q': 0,   'r': 310, 's': 257, 't': 447,
        'u': 154, 'v': 61,  'w': 70,  'x': 5,
        'y': 41,  'z': 41
    },
    4: {
        'a': 178, 'b': 24,  'c': 48,  'd': 431,
        'e': 595, 'f': 44,  'g': 61,  'h': 192,
        'i': 45,  'j': 0,   'k': 143, 'l': 202,
        'm': 77,  'n': 203, 'o': 150, 'p': 91,
        'q': 0,   'r': 401, 's': 1764,'t': 360,
        'u': 13,  'v': 0,   'w': 28,  'x': 30,
        'y': 665, 'z': 12
    }
}
```

#### Good starter words


I use the following logic to derive a good starter word:
1. Calculate frequency of all letters (i.e., number of unique occurrences in words; do not double count). Sum all frequency counts.

```python
# Given a list of words,
"aaa"
"abb"
"abc"

# we get the corresponding dictionary of frequencies:
{
    "a": 3,  # 'a' occurs in 3 words, and so on.
    "b": 2,
    "c": 1,
}
# and sum of all frequencies is:
3 + 2 + 1 = 6
```

2. Calculate letter "coverage", which shows the percentage of letters (from alphabet of all words) covered by a word. The idea here is that we want to cover as many *unique* letters as possible for maximum diversity. The diversity helps us maximize likelihood of hitting at least one letter. We want a good starting word, not the "one-and-done" kind.

```python
"aaa"
# ==> take unique letter 'a'
# ==> freq['a'] / n
# ==> 3/6 = 50%
# Coverage: 50%

"abb"
# ==> take unique letters 'a', 'b'
# ==> (freq['a'] / n) + (freq['b'] / n)
# ==> (3/6) + (2/6) = 83%
# Coverage: 83%

"abc"
# ==> take unique letters 'a', 'b', 'c'
# ==> (freq['a'] / n) + ... + (freq['c'] / n)
# ==> (3/6) + (2/6) + (1/6) = 100%
# Coverage: 100%
```

3. Sort by coverage in descending order.
4. Drink some coffee and enjoy a chocolatine.

One of the disadvantages of this approach is that if we have two equally "good" words, which one do we choose?

```python
# From the example above,
"abc"  # Coverage: 100%
"cba"  # Coverage: 100%
```

For example, should we choose `"abc"` over `"cba"`? Or vice versa?
In such case, we should consider proportion of each letter *in each position* (0th to 4th indices). 
