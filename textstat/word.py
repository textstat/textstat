from .stats import Stats


class Word(Stats):
    properties = [
        "letters",
        "length",
    ]

    def __repr__(self):
        return f"Word('{self.text}')"

    @property
    def letters(self):
        return list(self.text)

    @property
    def length(self):
        return len(self.letters)
