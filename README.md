# Raspirus - Raspberry Pi Virusscanner
[![Python Flake8](https://github.com/Benji377/Raspirus/actions/workflows/python-flake8.yml/badge.svg)](https://github.com/Benji377/Raspirus/actions/workflows/python-flake8.yml)
[![Pylint](https://github.com/Benji377/Raspirus/actions/workflows/pylint.yml/badge.svg)](https://github.com/Benji377/Raspirus/actions/workflows/pylint.yml)

## Introduction
Even to this day, there are still some devices that for whatever reason can't have an antivirus or are outside the internet. 
This means that transferring files from your personal laptop or pc to these devices might be a very dangerous thing. Especially
when done with unsecured USB-sticks. To solve this issue, Raspirus has been invented. A black box where you attach your hard-drive
and it removes threats from it, making it safer.

## Design:
The design of the GUI is as easy and user-freindly as possible, without limiting its functionality. The whole Mockup of the app
has been planned and designed using Figma and you can take a look at the result using the link below.\
The actual design will then be coded with Qt \
Figma: https://www.figma.com/file/pkgpwieNbhYiOi4Gz6Uyt6/Raspirus?node-id=0%3A1

## Why Python? And what is The Big Refactoring?
The project was initially planned to be created in C++ as I thought it would be much faster in scanning large quantities of Hashes, compare strings and list files. 
But I have almost no experience in C++ and I wanted to use this opportunity. 
After a lot of struggle I eventually got it to work, but the code looked ugly and I didn't fully understand everything that was going on.
So after some more thought I decided to switch back to Python, which I know far better.
Python isn't that slow anymore, and for the purpose I need it for its actually quite ok.

## Instructions
Coming soon
