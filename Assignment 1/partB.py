#!/usr/bin/python3
import sys
import partA as tokenizer


def getCommonToken(file1, file2):
    num_of_common_tokens = 0

    if file1 == '' or file2 == '':
        return num_of_common_tokens

    tokensMap = tokenizer.computeWordFrequencies(tokenizer.tokenize(file1))

    with open(file2, 'r') as f:
        for line in f:
            for word in line.split():
                if word.isalnum() and word.upper() in tokensMap:
                    num_of_common_tokens += 1
                    del tokensMap[word.upper()]
    return num_of_common_tokens


if __name__ == '__main__':
    if (len(sys.argv) < 3):
        sys.exit(0)
    textfile1 = sys.argv[1]
    textfile2 = sys.argv[2]
    print(getCommonToken(textfile1, textfile2))
