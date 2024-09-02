# your code goes here!
class Anagram:
    def __init__(self, word):
        self.word = word
        self.sorted_word = sorted(word)

    def match(self, word_list):
        matches = []
        for enlist_word in word_list:
            if sorted(enlist_word) == self.sorted_word:
                matches.append(enlist_word)
        return matches