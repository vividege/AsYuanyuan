from typing import List


def threeSum(nums: List[int]):
    res = set()
    nums.sort()
    for i, v in enumerate(nums[:-2]):
        head = i + 1
        end = len(nums) - 1
        target = -v
        while head < end:
            if nums[head] + nums[end] == target:
                res.add((v, nums[head], nums[end]))
                head += 1
                end -= 1
            elif nums[head] + nums[end] > target:
                end -= 1
            else:
                head += 1
    return list(map(list, res))


def threeSumClosest(nums: List[int], target: int) -> List[int]:
    nums.sort()
    res = sum(nums[:3])
    for i, v in enumerate(nums):
        head = i + 1
        end = len(nums) - 1
        while head < end:
            s = sum((nums[head], nums[end], v))
            if abs(s - target) < abs(res - target):
                res = s
            if s < target:
                head += 1
            elif s > target:
                end -= 1
            else:
                break
    return res


def letterCombination(digits: str) -> List[str]:
    lip = {'2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl',
           '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'}
    if len(digits) == 0:
        return []
    start = list(lip.get(digits[0]))
    if len(digits) == 1:
        return start
    for d in digits[1:]:
        ret = []
        for v in list(lip.get(d)):
            for w in start:
                ret.append(w + v)
        start = ret

    return start


def letterCombinationsBetter(digits):
    """
    :type digits: str
    :rtype: List[str]
    """
    phone = {'2': ['a', 'b', 'c'],
             '3': ['d', 'e', 'f'],
             '4': ['g', 'h', 'i'],
             '5': ['j', 'k', 'l'],
             '6': ['m', 'n', 'o'],
             '7': ['p', 'q', 'r', 's'],
             '8': ['t', 'u', 'v'],
             '9': ['w', 'x', 'y', 'z']}

    def backtrack(combination, next_digits):
        # if there is no more digits to check
        if len(next_digits) == 0:
            # the combination is done
            output.append(combination)
        # if there are still digits to check
        else:
            # iterate over all letters which map
            # the next available digit
            for letter in phone[next_digits[0]]:
                # append the current letter to the combination
                # and proceed to the next digits
                backtrack(combination + letter, next_digits[1:])

    output = []
    if digits:
        backtrack("", digits)
    return output


def fourSumEqualTarget(nums: List[int], target: int) -> List[int]:
    nums.sort()
    res = []
    for i in range(len(nums) - 3):
        if nums[i] > target / 4.0:
            break
        if i > 0 and nums[i] == nums[i - 1]:
            continue
        target2 = target - nums[i]
        for j in range(i + 1, len(nums) - 2):
            if nums[j] > target2 / 3.0:
                break
            if j > i + 1 and nums[j] == nums[j - 1]:
                continue
            h = j + 1
            t = len(nums) - 1
            target3 = target2 - nums[j]

            if nums[h] > target3 / 2.0:
                continue
            if nums[t] < target3 / 2.0:
                continue

            while h < t:
                sum_value = nums[h] + nums[t]
                if sum_value == target3:
                    res.append([nums[i], nums[j], nums[h], nums[t]])
                    hh = nums[h]
                    h += 1
                    while h < t and hh == nums[h]:
                        h += 1
                    tt = nums[t]
                    t -= 1
                    while h < t and tt == nums[t]:
                        t -= 1
                elif sum_value < target3:
                    h += 1
                else:
                    t -= 1
    return res


def fourSum(num, target):
    num.sort()
    result = []
    for i in range(len(num) - 3):
        if num[i] > target / 4.0:
            break
        if i > 0 and num[i] == num[i - 1]:
            continue
        target2 = target - num[i]
        for j in range(i + 1, len(num) - 2):
            if num[j] > target2 / 3.0:
                break
            if j > i + 1 and num[j] == num[j - 1]:
                continue
            k = j + 1
            l = len(num) - 1
            target3 = target2 - num[j]
            # we should use continue not break
            # because target3 changes as j changes
            if num[k] > target3 / 2.0:
                continue
            if num[l] < target3 / 2.0:
                continue
            while k < l:
                sum_value = num[k] + num[l]
                if sum_value == target3:
                    result.append([num[i], num[j], num[k], num[l]])
                    kk = num[k]
                    k += 1
                    while k < l and num[k] == kk:
                        k += 1

                    ll = num[l]
                    l -= 1
                    while k < l and num[l] == ll:
                        l -= 1
                elif sum_value < target3:
                    k += 1
                else:
                    l -= 1
    return result
if __name__ == '__main__':
    # print(threeSumClosest([-1, 2, 1, -4], 1))
    # print(letterCombinationsBetter('23'))
    print(fourSumEqualTarget([-3, -2, -1, 0, 0, 1, 2, 3], 0))
