import string
import re

class textstatistics:

	def __init__(self):
		return None

	def charcount(self, text, ignore_spaces = True):
		if ignore_spaces:
			text = text.replace(" ","")
		return len(text)

	def lexicon_count(self, text, removepunct = True):
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
		for index in range(1,len(text)):
		    if text[index] in vowels and text[index-1] not in vowels:
		        count += 1
		if text.endswith('e'):
		    count -= 1
		if text.endswith('le'):
		    count += 1
		if count == 0:
		    count += 1
		#count = count - (0.1*count)
		return (round(count))

	def sentence_count(self, text):
		count = 0
		text = ''.join(text)
		sentences = re.split(r' *[\.\?!][\'"\)\]]* *', text)
		for value in sentences:
			if self.lexicon_count(value)<4:
				count = count + 1
		return len(sentences) - count

	def avg_sentence_length(self, text):
		lc = self.lexicon_count(text)
		sc = self.sentence_count(text)
		return round(lc/sc,1)

	def avg_syllables_per_word(self, text):
		syllable = self.syllable_count(text)
		words = self.lexicon_count(text)
		ASPW = float(syllable)/float(words)
		return round(ASPW,1)

	def avg_letter_per_word(self,text):
		ALPW = float(float(self.charcount(text))/float(self.lexicon_count(text)))
		return round(ALPW,2)

	def avg_sentence_per_word(self,text):
		ASPW = float(float(self.sentence_count(text))/float(self.lexicon_count(text)))
		return round(ASPW,2)

	def flesch_reading_ease(self, text):
		ASL = self.avg_sentence_length(text)
		ASW = self.avg_syllables_per_word(text)
		FRE = 206.835 - float(1.015 * ASL) - float(84.6 * ASW) 
		return round(FRE,2)

	def flesch_kincaid_grade(self, text):
		ASL = self.avg_sentence_length(text)
		ASW = self.avg_syllables_per_word(text)
		FKRA = float(0.39 * ASL) + float(11.8 * ASW) - 15.59 
		return FKRA

	def polysyllabcount(self, text):
		count = 0
		for word in text.split():
			wrds = self.syllable_count(word)
			if wrds >= 3:
				count += 1
		return count

	def SMOG_Index(self, text):
		poly_syllab = self.polysyllabcount(text)
		SMOG = 3 + poly_syllab**(1/2) 
		return SMOG

	
	def Coleman_Liau_Index(self, text):
		L = round(self.avg_letter_per_word(text)*100)
		S = round(self.avg_sentence_per_word(text)*100)
		CLI = (0.058 * L) - (0.296 * S ) - 15.8
		return round(CLI,2)

	def Automated_Readability_Index(self, text):
		chrs = self.charcount(text)
		wrds = self.lexicon_count(text)
		snts = self.sentence_count(text)
		a = (float(chrs)/float(wrds))
		b = (float(wrds)/float(snts))
		ARI = (4.71 * round(a)) + (0.5*round(b)) - 21.43
		return ARI

	def Linsear_Write_Formula(self, text):
		easy_word = []
		difficult_word = []
		test_data_list = text.split()

		for i,value in enumerate(test_data_list):
				if i <=101:
					if self.syllable_count(value)<3:
						easy_word.append(value)
					elif self.syllable_count(value)>3:
						difficult_word.append(value)
					test = ' '.join(test_data_list[:100])
					Number = (len(easy_word)*1 + len(difficult_word)*3)/self.sentence_count(test)
					if Number >20:
						Number/=2
					else:
						Number = (Number-2)/2
		return Number

	def Dale_Chall_Readability_Score(self, text):
		test_data_list = text.split()
		filename = open('textstat/easy_word_list').read().split()
		diff = []
		count = 0
		for value in test_data_list:
			if value not in filename:
				if self.syllable_count(value)>2:
					count = count + 1
					if value not in diff:
						diff.append(value)
		count =  len(test_data_list) - len(diff)
		words = self.lexicon_count(text)
		per =  float(count)/float(words)*100
		difficult_words =  100-per
		score = (0.1579 * difficult_words) + (0.0496 * self.avg_sentence_length(text)) + 3.6365
		return round(score,2)


textstat = textstatistics()