from typing import List


def removeDuplicate(l: List[int]):
    if not l or 0 == len(l):
        return 0
    pointer = 0
    counter = 1
    base = l[0]
    for idx, val in enumerate(l):
        if val > base:
            base = val
            counter += 1
            pointer += 1
            temp = l[pointer]
            l[pointer] = l[idx]
            l[idx] = temp

    print("Number=%d" % counter)
    print(l)


def removeDuplicate_Better(nums: List[int]):
    if not nums or 0 == len(nums):
        return 0
    base = nums[0]
    counter = 0
    for e in nums:
        if e != base:
            counter += 1
            base = e
            nums[counter] = e
    print(nums)
    return counter + 1


if __name__ == '__main__':
    print(removeDuplicate_Better([1, 1, 2]))
    print(removeDuplicate_Better([1, 1, 2, 2, 2, 2, 3, 3, 4, 4, 5, 6]))
