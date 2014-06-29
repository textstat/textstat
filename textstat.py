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
		ALPW = float(float(self.charcount(test_data))/float(self.lexicon_count(test_data)))
		return round(ALPW,2)

	def avg_sentence_per_word(self,text):
		ASPW = float(float(self.sentence_count(test_data))/float(self.lexicon_count(test_data)))
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
		for word in test_data.split():
			wrds = TS.syllable_count(word)
			if wrds >= 3:
				count += 1
		return count

	def SMOG_Index(self, text):
		poly_syllab = self.polysyllabcount(text)
		SMOG = 3 + poly_syllab**(1/2) 
		return SMOG

	
	def Coleman_Liau_Index(self, text):
		L = round(self.avg_letter_per_word(test_data)*100)
		S = round(self.avg_sentence_per_word(test_data)*100)
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
		test_data_list = test_data.split()
		filename = open('/home/workstation/Project/Data/easy_word_list').read().split()
		diff = []
		count = 0
		for value in test_data_list:
			if value not in filename:
				if self.syllable_count(value)>2:
					count = count + 1
					if value not in diff:
						diff.append(value)
		count =  len(test_data_list) - len(diff)
		words = self.lexicon_count(test_data)
		per =  float(count)/float(words)*100
		difficult_words =  100-per
		score = (0.1579 * difficult_words) + (0.0496 * self.avg_sentence_length(test_data)) + 3.6365
		return round(score,2)


textstat = textstatistics()



# if __name__ == '__main__':

# 	test_data = """Far up in the mountains of Canada, there is an old abandoned log cabin. Once it was occupied by a young couple who wanted to distance themselves from the chaos of this modern world. Here they were miles away from the nearest town. Bob, the husband, made the occasional trip into town to buy supplies whereas Jan, his wife, spent her free time by the fire, sewing. Their life was simply idyllic.

# Then, one midwinter's day, Jan woke up from bed with a strange ache in her bones. Putting it down to overwork, Bob shooed her to bed and made sure she rested. Though Jan was impatient to get to her chores, Bob soothed her, "Relax, Sugar. You're overdoing things. All these chores will be here when you recover."

# However, Jan seemed to be getting worse instead of recovering. By evening, she was running a high fever and in greater pain. In spite of his best efforts, Bob could not manage to ease her suffering. And then suddenly, she started to lapse into unconsciousness.

# It was then obvious that she was seriously ill. What could Bob do? He had no experience in treating the sick and Jan was getting worse by the minute. He knew that there was an old doctor in town but he lived three miles away, downhill. Pot-bellied and obese, there was no way the doctor could make it up to their cabin.

# Something had to be done quickly! Bob racked his brains but to no avail. The only thing left to do was to go to the doctor. In Jan's condition, she could never walk that far in the waist-deep snow. Bob would have to carry her!

# Bob searched his mind for a way to move poor, sick Jan. Then, he remembered. He had once made a sledge so that they could ride together over the mountain. They never got around to using it though, because the whole mountain was thickly covered with rocks and trees. He had never found a safe way down, not even once.

# "Well," he thought, "looks like I'm going to have to try it anyhow," as he dug out the sledge from the storeroom. "Jan may die unless I get her to the doctor, and life means nothing to me without her." With this thought in mind, Bob gently tucked Jan into the sledge, got in the front, and with a short prayer for safety, pushed off.

# How they got through that ride alive, Bob has never figured out. As trees loomed up in front of him and just as quickly whizzed by his side, close enough to touch, he felt relieved that Jan was not awake to experience the ride. It was all he could do not to scream as collision seemed imminent, time and again, with only inches to spare.

# At last, bursting from the mountainside, the town came into view. Barely slowing down, they sped through the icy streets, only losing speed as they neared the doctor's house. The sledge, battered through the journey, collapsed in the left ski as it came to a halt, spilling out its occupants. Bob picked up his Jan and made his way into the doctor's house.

# After what seemed to be a long winter, Jan recovered fully from her illness but Bob never recovered from his fright. They moved into the little town so as to be near help in times of crisis, and have lived there ever since"""


	

# 	textstat = textstatistics()
# 	print textstat.lexicon_count(test_data)
# 	print textstat.charcount(test_data)
# 	print textstat.syllable_count("Twenty Ninth 29th")
# 	print textstat.sentence_count(test_data)
# 	print textstat.flesch_reading_ease(test_data)
# 	print textstat.SMOG_Index(test_data)
# 	print textstat.flesch_kincaid_grade(test_data)	
# 	print textstat.avg_letter_per_word(test_data)
# 	print textstat.Coleman_Liau_Index(test_data)
# 	print textstat.avg_syllables_per_word(test_data)
# 	print textstat.Automated_Readability_Index(test_data)
# 	print textstat.Dale_Chall_Readability_Score(test_data)