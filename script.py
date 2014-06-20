import string

class textstatistics:
	''' Constructor to set object parameters. '''
	def __init__(self):
		return None

	''' Character Count Function '''
	def charcount(self, text, ignore_spaces = True):
		if ignore_spaces:
			text = text.replace(" ","")
		return len(text)

	''' # Consider alnums/digits etc'''
	def lexicon_count(self, text, removepunct = True):
		exclude = list(set(string.punctuation))
		if removepunct:
			text = ''.join(ch for ch in text if ch not in exclude)
		count = len(text.split())
		return count

	''' '''
	def syllable_count(self, text):
		vowels = 'aeiouy'
		text = text.lower().strip(".:;?!)(")
		if text[0] in vowels:
		    count +=1
		for index in range(1,len(text)):
		    if text[index] in vowels and text[index-1] not in vowels:
		        count +=1
		if text.endswith('e'):
		    count -= 1
		if text.endswith('le'):
		    count+=1
		if count == 0:
		    count +=1
		count = count - (0.1*count)
		return (round(count))

	# Impleemet sentence count
	def avg_sentence_length(self, text):
		lc = lexicon_count(text)
		sc = sentence_count(text)
		return float(lc/sc)

	# implement ASW Function
	def Flesch_Reading_Ease(self, text):
		ASL = avg_sentence_length(text)
		ASW = avg_syllables_per_word(text)
		RE = 206.835 - float(1.015 * ASL) - float(84.6 * ASW) 
		return RE

	def Flesch_Kincaid_Grade():
		return None

	def Fog_Scale():
		return None

	def SMOG_Index():
		return None

	def Coleman_Liau_Index():
		return None

	def Automated_Readability_Index():
		return None

	def Linsear_Write_Formula():
		return None

	def Syllable_Count():
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
	
	print TS.charcount(test_data)
	print TS.syllable_count(test_data)
	print TS.lexicon_count(test_data)



