from setuptools import setup

setup(
    name='textstat',
    packages=['textstat'],
    version='0.4.1',
    description='Calculate statistical features from text',
    author='Shivam Bansal, Chaitanya Aggarwal',
    author_email='shivam5992@gmail.com',
    url='https://github.com/shivam5992/textstat',
    long_description=open('README.md').read(),
    package_data={'': ['easy_word_list']},
    include_package_data=True,
    install_requires=['pyphen', 'repoze.lru'],
    license='MIT',
    classifiers=(
        "Programming Language :: Python",
        "Programming Language :: Python :: 2.5",
        "Programming Language :: Python :: 2.6",
        "Programming Language :: Python :: 2.7",
        ),
)
