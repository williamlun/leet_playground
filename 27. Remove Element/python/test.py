from typing import List


# given nums: List[int], val: int
# [3,2,2,3]  -> [2,2,_,_]


class Solution1:
    def removeElement(self, nums: List[int], val: int) -> int:
        index = 0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[index] = nums[i]
                index += 1
        print(nums)
        return index


class Solution2:
    def removeElement(self, nums: List[int], val: int) -> int:
        original_length = len(nums)
        for index, num in enumerate(nums):
            if num == val:
                del nums[index]
        not_equal = len(nums)
        print(nums)

        return not_equal


nums_1 = [3, 2, 2, 3]
val_1 = 3

nums_2 = [0, 1, 2, 2, 3, 0, 4, 2]
val_2 = 2

print(Solution2().removeElement(nums_1, val_1))
print(Solution2().removeElement(nums_2, val_2))
