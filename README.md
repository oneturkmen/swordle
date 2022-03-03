# Swordle

Basic analysis of 5-letter words. Inspired by [Wordle](https://www.nytimes.com/games/wordle/index.html).

**Note:** there are only 5757 words in the dataset from [the Stanford GraphBase](https://www-cs-faculty.stanford.edu/~knuth/sgb.html). 

## Analysis 

* **General frequency:** What is the general (unordered) frequency of all letters in 5-letter words?
* **Positioned frequency:** Print positioned (ordered) frequency of all letters in 5-letter words. In other words, find frequency of letters for each position (0 through 4).
* **Good starter word:** Find the starting word which:
    * Has the highest odds of being the target word based on Idea 2, and
    * If it is not the target word, it will most likely expose letters that are in the target word.
