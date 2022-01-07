#!/usr/bin/python3
import sys

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.

def tokenize(filepath):
    tokens = list()
    if filepath is None:
        return tokens
    with open(filepath, 'r') as f:
        for line in f:
            for word in line.split():
                if word.isalnum():
                    tokens.append(word.upper())
    return tokens

def computeWordFrequencies(tokensList):
    if len(tokensList) == 0:
        return {}


if __name__ == '__main__':
    # print_hi('PyCharm')
    tokens = tokenize(sys.argv[1])
    print(len(tokens))
    print(tokens)
