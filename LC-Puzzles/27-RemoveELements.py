from typing import List


def removeElements(nums: List[int], val: int):
    ### The solution doesn't care about the left elements of the nums, except the first length of non duplicated

    ##### My Solution
    # index = list()
    # counter = 0
    # for mover in range(len(nums)):
    #     if nums[mover] == val:
    #         index.append(mover)
    #     else:
    #         counter += 1
    # while index:
    #     nums.pop(index.pop())
    #
    # return counter

    ##### Two Pointer Solution
    i = 0
    for j in range(len(nums)):
        if nums[j] != val:
            nums[i] = nums[j]
            i += 1
    return i


if __name__ == '__main__':
    nums = [0, 1, 2, 2, 3, 0, 4, 2]
    val = 2
    print(removeElements(nums, val))
    print(nums)
