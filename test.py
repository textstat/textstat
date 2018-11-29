# -*- coding: utf-8 -*-

"""Test suite for textstat
"""

import unittest

import textstat


class Test_TextStat(unittest.TestCase):

    def setUp(self):
        self.short_test = "Cool dogs wear da sunglasses."

        self.long_test = ("Playing ... games has always been thought to be "
                          "important to the development of well-balanced and "
                          "creative children; however, what part, if any, "
                          "they should play in the lives of adults has never "
                          "been researched that deeply. I believe that "
                          "playing games is every bit as important for adults "
                          "as for children. Not only is taking time out to "
                          "play games with our children and other adults "
                          "valuable to building interpersonal relationships "
                          "but is also a wonderful way to release built up "
                          "tension.\n"
                          "There's nothing my husband enjoys more after a "
                          "hard day of work than to come home and play a game "
                          "of Chess with someone. This enables him to unwind "
                          "from the day's activities and to discuss the highs "
                          "and lows of the day in a non-threatening, kick back "
                          "environment. One of my most memorable wedding "
                          "gifts, a Backgammon set, was received by a close "
                          "friend. I asked him why in the world he had given "
                          "us such a gift. He replied that he felt that an "
                          "important aspect of marriage was for a couple to "
                          "never quit playing games together. Over the years, "
                          "as I have come to purchase and play, with other "
                          "couples & coworkers, many games like: Monopoly, "
                          "Chutes & Ladders, Mastermind, Dweebs, Geeks, & "
                          "Weirdos, etc. I can reflect on the integral part "
                          "they have played in our weekends and our "
                          "\"shut-off the T.V. and do something more "
                          "stimulating\" weeks. They have enriched my life and "
                          "made it more interesting. Sadly, many adults "
                          "forget that games even exist and have put them "
                          "away in the cupboards, forgotten until the "
                          "grandchildren come over.\n"
                          "All too often, adults get so caught up in working "
                          "to pay the bills and keeping up with the "
                          "\"Joneses'\" that they neglect to harness the fun "
                          "in life; the fun that can be the reward of "
                          "enjoying a relaxing game with another person. It "
                          "has been said that \"man is that he might have "
                          "joy\" but all too often we skate through life "
                          "without much of it. Playing games allows us to: "
                          "relax, learn something new and stimulating, "
                          "interact with people on a different more "
                          "comfortable level, and to enjoy non-threatening "
                          "competition. For these reasons, adults should "
                          "place a higher priority on playing games in their "
                          "lives")


    def test_char_count(self):
        count = textstat.char_count(self.long_test)
        count_spaces = textstat.char_count(self.long_test, ignore_spaces=False)

        self.assertEqual(1750, count)
        self.assertEqual(2123, count_spaces)


    def test_letter_count(self):
        count = textstat.letter_count(self.long_test)
        count_spaces = textstat.letter_count(self.long_test, ignore_spaces=False)

        self.assertEqual(1688, count)
        self.assertEqual(2061, count_spaces)


    def test_lexicon_count(self):
        count = textstat.lexicon_count(self.long_test)
        count_punc = textstat.lexicon_count(self.long_test, removepunct=False)

        self.assertEqual(372, count)
        self.assertEqual(375, count_punc)


    def test_syllable_count(self):
        count = textstat.syllable_count(self.long_test)

        self.assertEqual(521, count)


    def test_sentence_count(self):
        count = textstat.sentence_count(self.long_test)

        self.assertEqual(16, count)


    def test_avg_sentence_length(self):
        avg = textstat.avg_sentence_length(self.long_test)

        self.assertEqual(23.3, avg)


    def test_avg_syllables_per_word(self):
        avg = textstat.avg_syllables_per_word(self.long_test)

        self.assertEqual(1.4, avg)


    def test_avg_letter_per_word(self):
        avg = textstat.avg_letter_per_word(self.long_test)

        self.assertEqual(4.7, avg)


    def test_avg_sentence_per_word(self):
        avg = textstat.avg_sentence_per_word(self.long_test)

        self.assertEqual(0.04, avg)


    def test_flesch_reading_ease(self):
        score = textstat.flesch_reading_ease(self.long_test)

        self.assertEqual(64.75, score)


    def test_flesch_kincaid_grade(self):
        score = textstat.flesch_kincaid_grade(self.long_test)

        self.assertEqual(10.0, score)


    def test_polysyllabcount(self):
        count = textstat.polysyllabcount(self.long_test)

        self.assertEqual(32, count)


    def test_smog_index(self):
        index = textstat.smog_index(self.long_test)

        self.assertEqual(11.2, index)


    def test_coleman_liau_index(self):
        index = textstat.coleman_liau_index(self.long_test)

        self.assertEqual(10.28, index)


    def test_automated_readability_index(self):
        index = textstat.automated_readability_index(self.long_test)

        self.assertEqual(12.3, index)


    def test_linsear_write_formula(self):
        result = textstat.linsear_write_formula(self.long_test)

        self.assertEqual(14.5, result)


    def test_difficult_words(self):
        result = textstat.difficult_words(self.long_test)

        self.assertEqual(49, result)


    def test_dale_chall_readability_score(self):
        score = textstat.dale_chall_readability_score(self.long_test)

        self.assertEqual(6.87, score)


    def test_gunning_fog(self):
        score = textstat.gunning_fog(self.long_test)

        self.assertEqual(14.59, score)


    def test_lix(self):
        score = textstat.lix(self.long_test)

        self.assertEqual(45.11, score)


    def test_text_standard(self):
        standard = textstat.text_standard(self.long_test)

        self.assertEqual("9th and 10th grade", standard)

        standard = textstat.text_standard(self.short_test)

        self.assertEqual("2nd and 3rd grade", standard)


    def test_lru_caching(self):
        #Clear any cache
        textstat.sentence_count._cache.clear()
        textstat.avg_sentence_length._cache.clear()

        #Make a call that uses `sentence_count`
        textstat.avg_sentence_length(self.long_test)

        #Test that `sentence_count` was called
        self.assertEqual(textstat.sentence_count._cache.misses, 1)

        #Call `avg_sentence_length` again
        textstat.avg_sentence_length(self.long_test)

        #Test that `sentence_count` wasn't called again
        self.assertEqual(textstat.sentence_count._cache.lookups, 1)

    def test_unicode_support(self):
        textstat.text_standard(
            "\u3042\u308a\u304c\u3068\u3046\u3054\u3056\u3044\u307e\u3059")

        textstat.text_standard(u"ありがとうございます")
