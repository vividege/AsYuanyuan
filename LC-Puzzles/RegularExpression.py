from typing import List


def FindLongestCommonPrefix(strs: List[str]) -> str:
    if len(strs) == 1:
        return strs[0]
    elif len(strs) == 0:
        return ''
    else:
        first = strs[0]
        res = first
        for s in strs[1:]:
            while res:
                if s.startswith(res):
                    break
                else:
                    res = res[:-1]
    return res


def simplerSolution(strs: List[str]) -> str:
    res = ''
    for c in zip(*strs):
        if len(set(c)) > 1:
            break
        else:
            res += c[0]
    return res


if __name__ == '__main__':
    # print(romanToIntSimpler("MCMXCIV"))
    # print(FindLongestCommonPrefix(["flower","flow","flight", 'aavour']))
    print(simplerSolution(["flower", "flowertt", "floweraa"]))
    # a = [1,2,3,4]
    s = ['122', '123', '124', '12', '1']
    for c in zip(*s):
        print(c)
