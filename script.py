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
		count = count - (0.1*count)
		return (round(count))

	def sentence_count(self, text):
		text = ''.join(text)
		sentences = re.split(r' *[\.\?!][\'"\)\]]* *', text)
		return len(sentences)

	def avg_sentence_length(self, text):
		lc = self.lexicon_count(text)
		sc = self.sentence_count(text)
		return float(lc/sc)

	def avg_syllables_per_word(self, text):
		sum_syll = 0
		lc = self.lexicon_count(text)
		for word in test_data.split():
			wrds = TS.syllable_count(word)
			sum_syll += wrds
		ASPW = float(sum_syll)/lc 
		return ASPW

	def flesch_reading_ease(self, text):
		ASL = self.avg_sentence_length(text)
		ASW = self.avg_syllables_per_word(text)
		FRE = 206.835 - float(1.015 * ASL) - float(84.6 * ASW) 
		return FRE

	def flesch_kincaid_grade(self, text):
		ASL = self.avg_sentence_length(text)
		ASW = self.avg_syllables_per_word(text)
		FKRA = float(0.39 * ASL) + float(11.8 * ASW) - 15.59 
		return FKRA

	def fog_scale(self, text):
		ASL = self.avg_sentence_length(text)
		PHW = ''' CALCULATE THIS %age of hard words'''
		GL = 0.4 * (ASL + PHW) 
		return None

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

	## Incomplete
	def Coleman_Liau_Index(self, text):
		CLI = 0.058 * L - 0.296 * S - 15.8
		return CLI

	def Automated_Readability_Index(self, text):
		chrs = self.charcount(text)
		wrds = self.lexicon_count(text)
		snts = self.sentence_count(text)
		ARI = 4.71 * ( float(chrs)/wds ) + 0.5 * ( float(wds)/snts ) - 21.43
		return ARI

	def Linsear_Write_Formula():
		return None

	def Gunning_Fog_Score():
		return None

	def Dale_Chall_Readability_Score():
		return None

	def Spache_Readability_Score():
		return None




if __name__ == '__main__':

	test_data = """Far up in the mountains of Canada, there is an old abandoned log cabin. Once it was occupied by a young couple who wanted to distance themselves from the chaos of this modern world. Here they were miles away from the nearest town. Bob, the husband, made the occasional trip into town to buy supplies whereas Jan, his wife, spent her free time by the fire, sewing. Their life was simply idyllic.
Then, one midwinter's day, Jan woke up from bed with a strange ache in her bones. Putting it down to overwork, Bob shooed her to bed and made sure she rested. Though Jan was impatient to get to her chores, Bob soothed her, "Relax, Sugar. You're overdoing things. All these chores will be here when you recover."

However, Jan seemed to be getting worse instead of recovering. By evening, she was running a high fever and in greater pain. In spite of his best efforts, Bob could not manage to ease her suffering. And then suddenly, she started to lapse into unconsciousness.

It was then obvious that she was seriously ill. What could Bob do? He had no experience in treating the sick and Jan was getting worse by the minute. He knew that there was an old doctor in town but he lived three miles away, downhill. Pot-bellied and obese, there was no way the doctor could make it up to their cabin.

Something had to be done quickly! Bob racked his brains but to no avail. The only thing left to do was to go to the doctor. In Jan's condition, she could never walk that far in the waist-deep snow. Bob would have to carry her!

Bob searched his mind for a way to move poor, sick Jan. Then, he remembered. He had once made a sledge so that they could ride together over the mountain. They never got around to using it though, because the whole mountain was thickly covered with rocks and trees. He had never found a safe way down, not even once.

"Well," he thought, "looks like I'm going to have to try it anyhow," as he dug out the sledge from the storeroom. "Jan may die unless I get her to the doctor, and life means nothing to me without her." With this thought in mind, Bob gently tucked Jan into the sledge, got in the front, and with a short prayer for safety, pushed off.

How they got through that ride alive, Bob has never figured out. As trees loomed up in front of him and just as quickly whizzed by his side, close enough to touch, he felt relieved that Jan was not awake to experience the ride. It was all he could do not to scream as collision seemed imminent, time and again, with only inches to spare.

At last, bursting from the mountainside, the town came into view. Barely slowing down, they sped through the icy streets, only losing speed as they neared the doctor's house. The sledge, battered through the journey, collapsed in the left ski as it came to a halt, spilling out its occupants. Bob picked up his Jan and made his way into the doctor's house.

After what seemed to be a long winter, Jan recovered fully from her illness but Bob never recovered from his fright. They moved into the little town so as to be near help in times of crisis, and have lived there ever since"""
	
	

	TS = textstatistics()
	
	#print TS.charcount(test_data)
	#print TS.syllable_count(test_data)
	#lc = TS.lexicon_count(test_data)

	#print TS.flesch_reading_ease(test_data)
	print TS.SMOG_Index(test_data)
	#print TS.flesch_kincaid_grade(test_data)	




