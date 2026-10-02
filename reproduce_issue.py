import textstat

empty_samples = ["", "   ", "\t\n"]

for sample in empty_samples:
    print(f"--- Testing input: {repr(sample)} ---")
    
    try:
        score = textstat.flesch_reading_ease(sample)
        print(f"  Flesch Reading Ease: {score}")
    except Exception as e:
        print(f"  FAILED Flesch Reading Ease -> {type(e).__name__}: {e}")

    try:
        syllables = textstat.syllable_count(sample)
        print(f"  Syllable Count: {syllables}")
    except Exception as e:
        print(f"  FAILED Syllable Count -> {type(e).__name__}: {e}")
