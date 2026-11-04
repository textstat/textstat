"""Public API cache-isolation regressions using real Spanish resources."""

import unittest

from textstat import backend
from textstat.textstat import textstatistics


class TestDifficultWordsListIsolation(unittest.TestCase):
    def setUp(self):
        # Reset only between cases, never between the mutation and its assertions.
        backend.selections.list_difficult_words.cache_clear()
        backend.selections.set_difficult_words.cache_clear()
        backend.counts.count_difficult_words.cache_clear()
        self.stats = textstatistics()
        self.stats.set_lang("es")

    def test_returned_lists_are_independent(self):
        text = "electroencefalograma electroencefalograma otorrinolaringología"
        for unique in (False, True):
            with self.subTest(unique=unique):
                first = self.stats.difficult_words_list(text, unique=unique)
                second = self.stats.difficult_words_list(text, unique=unique)
                self.assertIsInstance(first, list)
                self.assertEqual(first, second)
                self.assertIsNot(first, second)

    def test_mutation_cannot_change_later_lists_or_uncached_counts(self):
        for index, mutation in enumerate(
            ("clear", "append", "replace", "pop", "reverse")
        ):
            with self.subTest(mutation=mutation):
                # Distinct real input keys isolate cases without masking a mutation.
                text = (
                    "electroencefalograma electroencefalograma otorrinolaringología"
                    + " " * index
                )
                words = self.stats.difficult_words_list(text, unique=False)
                expected = list(words)
                self.assertEqual(
                    expected,
                    [
                        "electroencefalograma",
                        "electroencefalograma",
                        "otorrinolaringología",
                    ],
                )
                if mutation == "clear":
                    words.clear()
                elif mutation == "append":
                    words.append("caller-owned")
                elif mutation == "replace":
                    words[0] = "caller-owned"
                elif mutation == "pop":
                    words.pop()
                else:
                    words.reverse()
                other = textstatistics()
                other.set_lang("es")
                self.assertEqual(
                    other.difficult_words_list(text, unique=False), expected
                )
                # First count call for this input must read the uncorrupted backend.
                self.assertEqual(
                    other.difficult_words(text, unique=False), len(expected)
                )
                self.assertCountEqual(other.difficult_words_list(text), set(expected))

    def test_mutation_cannot_change_first_count(self):
        text = "electroencefalograma electroencefalograma otorrinolaringología"
        words = self.stats.difficult_words_list(text, unique=False)
        self.assertEqual(len(words), 3)
        words.clear()
        self.assertEqual(self.stats.difficult_words(text, unique=False), 3)

    def test_empty_list_mutation_cannot_create_difficult_words(self):
        words = self.stats.difficult_words_list("", unique=False)
        self.assertEqual(words, [])
        words.append("caller-owned")
        self.assertEqual(self.stats.difficult_words_list("", unique=False), [])
        self.assertEqual(self.stats.difficult_words("", unique=False), 0)

    def test_unique_list_mutation_remains_isolated(self):
        text = "electroencefalograma electroencefalograma otorrinolaringología"
        words = self.stats.difficult_words_list(text)
        expected = set(words)
        self.assertEqual(expected, {"electroencefalograma", "otorrinolaringología"})
        words.clear()
        self.assertCountEqual(self.stats.difficult_words_list(text), expected)
        self.assertEqual(self.stats.difficult_words(text), len(expected))
