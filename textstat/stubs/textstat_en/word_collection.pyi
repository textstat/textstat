from textstat.word_collection import WordCollection as BaseCollection

class WordCollection(BaseCollection):
    @property
    def reading_time(self) -> float: ...
