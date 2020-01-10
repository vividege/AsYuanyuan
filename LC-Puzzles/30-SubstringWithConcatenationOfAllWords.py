from typing import List
from collections import Counter


def findAllStrings(s: str, words: List[str]):
    ###My TLE Solution
    '''
    sLen = len(s)
    if 0 == sLen or 0 == len(words):
        return []
    wLen = len(words[0])
    ret = list()


    for i in range(sLen):
        j = i
        tempWords = words.copy() #这里使用浅拷贝就行,如果list包含有多层list就用copy.deepcopy()
        while j <= sLen - wLen:
            subStr = s[j:j+wLen]
            if subStr in tempWords:
                tempWords.pop(tempWords.index(subStr))
                j += wLen
                if not tempWords:
                    break
            else:
                break
        if not tempWords:
            ret.append(i)
    return ret
    '''

    ## The LeetCoder's Solution with window slide and utilize Collections.Counter
    sLen = len(s)
    if 0 == sLen or 0 == len(words):
        return []
    wLen = len(words[0])
    ret = []
    winLen = len(words) * wLen
    for i in range(0, sLen - winLen + 1):
        temp = []
        word_win = s[i: i + winLen]
        for j in range(0, winLen, wLen):
            temp.append(word_win[j: j + wLen])
        if Counter(temp) == Counter(words):
            ret.append(i)
    return ret


if __name__ == '__main__':
    s = "barfoothefoobarman"
    words = ["foo", "bar"]
    print(findAllStrings(s, words))
    # print(words.index('best'))
