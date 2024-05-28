class Guess:

    def __init__(self, secret: str):
        self.secret: str = secret
        self.attempts = []
        pass

    def attempt(self, word: str):
        self.attempts.append(word)

    @property
    def is_correct(self):
        return len(self.attempts) > 0 and self.attempts[-1] == self.secret
