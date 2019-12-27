def romanToInteger(s: str):
    repo = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    sum = 0
    if len(s) <= 0:
        return sum
    elif len(s) == 1 and s[0] in repo.keys():
        return sum + repo.get(s[0])
    else:
        if s[0] == 'I':
            if s[1] == 'V':
                sum = sum + 4 + romanToInteger(s[2:])
            elif s[1] == 'X':
                sum = sum + 9 + romanToInteger(s[2:])
            else:
                sum = sum + 1 + romanToInteger(s[1:])
        elif s[0] == 'X':
            if s[1] == 'L':
                sum = sum + 40 + romanToInteger(s[2:])
            elif s[1] == 'C':
                sum = sum + 90 + romanToInteger(s[2:])
            else:
                sum = sum + 10 + romanToInteger(s[1:])
        elif s[0] == 'C':
            if s[1] == 'D':
                sum = sum + 400 + romanToInteger(s[2:])
            elif s[1] == 'M':
                sum = sum + 900 + romanToInteger(s[2:])
            else:
                sum = sum + 100 + romanToInteger(s[1:])
        elif s[0] in repo.keys():
            sum = sum + repo.get(s[0]) + romanToInteger(s[1:])
        else:
            raise Exception("Incorrect Input: " + s[0])
        return sum


def romanToIntSimple(s: str) -> int:
    repo = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    sum = 0
    for c in s:
        sum += repo.get(c)
    if "CM" in s or "CD" in s:
        sum -= 200
    if "XC" in s or "XD" in s:
        sum -= 20
    if "IX" in s or "IV" in s:
        sum -= 2
    return sum


def romanToIntSimpler(s: str) -> int:
    repo = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    sum = 0
    prev = 0
    for i in s[::-1]:
        curr = repo[i]
        if prev > curr:
            sum -= curr
        else:
            sum += curr
        prev = curr
    return sum


def intToRomanHL(num: int) -> str:
    repo = {1: 'I', 5: 'V', 10: 'X', 50: 'L', 100: 'C', 500: 'D', 1000: 'M',
            4: 'IV', 9: 'IX', 40: 'XL', 90: 'XC', 400: 'CD', 900: 'CM'}
    divider = [1000, 100, 10, 1]
    s = ''

    for d in divider:
        res = num // d
        num = num % d
        if res == 0:
            continue
        if repo.get(res * d, None):
            s += repo.get(res * d)
        else:
            if res >= 5:
                s += repo.get(5 * d)
                res -= 5
            s += repo.get(d) * res
    return s


def intToRomanSimpler(num: int) -> str:
    numbers = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
    romans = ['M', 'CM', 'D', 'CD', 'C', 'XC', 'L', 'XL', 'X', 'IX', 'V', 'IV', 'I']
    s = ''
    for n, r in zip(numbers, romans):
        res = num // n
        s += r * res
        num %= n
    return s


if __name__ == '__main__':
    # print(romanToIntSimpler("MCMXCIV"))

    print(intToRomanSimpler(1994))
    # print(3//2)
