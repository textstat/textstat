import string
import re
import math
import operator


class textstatistics:

        def __init__(self):
                return None

        def charcount(self, text, ignore_spaces=True):
                if ignore_spaces:
                        text = text.replace(" ", "")
                return len(text)

        def lexicon_count(self, text, removepunct=True):
                exclude = list(set(string.punctuation))
                if removepunct:
                        text = ''.join(ch for ch in text if ch not in exclude)
                count = len(text.split())
                return count

        def syllable_count(self, text):
                count = 0
                vowels = 'aeiouy'
                text = text.lower().strip(".:;?!)(")
                if text[0] in vowels:
                    count += 1
                for index in range(1, len(text)):
                    if text[index] in vowels and text[index-1] not in vowels:
                        count += 1
                if text.endswith('e'):
                    count -= 1
                if text.endswith('le'):
                    count += 1
                if count == 0:
                    count += 1
                count = count - (0.1*count)
                return (round(count))

        def sentence_count(self, text):
                count = 0
                text = ''.join(text)
                sentences = re.split(r' *[\.\?!][\'"\)\]]* *', text)
                for value in sentences:
                        if self.lexicon_count(value) < 4:
                                count = count + 1

                return len(sentences) - count

        def avg_sentence_length(self, text):
                lc = self.lexicon_count(text)
                sc = self.sentence_count(text)
                ASL = float(lc/sc)
                return round(lc/sc, 1)

        def avg_syllables_per_word(self, text):
                syllable = self.syllable_count(text)
                words = self.lexicon_count(text)
                ASPW = float(syllable)/float(words)
                return round(ASPW, 1)

        def avg_letter_per_word(self, text):
                ALPW = float(float(self.charcount(text))/float(self.lexicon_count(text)))
                return round(ALPW, 2)

        def avg_sentence_per_word(self, text):
                ASPW = float(float(self.sentence_count(text))/float(self.lexicon_count(text)))
                return round(ASPW, 2)

        def flesch_reading_ease(self, text):
                ASL = self.avg_sentence_length(text)
                ASW = self.avg_syllables_per_word(text)

                FRE = 206.835 - float(1.015 * ASL) - float(84.6 * ASW)
                return round(FRE, 2)

        def flesch_kincaid_grade(self, text):
                ASL = self.avg_sentence_length(text)
                ASW = self.avg_syllables_per_word(text)
                FKRA = float(0.39 * ASL) + float(11.8 * ASW) - 15.59
                return round(FKRA, 1)

        def polysyllabcount(self, text):
                count = 0
                for word in text.split():
                        wrds = self.syllable_count(word)
                        if wrds >= 3:
                                count += 1
                return count

        def smog_index(self, text):
                if self.sentence_count(text) >= 3:
                        poly_syllab = self.polysyllabcount(text)
                        # SMOG = 3.129 + round(poly_syllab**.5)
                        SMOG = (1.043 * (30*(poly_syllab/self.sentence_count(text)))**.5) + 3.1291
                        return round(SMOG, 1)

        def coleman_liau_index(self, text):
                L = round(self.avg_letter_per_word(text)*100, 2)
                S = round(self.avg_sentence_per_word(text)*100, 2)

                CLI = float((0.058 * L) - (0.296 * S) - 15.8)

                return round(CLI, 2)

        def automated_readability_index(self, text):
                chrs = self.charcount(text)
                wrds = self.lexicon_count(text)
                snts = self.sentence_count(text)
                a = (float(chrs)/float(wrds))
                b = (float(wrds)/float(snts))
                ARI = (4.71 * round(a, 2)) + (0.5*round(b, 2)) - 21.43
                return round(ARI, 1)

        def linsear_write_formula(self, text):
                easy_word = []
                difficult_word = []
                text_list = text.split()

                for i, value in enumerate(text_list):
                                if i <= 101:
                                        if self.syllable_count(value) < 3:
                                                easy_word.append(value)
                                        elif self.syllable_count(value) > 3:
                                                difficult_word.append(value)
                                        text = ' '.join(text_list[:100])
                                        Number = float((len(easy_word)*1 + len(difficult_word)*3)/self.sentence_count(text))
                                        if Number > 20:
                                                Number /= 2
                                        else:
                                                Number = (Number-2)/2
                return float(Number)

        def difficult_words(self, text):
                text_list = text.split()
                filename = open('textstat/easy_word_list').read().split()
                diff_words = []
                for value in text_list:
                        if value not in filename:
                                if self.syllable_count(value) > 1:
                                        if value not in diff_words:
                                                diff_words.append(value)

                return len(diff_words)

        def dale_chall_readability_score(self, text):

                word_count = self.lexicon_count(text)
                count = word_count - self.difficult_words(text)
                per = float(count)/float(word_count)*100
                difficult_words = 100-per
                if difficult_words > 5:
                        score = (0.1579 * difficult_words) + (0.0496 * self.avg_sentence_length(text)) + 3.6365
                else:
                        score = (0.1579 * difficult_words) + (0.0496 * self.avg_sentence_length(text))
                return round(score, 2)

        def gunning_fog(self, text):
                per_diff_words = (self.difficult_words(text)/self.lexicon_count(text)*100) + 5
                grade = 0.4*(self.avg_sentence_length(text) + per_diff_words)
                return grade

        def text_standard(self, text):
                grade = []
                ################################################ Appending Flesch Kincaid Grade ########################################################################
                lower = round(self.flesch_kincaid_grade(text))
                upper = math.ceil(self.flesch_kincaid_grade(text))
                grade.append(int(lower))
                grade.append(int(upper))
                ################################################ Appending Flesch Reading Easy ########################################################################
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
                ###################################################### Appending SMOG Index ########################################################################
                lower = round(self.smog_index(text))
                upper = math.ceil(self.smog_index(text))
                grade.append(int(lower))
                grade.append(int(upper))
                ################################################ Appending Coleman_Liau_Index ########################################################################
                lower = round(self.coleman_liau_index(text))
                upper = math.ceil(self.coleman_liau_index(text))
                grade.append(int(lower))
                grade.append(int(upper))
                ################################################ Appending Automated_Readability_Index ########################################################################
                lower = round(self.automated_readability_index(text))
                upper = math.ceil(self.automated_readability_index(text))
                grade.append(int(lower))
                grade.append(int(upper))
                ###################################################### Appending Dale_Chall_Readability_Score ########################################################################
                lower = round(self.dale_chall_readability_score(text))
                upper = math.ceil(self.dale_chall_readability_score(text))
                grade.append(int(lower))
                grade.append(int(upper))
                ###################################################### Appending Linsear_Write_Formula ########################################################################
                lower = round(self.linsear_write_formula(text))
                upper = math.ceil(self.linsear_write_formula(text))
                grade.append(int(lower))
                grade.append(int(upper))
                ###################################################### Appending Gunning Fog Index ########################################################################
                lower = round(self.gunning_fog(text))
                upper = math.ceil(self.gunning_fog(text))
                grade.append(int(lower))
                grade.append(int(upper))
                #################################### Finding the Readability Consensus based upon all the above tests #################################################
                d = {x: grade.count(x) for x in grade}
                sorted_x = sorted(d.iteritems(), key=operator.itemgetter(1))
                final_grade = str((sorted_x)[len(sorted_x)-1])
                score = final_grade.split(',')[0].strip('(')
                return str(int(score)-1) + "th " + "and " + str(int(score)) + "th grade"

textstat = textstatistics()
