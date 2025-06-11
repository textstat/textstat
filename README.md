# Textstat

_Textstat is an easy to use Python library that analyzes text to provide detailed statistics, readability scores, and complexity metrics. Perfect for content analysis, education, and natural language processing._

[![GitHub Workflow Status (main)](https://img.shields.io/github/actions/workflow/status/textstat/textstat/test.yml?branch=main&label=main&logo=github&logoColor=white)](https://github.com/textstat/textstat/actions/workflows/test.yml)
[![License](https://img.shields.io/github/license/textstat/textstat)](https://github.com/textstat/textstat/blob/main/LICENSE)
[![PyPI version](https://img.shields.io/pypi/v/textstat.svg)](https://pypi.org/project/textstat/)
[![PyPI - Downloads](https://img.shields.io/pypi/dm/textstat?logo=pypi&logoColor=white)](https://pypistats.org/packages/textstat)

<p>
  <p align="center">
    <img width="100%" src=".github/splash.png">
  </p>
  <p align="right">
    <sup>Photo by <a href="https://unsplash.com/@impatrickt">Patrick Tomasso</a>
    on <a href="https://unsplash.com/images/things/book">Unsplash</a></sup>
  </p>
</p>



## Usage

```python
>>> from textstat import Text, Sentence, Word

>>> my_text = Text(
  "Alice was beginning to get very tired of sitting by her sister on the "
  "bank, and of having nothing to do: once or twice she had peeped into "
  "the book her sister was reading, but it had no pictures or "
  "conversations in it, “and what is the use of a book,” thought Alice "
  "“without pictures or conversations?”"
)

>>> my_text.stats()
{'letters': 236, 'characters': 246, 'words': 57, 'sentences': 1}

>>> my_text.flesch_reading_ease()
31.727368421052645

>>> my_text.filter(Word.length >= 10)
[Word('conversations'), Word('conversations')]
```

For full documentation, see https://docs.textstat.org/

## Installation

`textstat` is available on [PyPi](https://pypi.org/project/textstat/) and [Conda Forge](https://anaconda.org/conda-forge/textstat).

```
pip install textstat
```

```
conda install textstat
```
