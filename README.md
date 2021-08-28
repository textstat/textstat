# Textstat

[![PyPI](https://img.shields.io/pypi/v/textstat.svg)](https://pypi.org/project/textstat/)
[![Build Status](https://github.com/shivam5992/textstat/actions/workflows/test.yml/badge.svg?branch=master)](https://github.com/shivam5992/textstat/actions/workflows/test.yml)
[![Downloads](https://img.shields.io/badge/dynamic/json.svg?url=https://pypistats.org/api/packages/textstat/recent?mirrors=false&label=downloads&query=$.data.last_month&suffix=/month)](https://pypistats.org/packages/textstat)

**Textstat is an easy to use library to calculate statistics from text. It helps determine readability, complexity, and grade level.**

<p align="center">
  <img width="100%" src="https://images.unsplash.com/photo-1457369804613-52c61a468e7d?ixlib=rb-1.2.1&auto=format&fit=crop&w=1350&h=400&q=80">
</p>
<p align="right">
  <sup>Photo by <a href="https://unsplash.com/@impatrickt">Patrick Tomasso</a>
  on <a href="https://unsplash.com/images/things/book">Unsplash</a></sup>
</p>

## Usage

```python
>>> import textstat

>>> test_data = (
    "Playing games has always been thought to be important to "
    "the development of well-balanced and creative children; "
    "however, what part, if any, they should play in the lives "
    "of adults has never been researched that deeply. I believe "
    "that playing games is every bit as important for adults "
    "as for children. Not only is taking time out to play games "
    "with our children and other adults valuable to building "
    "interpersonal relationships but is also a wonderful way "
    "to release built up tension."
)

>>> textstat.flesch_reading_ease(test_data)
>>> textstat.flesch_kincaid_grade(test_data)
>>> textstat.smog_index(test_data)
>>> textstat.coleman_liau_index(test_data)
>>> textstat.automated_readability_index(test_data)
>>> textstat.dale_chall_readability_score(test_data)
>>> textstat.difficult_words(test_data)
>>> textstat.linsear_write_formula(test_data)
>>> textstat.gunning_fog(test_data)
>>> textstat.text_standard(test_data)
>>> textstat.fernandez_huerta(test_data)
>>> textstat.szigriszt_pazos(test_data)
>>> textstat.gutierrez_polini(test_data)
>>> textstat.crawford(test_data)
>>> textstat.gulpease_index(test_data)
>>> textstat.osman(test_data)
```

The argument (text) for all the defined functions remains the same -
i.e the text for which statistics need to be calculated.

## Install

You can install textstat either via the Python Package Index (PyPI) or from source.

### Install using pip

```shell
pip install textstat
```

### Install using easy_install

```shell
easy_install textstat
```

### Install latest version from GitHub

```shell
git clone https://github.com/shivam5992/textstat.git
cd textstat
pip install .
```

### Install from PyPI

Download the latest version of textstat from http://pypi.python.org/pypi/textstat/

You can install it by doing the following:

```shell
tar xfz textstat-*.tar.gz
cd textstat-*/
python setup.py build
python setup.py install # as root
```

## Language support
By default functions implement algorithms for english language. 
To change language, use:

```python
textstat.set_lang(lang)
``` 

The language will be used for syllable calculation and to choose 
variant of the formula.

### Language variants
All functions implement `en_US` language. Some of them has also variants 
for other languages listed below. 

|  Function                   | en | de | es | fr | it | nl | pl | ru |
|-----------------------------|----|----|----|----|----|----|----|----|
| flesch_reading_ease         | ✔  | ✔  | ✔  | ✔  | ✔  | ✔  |    | ✔  |
| gunning_fog                 | ✔  |    |    |    |    |    | ✔  |    |

#### Spanish-specific tests
The following functions are specifically designed for spanish language.
They can be used on non-spanish texts, even though that use case is not recommended.

```python
>>> textstat.fernandez_huerta(test_data)
>>> textstat.szigriszt_pazos(test_data)
>>> textstat.gutierrez_polini(test_data)
>>> textstat.crawford(test_data)
```

Additional information on the formula they implement can be found in their respective docstrings.

## List of Functions

### Formulas

#### The Flesch Reading Ease formula

```python
textstat.flesch_reading_ease(text)
```

Returns the Flesch Reading Ease Score.

The following table can be helpful to assess the ease of
readability in a document.

The table is an _example_ of values. While the
maximum score is 121.22, there is no limit on how low
the score can be. A negative score is valid.

| Score |    Difficulty     |
|-------|-------------------|
|90-100 | Very Easy         |
| 80-89 | Easy              |
| 70-79 | Fairly Easy       |
| 60-69 | Standard          |
| 50-59 | Fairly Difficult  |
| 30-49 | Difficult         |
| 0-29  | Very Confusing    |

> Further reading on
[Wikipedia](https://en.wikipedia.org/wiki/Flesch%E2%80%93Kincaid_readability_tests#Flesch_reading_ease)

#### The Flesch-Kincaid Grade Level

```python
textstat.flesch_kincaid_grade(text)
```

Returns the Flesch-Kincaid Grade of the given text. This is a grade
formula in that a score of 9.3 means that a ninth grader would be able to
read the document.

> Further reading on
[Wikipedia](https://en.wikipedia.org/wiki/Flesch%E2%80%93Kincaid_readability_tests#Flesch%E2%80%93Kincaid_grade_level)

#### The Fog Scale (Gunning FOG Formula)

```python
textstat.gunning_fog(text)
```

Returns the FOG index of the given text. This is a grade formula in that
a score of 9.3 means that a ninth grader would be able to read the document.

> Further reading on
[Wikipedia](https://en.wikipedia.org/wiki/Gunning_fog_index)

#### The SMOG Index

```python
textstat.smog_index(text)
```

Returns the SMOG index of the given text. This is a grade formula in that
a score of 9.3 means that a ninth grader would be able to read the document.

Texts of fewer than 30 sentences are statistically invalid, because
the SMOG formula was normed on 30-sentence samples. textstat requires at
least 3 sentences for a result.

> Further reading on
[Wikipedia](https://en.wikipedia.org/wiki/SMOG)

#### Automated Readability Index

```python
textstat.automated_readability_index(text)
```

Returns the ARI (Automated Readability Index) which outputs
a number that approximates the grade level needed to
comprehend the text.

For example if the ARI is 6.5, then the grade level to comprehend
the text is 6th to 7th grade.

> Further reading on
[Wikipedia](https://en.wikipedia.org/wiki/Automated_readability_index)

#### The Coleman-Liau Index

```python
textstat.coleman_liau_index(text)
```

Returns the grade level of the text using the Coleman-Liau Formula. This is
a grade formula in that a score of 9.3 means that a ninth grader would be
able to read the document.

> Further reading on
[Wikipedia](https://en.wikipedia.org/wiki/Coleman%E2%80%93Liau_index)

#### Linsear Write Formula

```python
textstat.linsear_write_formula(text)
```

Returns the grade level using the Linsear Write Formula. This is
a grade formula in that a score of 9.3 means that a ninth grader would be
able to read the document.

> Further reading on
[Wikipedia](https://en.wikipedia.org/wiki/Linsear_Write)

#### Dale-Chall Readability Score

```python
textstat.dale_chall_readability_score(text)
```

Different from other tests, since it uses a lookup table
of the most commonly used 3000 English words. Thus it returns
the grade level using the New Dale-Chall Formula.

| Score       |  Understood by                                |
|-------------|-----------------------------------------------|
|4.9 or lower | average 4th-grade student or lower            |
|  5.0–5.9    | average 5th or 6th-grade student              |
|  6.0–6.9    | average 7th or 8th-grade student              |
|  7.0–7.9    | average 9th or 10th-grade student             |
|  8.0–8.9    | average 11th or 12th-grade student            |
|  9.0–9.9    | average 13th to 15th-grade (college) student  |

> Further reading on
[Wikipedia](https://en.wikipedia.org/wiki/Dale%E2%80%93Chall_readability_formula)

#### Readability Consensus based upon all the above tests

```python
textstat.text_standard(text, float_output=False)
```

Based upon all the above tests, returns the estimated school
grade level required to understand the text.

Optional `float_output` allows the score to be returned as a
`float`. Defaults to `False`.

#### Spache Readability Formula

```python
textstat.spache_readability(text)
```

Returns grade level of english text.

Intended for text written for children up to grade four.

> Further reading on
[Wikipedia](https://en.wikipedia.org/wiki/Spache_readability_formula)

#### McAlpine EFLAW Readability Score

```python
textstat.mcalpine_eflaw(text)
```

Returns a score for the readability of an english text for a foreign learner or
English, focusing on the number of miniwords and length of sentences.

It is recommended to aim for a score equal to or lower than 25. 

> Further reading on
[This blog post](https://strainindex.wordpress.com/2009/04/30/mcalpine-eflaw-readability-score/)

#### Reading Time

```python
textstat.reading_time(text, ms_per_char=14.69)
```

Returns the reading time of the given text.

Assumes 14.69ms per character.

> Further reading in
[This academic paper](https://homepages.inf.ed.ac.uk/keller/papers/cognition08a.pdf)

### Language Specific Formulas 
#### Índice de lecturabilidad Fernandez-Huerta (Spanish)  

```python
textstat.fernandez_huerta(text)
```

Reformulation of the Flesch Reading Ease Formula specifically for spanish.
The results can be interpreted similarly

> Further reading on
[This blog post](https://legible.es/blog/lecturabilidad-fernandez-huerta/)

#### Índice de perspicuidad de Szigriszt-Pazos (Spanish)  

```python
textstat.szigriszt_pazos(text)
```
Adaptation of Flesch Reading Ease formula for spanish-based texts.

Attempts to quantify how understandable a text is.

> Further reading on
[This blog post](https://legible.es/blog/perspicuidad-szigriszt-pazos/)

#### Fórmula de comprensibilidad de Gutiérrez de Polini (Spanish)  

```python
textstat.gutierrez_polini(text)
```

Returns the Guttiérrez de Polini understandability index.

Specifically designed for the texts in spanish, not an adaptation.
Conceived for grade-school level texts.

Scores for more complex text are not reliable.

> Further reading on
[This blog post](https://legible.es/blog/comprensibilidad-gutierrez-de-polini/)

#### Fórmula de Crawford (Spanish)  

```python
textstat.crawford(text)
```

Returns the Crawford score for the text.

Returns an estimate of the years of schooling required to understand the text.

The text is only valid for elementary school level texts.

> Further reading on
[This blog post](https://legible.es/blog/formula-de-crawford/)

#### Osman (Arabic)

```python
textstat.osman(text)
```

Returns OSMAN score for text.

Designed for Arabic, an adaption of Flesch and Fog Formula.
Introduces a new factor called "Faseeh".

> Further reading in
[This academic paper](https://www.aclweb.org/anthology/L16-1038.pdf)

#### Gulpease Index (Italian)

```python
textstat.gulpease_index(text)
```

Returns the Gulpease index of Italian text, which translates to 
level of education completed.

Lower scores require higher level of education to read with ease.

> Further reading on
[Wikipedia](https://it.wikipedia.org/wiki/Indice_Gulpease)

#### Wiener Sachtextformel (German)

```python
textstat.wiener_sachtextformel(text, variant)
```

Returns a grade level score for the given text.

A value of 4 means very easy text, whereas 15 means very difficult text.

> Further reading on
[Wikipedia](https://de.wikipedia.org/wiki/Lesbarkeitsindex#Wiener_Sachtextformel)

### Aggregates and Averages

#### Syllable Count

```python
textstat.syllable_count(text)
```

Returns the number of syllables present in the given text.

Uses the Python module [Pyphen](https://github.com/Kozea/Pyphen)
for syllable calculation.

#### Lexicon Count

```python
textstat.lexicon_count(text, removepunct=True)
```

Calculates the number of words present in the text.
Optional `removepunct` specifies whether we need to take
punctuation symbols into account while counting lexicons.
Default value is `True`, which removes the punctuation
before counting lexicon items.

#### Sentence Count

```python
textstat.sentence_count(text)
```

Returns the number of sentences present in the given text.

#### Character Count

```python
textstat.char_count(text, ignore_spaces=True)
```

Returns the number of characters present in the given text.

#### Letter Count

```python
textstat.letter_count(text, ignore_spaces=True)
```

Returns the number of characters present in the given text without punctuation.

#### Polysyllable Count

```python
textstat.polysyllabcount(text)
```

Returns the number of words with a syllable count greater than or equal to 3.

#### Monosyllable Count

```python
textstat.monosyllabcount(text)
```

Returns the number of words with a syllable count equal to one.

## Contributing

If you find any problems, you should open an
[issue](https://github.com/shivam5992/textstat/issues).

If you can fix an issue you've found, or another issue, you should open
a [pull request](https://github.com/shivam5992/textstat/pulls).

1. Fork this repository on GitHub to start making your changes to the master
branch (or branch off of it).
2. Write a test which shows that the bug was fixed or that the feature works as expected.
3. Send a pull request!

### Development setup

> It is recommended you use a [virtual environment](
https://docs.python.org/3/tutorial/venv.html), or [Pipenv](
https://docs.pipenv.org/) to keep your development work isolated from your
systems Python installation.

```bash
$ git clone https://github.com/<yourname>/textstat.git  # Clone the repo from your fork
$ cd textstat
$ pip install -r requirements.txt  # Install all dependencies

$ # Make changes

$ python -m pytest test.py  # Run tests
```

