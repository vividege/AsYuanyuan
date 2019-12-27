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


if __name__ == '__main__':
    # print(threeSumClosest([-1, 2, 1, -4], 1))
    print(letterCombination('27'))
    print(len(letterCombination('27')))
