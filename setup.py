from setuptools import setup, find_packages
import os

here = os.path.abspath(os.path.dirname(__file__))


def read(filename):
    with open(filename, encoding='utf-8') as file:
        return file.read()


about = {}
with open(os.path.join(here, '__version__.py'), 'r') as f:
    exec(f.read(), about)


setup(
    name=about['__title__'],
    version=about['__version__'],
    url=about['__url__'],
    author=about['__author__'],
    packages=find_packages(),
    python_requires='>=3.6',
    long_description=read('README.md'),
    long_description_content_type='text/markdown'
)

classifiers = ['Programming Language :: Python :: 3']
