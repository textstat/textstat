# textstat

Python package to calculate statistics from text to determine
readability, complexity and grade level of a particular corpus.

## Useage

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

>>> textstat.text_standard(test_data)
'12th and 13th grade'
```


## Install

You can install textstat either via the Python Package Index
(PyPI) or from source.

#### Install using pip

```shell
pip install textstat
```

#### Install using easy_install

```shell
easy_install textstat
```

#### Install latest version from GitHub

```shell
git clone https://github.com/shivam5992/textstat.git
cd textstat
pip install .
```

#### Install from PyPI

Download the latest version of textstat from
http://pypi.python.org/pypi/textstat/

You can install it by doing the following:

```shell
tar xfz textstat-*.tar.gz
cd textstat-*/
python setup.py build
python setup.py install # as root
```
