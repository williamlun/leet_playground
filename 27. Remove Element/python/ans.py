from typing import List


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        index = 0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[index] = nums[i]
                index += 1
        print(nums)
        return index


nums_1 = [3, 2, 2, 3]
val_1 = 3

nums_2 = [0, 1, 2, 2, 3, 0, 4, 2]
val_2 = 2

print(Solution().removeElement(nums_1, val_1))
print(Solution().removeElement(nums_2, val_2))
