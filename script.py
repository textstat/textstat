class textstatistics:
	def __init__(self):
		return None

	def charcount(self, text, ignore_spaces = True):
		if ignore_spaces:
			text = text.replace(" ","")
		return len(text)

	def lexicon():
		return None

            def demo():
return None


if __name__ == '__main__':
	TS = textstatistics()
	print TS.charcount("hello how are you buddy", True)

