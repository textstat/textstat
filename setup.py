from setuptools import setup
from io import open

setup(
    name='textstat',
    packages=['textstat'],
    version='0.7.3',
    description='Calculate statistical features from text',
    author='Shivam Bansal, Chaitanya Aggarwal',
    author_email='shivam5992@gmail.com',
    url='https://github.com/shivam5992/textstat',
    long_description=open('README.md', encoding='utf-8').read(),
    long_description_content_type='text/markdown',
    package_data={'': ['easy_word_list']},
    include_package_data=True,
    install_requires=['pyphen'],
    license='MIT',
    python_requires=">=3.6",
    classifiers=(
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3 :: Only",
        "Intended Audience :: Developers",
        "Intended Audience :: Education",
        "Intended Audience :: Science/Research",
        "Topic :: Text Processing",
        ),
)
