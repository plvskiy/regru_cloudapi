from setuptools import setup, find_packages
import os

here = os.path.abspath(os.path.dirname(__file__))


def read(filename):
    with open(filename, encoding='utf-8') as file:
        return file.read()


setup(
    name='regru_cloudapi',
    description='Reg.ru CloudAPI Python library',
    version='1.2.13',
    url='https://github.com/plvskiy/regru_cloudapi',
    author='Matthew Polovskiy',
    author_email='github@plvskiy.ru',
    packages=find_packages(),
    python_requires='>=3.6',
    long_description=read('README.md'),
    long_description_content_type='text/markdown',
    license='MIT',
    classifiers=['Programming Language :: Python :: 3',
                 'License :: OSI Approved :: MIT License'
                 ],
    install_requires=[
        'setuptools==65.4.1',
        'requests==2.28.1'
    ]
)


