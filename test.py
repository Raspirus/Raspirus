import os


def walk():
    for p, d, f in os.walk('.'):
        for file in f:
            print(p + file)

walk()
