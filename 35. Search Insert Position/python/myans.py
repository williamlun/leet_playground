from typing import List


nums = [0,3,5,9,12]
target = 6


def searchInsert(nums: List[int], target: int) -> int:
    upper = len(nums) - 1
    lower = 0


    while lower <= upper:
        pvivot = lower + (upper - lower) // 2
        if(nums[pvivot] == target):
            return pvivot
        if(nums[pvivot] > target):
            upper = pvivot - 1
        else:
            lower = pvivot + 1
    return lower

print(searchInsert(nums,target))