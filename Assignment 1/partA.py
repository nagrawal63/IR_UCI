#!/usr/bin/python3
import re
import sys


def tokenize(filepath: str):
    tokens = list()
    if filepath is None:
        return tokens

    try:
        with open(filepath, 'r') as f:
            # for line in f:
            #     for word in line.split():
            #         if word.isalnum():
            #             tokens.append(word.lower())
            for line in f:
                # for word in re.finditer(r'\w+', line):
                #match either words or either of the special characters with regex
                for word in re.finditer(r'([a-zA-Z0-9@#*&\']+|[!^$(){}\[\]><:;."])', line):
                    tokens.append(word.group().lower())
    except Exception as e:
        print(e)
        return tokens
    return tokens


def computeWordFrequencies(tokensList: list):
    if len(tokensList) == 0:
        return {}
    tokenMap = dict()
    for token in tokensList:
        if token not in tokenMap:
            tokenMap[token] = 1
        else:
            tokenMap[token] += 1

    return tokenMap


def printFrequencyMap(frequenciesMap: dict):
    for key, value in frequenciesMap.items():
        print("<token>{}<freq>{}".format(key, value))


if __name__ == '__main__':
    if len(sys.argv) < 2:
        sys.exit(0)

    tokens = tokenize(sys.argv[1])
    # print(len(tokens))
    # print(tokens)
    tokenMap = computeWordFrequencies(tokens)
    # print(tokenMap)
    printFrequencyMap(tokenMap)