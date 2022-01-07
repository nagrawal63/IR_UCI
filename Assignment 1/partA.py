#!/usr/bin/python3
import sys


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
    tokenMap = dict()
    for token in tokensList:
        if token not in tokenMap:
            tokenMap[token] = 1
        else:
            tokenMap[token] += 1

    return tokenMap


def printFrequencyMap(frequenciesMap):
    for key, value in frequenciesMap.items():
        print("<token>{}<freq>{}".format(key, value))


if __name__ == '__main__':
    if len(sys.argv) < 2:
        sys.exit(0)
    # print_hi('PyCharm')
    tokens = tokenize(sys.argv[1])
    # print(len(tokens))
    # print(tokens)
    tokenMap = computeWordFrequencies(tokens)
    # print(tokenMap)
    printFrequencyMap(tokenMap)
