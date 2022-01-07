#!/usr/bin/python3
import sys
import partA as tokenizer


class Trie:

    def __init__(self, words: list):
        # Instantiate the root of trie as an empty dictionary
        self.root = dict()

        # Creating Trie from the list of given words
        for word in words:
            current_dict = self.root
            for letter in word:
                current_dict = current_dict.setdefault(letter, {})
            current_dict['__last_word__'] = '__last_word__'

    def addWord(self, word):
        current_dict = self.root
        for letter in word:
            current_dict = current_dict.setdefault(letter, {})
        current_dict['__last_word__'] = '__last_word__'

    def findInTrie(self, word, removeEle=False):
        current_dict = self.root
        for letter in word:
            if letter not in current_dict:
                return False
            current_dict = current_dict[letter]
        found = '__last_word__' in current_dict
        if found and removeEle:
            del current_dict['__last_word__']
        return found


def getCommonToken(file1: str, file2: str):
    num_of_common_tokens = 0

    if file1 == '' or file2 == '':
        return num_of_common_tokens

    tokensMap = tokenizer.computeWordFrequencies(tokenizer.tokenize(file1))

    try:
        with open(file2, 'r') as f:
            for line in f:
                for word in line.split():
                    if word.isalnum() and word.upper() in tokensMap:
                        num_of_common_tokens += 1
                        # Remove entry from the map so that there is no need to keep track of
                        # multiple occurrences
                        del tokensMap[word.upper()]
    except Exception as e:
        print(e)
        sys.exit(0)

    # tokens = tokenizer.tokenize(file1)
    # trieOfTokens = Trie(tokens)
    #
    # with open(file2, 'r') as f:
    #     for line in f:
    #         for word in line.split():
    #             if word.isalnum() and trieOfTokens.findInTrie(word.upper(), True):
    #                 num_of_common_tokens += 1

    return num_of_common_tokens


if __name__ == '__main__':
    if (len(sys.argv) < 3):
        sys.exit(0)
    textfile1 = sys.argv[1]
    textfile2 = sys.argv[2]
    print(getCommonToken(textfile1, textfile2))
    # tokens = tokenizer.tokenize(textfile1)
    # root = Trie()
    # root.make_trie(tokens)
    # print(root.findInTrie("SME"))
