# your code goes here!
class Anagram:
    def __init__(self, word):
        self.word = word.lower()
        self.sorted_letters = sorted(self.word)

    def match(self, candidates):
        return [word for word in candidates if word.lower() != self.word and sorted(word.lower()) == self.sorted_letters]
