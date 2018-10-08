# -*- coding: utf-8 -*-


from __future__ import print_function
from __future__ import division

import string
import re
import math
import operator
from collections import Counter

import pkg_resources
import repoze.lru
from pyphen import Pyphen

exclude = list(string.punctuation)

easy_word_set = set([
    ln.decode('utf-8').strip() for ln in
    pkg_resources.resource_stream('textstat', 'easy_words.txt')
])


def legacy_round(number, points=0):
    p = 10 ** points
    return float(math.floor((number * p) + math.copysign(0.5, number))) / p


class textstatistics:

    @repoze.lru.lru_cache(maxsize=128)
    def char_count(self, text, ignore_spaces=True):
        """
        Function to return total character counts in a text,
        pass the following parameter `ignore_spaces = False`
        to ignore whitespaces
        """
        if ignore_spaces:
            text = text.replace(" ", "")
        return len(text)

    @repoze.lru.lru_cache(maxsize=128)
    def lexicon_count(self, text, removepunct=True):
        """
        Function to return total lexicon (words in lay terms) counts in a text
        """
        if removepunct:
            text = ''.join(ch for ch in text if ch not in exclude)
        count = len(text.split())
        return count

    @repoze.lru.lru_cache(maxsize=128)
    def syllable_count(self, text, lang='en_US'):
        """
        Function to calculate syllable words in a text.
        I/P - a text
        O/P - number of syllable words
        """
        text = text.lower()
        text = "".join(x for x in text if x not in exclude)

        if not text:
            return 0

        dic = Pyphen(lang=lang)
        count = 0
        for word in text.split(' '):
            word_hyphenated = dic.inserted(word)
            count += max(1, word_hyphenated.count("-") + 1)
        return count

    @repoze.lru.lru_cache(maxsize=128)
    def sentence_count(self, text):
        """
        Sentence count of a text
        """
        ignore_count = 0
        sentences = re.split(r' *[\.\?!][\'"\)\]]*[ |\n](?=[A-Z])', text)
        for sentence in sentences:
            if self.lexicon_count(sentence) <= 2:
                ignore_count += 1
        return max(1, len(sentences) - ignore_count)

    @repoze.lru.lru_cache(maxsize=128)
    def avg_sentence_length(self, text):
        try:
            asl = float(self.lexicon_count(text) / self.sentence_count(text))
            return legacy_round(asl, 1)
        except ZeroDivisionError:
            return 0.0

    @repoze.lru.lru_cache(maxsize=128)
    def avg_syllables_per_word(self, text):
        syllable = self.syllable_count(text)
        words = self.lexicon_count(text)
        try:
            syllables_per_word = float(syllable) / float(words)
            return legacy_round(syllables_per_word, 1)
        except ZeroDivisionError:
            return 0.0

    @repoze.lru.lru_cache(maxsize=128)
    def avg_letter_per_word(self, text):
        try:
            letters_per_word = float(
                self.char_count(text) / self.lexicon_count(text))
            return legacy_round(letters_per_word, 2)
        except ZeroDivisionError:
            return 0.0

    @repoze.lru.lru_cache(maxsize=128)
    def avg_sentence_per_word(self, text):
        try:
            sentence_per_word = float(
                self.sentence_count(text) / self.lexicon_count(text))
            return legacy_round(sentence_per_word, 2)
        except ZeroDivisionError:
            return 0.0

    @repoze.lru.lru_cache(maxsize=128)
    def flesch_reading_ease(self, text):
        sentence_length = self.avg_sentence_length(text)
        syllables_per_word = self.avg_syllables_per_word(text)
        flesch = (
            206.835
            - float(1.015 * sentence_length)
            - float(84.6 * syllables_per_word)
        )
        return legacy_round(flesch, 2)

    @repoze.lru.lru_cache(maxsize=128)
    def flesch_kincaid_grade(self, text):
        sentence_lenth = self.avg_sentence_length(text)
        syllables_per_word = self.avg_syllables_per_word(text)
        flesch = (
            float(0.39 * sentence_lenth)
            + float(11.8 * syllables_per_word)
            - 15.59)
        return legacy_round(flesch, 1)

    @repoze.lru.lru_cache(maxsize=128)
    def polysyllabcount(self, text):
        count = 0
        for word in text.split():
            wrds = self.syllable_count(word)
            if wrds >= 3:
                count += 1
        return count

    @repoze.lru.lru_cache(maxsize=128)
    def smog_index(self, text):
        sentences = self.sentence_count(text)

        if sentences >= 3:
            try:
                poly_syllab = self.polysyllabcount(text)
                smog = (
                    (1.043 * (30 * (poly_syllab / sentences)) ** .5)
                    + 3.1291)
                return legacy_round(smog, 1)
            except ZeroDivisionError:
                return 0.0
        else:
            return 0.0

    @repoze.lru.lru_cache(maxsize=128)
    def coleman_liau_index(self, text):
        letters = legacy_round(self.avg_letter_per_word(text)*100, 2)
        sentences = legacy_round(self.avg_sentence_per_word(text)*100, 2)
        coleman = float((0.058 * letters) - (0.296 * sentences) - 15.8)
        return legacy_round(coleman, 2)

    @repoze.lru.lru_cache(maxsize=128)
    def automated_readability_index(self, text):
        chrs = self.char_count(text)
        words = self.lexicon_count(text)
        sentences = self.sentence_count(text)
        try:
            a = float(chrs)/float(words)
            b = float(words) / float(sentences)
            readability = (
                (4.71 * legacy_round(a, 2))
                + (0.5 * legacy_round(b, 2))
                - 21.43)
            return legacy_round(readability, 1)
        except ZeroDivisionError:
            return 0.0

    @repoze.lru.lru_cache(maxsize=128)
    def linsear_write_formula(self, text):
        easy_word = 0
        difficult_word = 0
        text_list = text.split()[:100]

        for word in text_list:
            if self.syllable_count(word) < 3:
                easy_word += 1
            else:
                difficult_word += 1

        text = ' '.join(text_list)

        number = float(
            (easy_word * 1 + difficult_word * 3)
            / self.sentence_count(text))

        if number <= 20:
            number -= 2

        return number / 2

    @repoze.lru.lru_cache(maxsize=128)
    def difficult_words(self, text):
        text_list = re.findall(r"[\w\='‘’]+", text.lower())
        diff_words_set = set()
        for value in text_list:
            if value not in easy_word_set:
                if self.syllable_count(value) > 1:
                    diff_words_set.add(value)
        return len(diff_words_set)

    @repoze.lru.lru_cache(maxsize=128)
    def dale_chall_readability_score(self, text):
        word_count = self.lexicon_count(text)
        count = word_count - self.difficult_words(text)

        try:
            per = float(count) / float(word_count) * 100
        except ZeroDivisionError:
            return 0.0

        difficult_words = 100 - per

        score = (
            (0.1579 * difficult_words)
            + (0.0496 * self.avg_sentence_length(text)))

        if difficult_words > 5:
            score += 3.6365
        return legacy_round(score, 2)

    @repoze.lru.lru_cache(maxsize=128)
    def gunning_fog(self, text):
        try:
            per_diff_words = (
                (self.difficult_words(text) / self.lexicon_count(text) * 100)
                + 5)

            grade = 0.4 * (self.avg_sentence_length(text) + per_diff_words)
            return legacy_round(grade, 2)
        except ZeroDivisionError:
            return 0.0

    @repoze.lru.lru_cache(maxsize=128)
    def lix(self, text):
        words = text.split()

        words_len = len(words)
        long_words = len([wrd for wrd in words if len(wrd) > 6])

        per_long_words = (float(long_words) * 100) / words_len
        asl = self.avg_sentence_length(text)
        lix = asl + per_long_words

        return legacy_round(lix, 2)

    @repoze.lru.lru_cache(maxsize=128)
    def text_standard(self, text, float_output=None):

        grade = []

        # Appending Flesch Kincaid Grade
        lower = legacy_round(self.flesch_kincaid_grade(text))
        upper = math.ceil(self.flesch_kincaid_grade(text))
        grade.append(int(lower))
        grade.append(int(upper))

        # Appending Flesch Reading Easy
        score = self.flesch_reading_ease(text)
        if score < 100 and score >= 90:
            grade.append(5)
        elif score < 90 and score >= 80:
            grade.append(6)
        elif score < 80 and score >= 70:
            grade.append(7)
        elif score < 70 and score >= 60:
            grade.append(8)
            grade.append(9)
        elif score < 60 and score >= 50:
            grade.append(10)
        elif score < 50 and score >= 40:
            grade.append(11)
        elif score < 40 and score >= 30:
            grade.append(12)
        else:
            grade.append(13)

        # Appending SMOG Index
        lower = legacy_round(self.smog_index(text))
        upper = math.ceil(self.smog_index(text))
        grade.append(int(lower))
        grade.append(int(upper))

        # Appending Coleman_Liau_Index
        lower = legacy_round(self.coleman_liau_index(text))
        upper = math.ceil(self.coleman_liau_index(text))
        grade.append(int(lower))
        grade.append(int(upper))

        # Appending Automated_Readability_Index
        lower = legacy_round(self.automated_readability_index(text))
        upper = math.ceil(self.automated_readability_index(text))
        grade.append(int(lower))
        grade.append(int(upper))

        # Appending Dale_Chall_Readability_Score
        lower = legacy_round(self.dale_chall_readability_score(text))
        upper = math.ceil(self.dale_chall_readability_score(text))
        grade.append(int(lower))
        grade.append(int(upper))

        # Appending Linsear_Write_Formula
        lower = legacy_round(self.linsear_write_formula(text))
        upper = math.ceil(self.linsear_write_formula(text))
        grade.append(int(lower))
        grade.append(int(upper))

        # Appending Gunning Fog Index
        lower = legacy_round(self.gunning_fog(text))
        upper = math.ceil(self.gunning_fog(text))
        grade.append(int(lower))
        grade.append(int(upper))

        # Finding the Readability Consensus based upon all the above tests
        d = Counter(grade)
        final_grade = d.most_common(1)
        score = final_grade[0][0]
        
        if float_output:
            return float(score)
        else:
            return "{}th and {}th grade".format(
                str(int(score)-1), str(int(score))
            )


textstat = textstatistics()
