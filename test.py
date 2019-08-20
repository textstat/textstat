"""Test suite for textstat
"""

import textstat

short_test = "Cool dogs wear da sunglasses."

long_test = (
    "Playing ... games has always been thought to be "
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
    "lives"
)

easy_text = (
    "Anna and her family love doing puzzles. Anna is best at "
    "little puzzles. Anna and her brother work on medium size "
    "puzzles together. Anna's Brother likes puzzles with cars "
    "in them. When the whole family does a puzzle, they do really "
    "big puzzles. It can take them a week to finish a really "
    "big puzzle. Last year they did a puzzle with 500 pieces! "
    "Anna tries to finish one small puzzle a day by her. "
    "Her puzzles have about 50 pieces. They all glue their "
    "favorite puzzles together and frame them. The puzzles look "
    "so nice on the wall."
)


def test_char_count():
    textstat.set_lang("en_US")
    count = textstat.char_count(long_test)
    count_spaces = textstat.char_count(
        long_test, ignore_spaces=False
    )

    assert count == 1750
    assert count_spaces == 2123


def test_letter_count():
    textstat.set_lang("en_US")
    count = textstat.letter_count(long_test)
    count_spaces = textstat.letter_count(
        long_test, ignore_spaces=False
    )

    assert count == 1688
    assert count_spaces == 2061


def test_lexicon_count():
    textstat.set_lang("en_US")
    count = textstat.lexicon_count(long_test)
    count_punc = textstat.lexicon_count(long_test, removepunct=False)

    assert count == 372
    assert count_punc == 376


def test_syllable_count():
    textstat.set_lang("en_US")
    count = textstat.syllable_count(long_test)

    assert count == 521


def test_sentence_count():
    textstat.set_lang("en_US")
    count = textstat.sentence_count(long_test)

    assert count == 16


def test_avg_sentence_length():
    textstat.set_lang("en_US")
    avg = textstat.avg_sentence_length(long_test)

    assert avg == 23.3


def test_avg_syllables_per_word():
    textstat.set_lang("en_US")
    avg = textstat.avg_syllables_per_word(long_test)

    assert avg == 1.4


def test_avg_letter_per_word():
    textstat.set_lang("en_US")
    avg = textstat.avg_letter_per_word(long_test)

    assert avg == 4.54


def test_avg_sentence_per_word():
    textstat.set_lang("en_US")
    avg = textstat.avg_sentence_per_word(long_test)

    assert avg == 0.04


def test_flesch_reading_ease():
    textstat.set_lang("en_US")
    score = textstat.flesch_reading_ease(long_test)

    assert score == 64.75

    textstat.set_lang("de_DE")
    score = textstat.flesch_reading_ease(long_test)

    assert score == 63.1

    textstat.set_lang("es_ES")
    score = textstat.flesch_reading_ease(long_test)

    assert score == 84.37

    textstat.set_lang("fr_FR")
    score = textstat.flesch_reading_ease(long_test)

    assert score == 80.31

    textstat.set_lang("it_IT")
    score = textstat.flesch_reading_ease(long_test)

    assert score == 89.27

    textstat.set_lang("nl_NL")
    score = textstat.flesch_reading_ease(long_test)

    assert score == 61.97

    textstat.set_lang("ru_RU")
    score = textstat.flesch_reading_ease(long_test)

    assert score == 116.45


def test_flesch_kincaid_grade():
    textstat.set_lang("en_US")
    score = textstat.flesch_kincaid_grade(long_test)

    assert score == 10.0


def test_polysyllabcount():
    textstat.set_lang("en_US")
    count = textstat.polysyllabcount(long_test)

    assert count == 32


def test_smog_index():
    textstat.set_lang("en_US")
    index = textstat.smog_index(long_test)

    assert index == 11.2


def test_coleman_liau_index():
    textstat.set_lang("en_US")
    index = textstat.coleman_liau_index(long_test)

    assert index == 9.35


def test_automated_readability_index():
    textstat.set_lang("en_US")
    index = textstat.automated_readability_index(long_test)

    assert index == 12.3


def test_linsear_write_formula():
    textstat.set_lang("en_US")
    result = textstat.linsear_write_formula(long_test)

    assert result == 14.5


def test_difficult_words():
    textstat.set_lang("en_US")
    result = textstat.difficult_words(long_test)

    assert result == 49


def test_difficult_words_list():
    textstat.set_lang("en_US")
    result = textstat.difficult_words_list(short_test)

    assert result == ["sunglasses"]


def test_dale_chall_readability_score():
    textstat.set_lang("en_US")
    score = textstat.dale_chall_readability_score(long_test)

    assert score == 6.87


def test_gunning_fog():
    textstat.set_lang("en_US")
    score = textstat.gunning_fog(long_test)

    assert score == 11.26

    # FOG-PL
    textstat.set_lang("pl_PL")
    score_pl = textstat.gunning_fog(long_test)

    assert score_pl == 10.40


def test_lix():
    textstat.set_lang("en_US")
    score = textstat.lix(long_test)

    assert score == 45.11


def test_rix():
    textstat.set_lang("en_US")
    score = textstat.rix(long_test)

    assert score == 5.13


def test_text_standard():
    textstat.set_lang("en_US")
    standard = textstat.text_standard(long_test)

    assert standard == "9th and 10th grade"

    standard = textstat.text_standard(short_test)

    assert standard == "2nd and 3rd grade"


def test_reading_time():
    textstat.set_lang("en_US")
    score = textstat.reading_time(long_test)

    assert score == 25.68


def test_lru_caching():
    textstat.set_lang("en_US")
    # Clear any cache
    textstat.sentence_count.cache_clear()
    textstat.avg_sentence_length.cache_clear()

    # Make a call that uses `sentence_count`
    textstat.avg_sentence_length(long_test)

    # Test that `sentence_count` was called
    assert textstat.sentence_count.cache_info().misses == 1

    # Call `avg_sentence_length` again
    textstat.avg_sentence_length(long_test)

    # Test that `sentence_count` wasn't called again
    assert textstat.sentence_count.cache_info().hits == 1


def test_unicode_support():
    textstat.set_lang("en_US")
    textstat.text_standard(
        "\u3042\u308a\u304c\u3068\u3046\u3054\u3056\u3044\u307e\u3059")

    textstat.text_standard("ありがとうございます")


def test_spache_readability():
    textstat.set_lang("en_US")
    spache = textstat.spache_readability(easy_text, False)

    assert spache == 2


def test_dale_chall_readability_score_v2():
    textstat.set_lang("en_US")
    score = textstat.dale_chall_readability_score_v2(long_test)

    assert score == 6.87


def test_default_lang_configs():
    # Config from default en_US should be used
    textstat.set_lang("en_GB")
    score = textstat.flesch_reading_ease(long_test)

    assert score == 64.75
