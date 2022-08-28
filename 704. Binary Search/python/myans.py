from typing import List

nums = [-1,0,3,5,9,12]
target = 1


def search(nums: list[int], target: int) -> int:
    upper = len(nums)
    lower = 0
    while(True):
        middle = int((upper - lower)/2)
        if nums[middle] == target:
            return middle
        elif nums[middle] > target:
            upper = middle
        elif nums[middle] < target:
            lower = middle
        if middle == upper or middle == lower:
            for i in range(lower, upper):
                if nums[i] == target:
                    return i
            return -1
        
#print(search(nums,target))




def search2( nums: List[int], target: int) -> int:
    left = 0
    right = len(nums) -1
    while left <= right:
        pivot = left + int((right - left)/2)
        if(nums[pivot] == target):
            return pivot
        if(nums[pivot] > target):
            right = pivot -1
        else:
            left = pivot + 1
    return -1

print(search2(nums,target))