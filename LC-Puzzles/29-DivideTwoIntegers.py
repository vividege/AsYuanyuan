import math


def divideTwoIntegers(dividend: int, divisor: int) -> int:
    # isDividendNeg = False
    # isDivisorNeg = False
    # ret = 0
    # if dividend < 0:
    #     isDividendNeg = True
    #     dividend = -dividend
    # if divisor == 0:
    #     raise Exception("Divisor can't be ZERO!")
    # if divisor < 0:
    #     isDivisorNeg = True
    #     divisor = -divisor
    # if divisor == 1:
    #     return dividend
    #
    # mover = int(math.log2(10))
    # left = dividend - divisor*mover
    #
    # ret = dividend >> mover + left * dividend
    # if isDivisorNeg ^ isDividendNeg:
    #     return -ret
    # else:
    #     return ret

    # Others Approach
    isDividendNeg = False
    isDivisorNeg = False
    ret = 0
    if dividend < 0:
        isDividendNeg = True
        dividend = -dividend
    if divisor == 0:
        raise Exception("Divisor can't be ZERO!")
    if divisor < 0:
        isDivisorNeg = True
        divisor = -divisor
    # if divisor == 1:
    #     return dividend
    '''
    解题思路：
    0. 最直观的思路是：一直除直到余数小于除数，但是这个方式太慢了
    1.任何数都可以分解为2的n次方之和
    2. 比如：25/4 = 4 * 4 + 4 * 2 +1 ==> 4+2 = 6
    3. 比如：25/3 = 3 * 8 + 1 ==> 8+0 = 8
    4. 比如：40/7 = 7 * 4 +7 * 1 + 5 ==> 4+1 = 5
    '''
    while divisor <= dividend:
        temp = divisor
        double = 1
        while (temp << 1) <= dividend:
            temp <<= 1
            double <<= 1
        dividend -= temp
        ret += double
        ret = -ret if isDividendNeg ^ isDivisorNeg else ret
        return min(max(-2147483648, ret), 2147483647)


if __name__ == '__main__':
    # print(divideTwoIntegers(2147483648,1))
    print(divideTwoIntegers(-2147483648, -1))
