textstat
========

Calculate statistics from text


Features
--------

1. Syllable Count
2. Lexicon Count
3. Sentence Count
4. The Flesch Reading Ease formula
5. The Flesch-Kincaid Grade Level
6. The Fog Scale (Gunning FOG Formula)
7. The SMOG Index
8. Automated Readability Index
9. The Coleman-Liau Index
10. Linsear Write Formula
11. Dale-Chall Readability Score
12. Readability Consensus based upon all the above tests

Installation
----------

	pip install textstat

Usage
----------
	
	from textstat.textstat import textstat
	if __name__ == '__main__':
		test_data = """Playing games has always been thought to be important to the development of well-balanced and creative children; however, what part, if any, they should play in the lives of adults has never been researched that deeply. I believe that playing games is every bit as important for adults as for children. Not only is taking time out to play games with our children and other adults valuable to building interpersonal relationships but is also a wonderful way to release built up tension."""

	print textstat.syllable_count(test_data) #demo function


the arguement (text) for all the functions defined remains same - 
i.e the text for which statistics needs to be calculated

#List of Functions

## Syllable Count

function name - syllable_count(text)

returns - the number of syllables present in the given text.

## Lexicon Count

function name - lexicon_count(text, TRUE/FALSE)

Calculates the number of words present in the text.
TRUE/FALSE specifies whether we need to take in account in punctuation symbols while counting lexicons or not.
Default value is TRUE, which removes the punctuation before counting lexicons.

## Sentence Count

function name - sentence_count(text)

returns the number of sentences present in the given text.


## The Flesch Reading Ease formula

function name - flesch_reading_ease(text)

returns the Flesch Reading Ease Score. Following table is helpful to access the ease of readability in a document.

* 90-100 : Very Easy 
* 80-89 : Easy 
* 70-79 : Fairly Easy 
* 60-69 : Standard 
* 50-59 : Fairly Difficult 
* 30-49 : Difficult 
* 0-29 : Very Confusing

## The The Flesch-Kincaid Grade Level

function name - flesch_kincaid_grade(text)

returns the grade score using the Flesch-Kincaid Grade Formula. For example a score of 9.3 means that a ninth grader would be able to read the document.

## The Fog Scale (Gunning FOG Formula)
function name - gunning_fog(text)
returns the FOG index of the given text.

## The SMOG Index
function name - smog_index(text)

return the SMOG index of the given text.

## Automated Readability Index
function name - automated_readability_index(text)

returns the ARI(Automated Readability Index) which outputs a number that approximates the grade level needed to comprehend the text.
For example if the ARI is 6.5, then the grade level to comprehend the text is 6th to 7th grade.

## The Coleman-Liau Index
function name - coleman_liau_index(text)

returns the grade level of the text using the Coleman-Liau Formula

## Linsear Write Formula
function name - linsear_write_formula(text)

returns the grade level using the Lisear Write Formula

## Dale-Chall Readability Score
function name - dale_chall_readability_score(text)

Different from other tests, since it uses a lookup table of most commonly used 3000 english words.
Thus it returns the grade level using the New Dale-Chall Formula. Following table is helpful to access the ease of readability in a document based upon this score. 

ADJUSTED SCORE	GRADE LEVEL
4.9 and Below	Grade 4 and Below
5.0 to 5.9	Grades 5 - 6
6.0 to 6.9	Grades 7 - 8
7.0 to 7.9	Grades 9 - 10
8.0 to 8.9	Grades 11 - 12
9.0 to 9.9	Grades 13 - 15 (College)
10 and Above	Grades 16 and Above (College Graduate)

## Readability Consensus based upon all the above tests
function name - readability_consensus(text)
Based upon all the above tests returns the best grade level under which the given text belongs to.











