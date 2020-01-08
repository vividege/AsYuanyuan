def strStr(haystack: str, needle: str) -> int:
    lengthN = len(needle)
    if not lengthN:
        return 0
    for i in range(len(haystack) - lengthN + 1):
        if haystack[i:i + lengthN] == needle:
            return i
    return -1


if __name__ == '__main__':
    haystack = ""
    needle = ""
    print(strStr(haystack, needle))
