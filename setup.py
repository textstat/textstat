from setuptools import setup, find_packages
from io import open

setup(
    name="textstat",
    packages=find_packages(),
    version="0.7.8",
    description="Calculate statistical features from text",
    author="Shivam Bansal, Chaitanya Aggarwal",
    author_email="shivam5992@gmail.com",
    url="https://github.com/textstat/textstat",
    long_description=open("README.md", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    package_data={"": ["easy_word_list"]},
    include_package_data=True,
    install_requires=["pyphen", "cmudict", "setuptools"],
    license="MIT",
    python_requires=">=3.6",
    classifiers=(
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Programming Language :: Python :: 3.13",
        "Programming Language :: Python :: 3 :: Only",
        "Intended Audience :: Developers",
        "Intended Audience :: Education",
        "Intended Audience :: Science/Research",
        "Topic :: Text Processing",
    ),
)
