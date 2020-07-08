# R-07 Python Package

[![Setup Automated](https://img.shields.io/badge/setup-automated-blue?logo=gitpod)](https://gitpod.io/from-referrer/)
![Test passing](https://img.shields.io/badge/Tests-passing-brightgreen.svg)
![Python Version](https://img.shields.io/badge/python-3.x-brightgreen.svg)
[![PyPI version](https://badge.fury.io/py/R07.svg)](https://badge.fury.io/py/R07)
![](https://img.shields.io/pypi/dm/R07?color=green&label=pypi-downloads&style=flat-square)
![](https://img.shields.io/github/last-commit/rahulbordoloi/pypi-publish?style=flat-square)
[![Open Source Love png2](https://badges.frapsoft.com/os/v2/open-source.png?v=103)](https://github.com/ellerbrock/open-source-badges/)

## About

This Package contains all the Modules developed by [@rahulbordoloi](https://github.com/rahulbordoloi) published to PyPI.

All the classes will be imported under the package `R07`.

## Installation

Run the following command on your terminal to install : 

```python
pip install R07
```

## Usage

1. For Module 1, `say_hello`

```python
from R07 import say_hello

# Generate 'Hello R-07!'
say_hello()

# Generate 'Hello, Rahul!'
say_hello('Rahul')
```

2. For Module 2, `YTDownloader`

```python
from R07 import YTDownloader

# Call Downloader Class
YTDownloader()

# Directly Download the File from the URL
YTDownloader('https://youtu.be/xl8zdCY-abw')
```

Note : 
1. Calling `YTDownloader()` without arguments prompts you to enter the URL after you call it. <br>
2. The File will get downloaded in your current working directory. <br>
3. For more information, refer to my repository [Youtube-Video-Downloader](https://github.com/rahulbordoloi/Youtube-Video-Downloader.git)

## Outputs

1. For `say_hello`,

```
>>> from R07 import say_hello
>>> say_hello()
'Hello R-07!'
>>> say_hello('Rahul')
'Hello, Rahul!'
```

2. For `YTDownloader`,

```
>>> from R07 import YTDownloader
>>> YTDownloader()
Enter the Youtube URL of the Video you want to Download :
https://youtu.be/xl8zdCY-abw
-----------------------------------
Title :  YouTube
Views :  1015559
Length :  128 seconds
Description :  The Medellin cartel - the most violent, ruthless and wealthy criminal organization in the history of modern crime. And the one man who lorded over them all... Pablo Escobar.

NARCOS is the true story of the U.S. and Colombian efforts to battle the Medellin cartel during the cocaine-fueled drug wars of the 1980's. Multi-layered and multi-faceted, NARCOS depicts a brutal world where lines are blurred and little is black and white. The Netflix original series, starring Wagner Moura, Boyd Holbrook, and Pedro Pascal.

http://www.netflix.com
Rating :  4.9314308
-----------------------------------
Starting Download ...
Download Successful, You can find your File at : D:\Studies (Contd.)\Projects\PyPi Publish
Time Elapsed :  16.45 seconds
>>> YTDownloader('https://www.youtube.com/watch?v=cq2iTHoLrt0')
-----------------------------------
Title :  YouTube
Views :  2787903
Length :  147 seconds
Description :  The end is the beginning. And the beginning is the end. Dark comes full circle on June 27th.

Watch Dark on Netflix: https://www.netflix.com/title/80100172

SUBSCRIBE: http://bit.ly/29qBUt7

About Netflix:
Netflix is the world's leading streaming entertainment service with 183 million paid memberships in over 190 countries enjoying TV series, documentaries and feature films across a wide variety of genres and languages. Members can watch as much as they want, anytime, anywhere, on any internet-connected screen. Members can play, pause and resume watching, all without commercials or commitments.

Dark Season 3 | Official Trailer | Netflix
https://youtube.com/Netflix

The time-twisting madness reaches its conclusion in a strange new world, where some things are quite familiar — and others are disturbingly not.
Rating :  4.9651532
-----------------------------------
Starting Download ...
Download Successful, You can find your File at : D:\Studies (Contd.)\Projects\PyPi Publish
Time Elapsed :  7.13 seconds
```

## Developing R07

To install `R07`, along with the tools you need to develop and run tests, run the following in your virtualenv:

```bash
$ pip install -e .[dev]
```

## Contact Author

Name : Rahul Bordoloi <br>
Website : https://rahulbordoloi.me <br>
Email : mail@rahulbordoloi.me <br>

[![forthebadge made-with-python](http://ForTheBadge.com/images/badges/made-with-python.svg)](https://www.python.org/)
[![ForTheBadge built-with-love](http://ForTheBadge.com/images/badges/built-with-love.svg)](https://GitHub.com/rahulbordoloi/)