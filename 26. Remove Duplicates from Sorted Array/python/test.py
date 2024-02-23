from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        index = 1
        pivot = nums[0]
        for i in range(len(nums)):
            if i == 0:
                continue
            if nums[i] != pivot:
                nums[index] = nums[i]
                index += 1
            pivot = nums[i]
        print(nums)
        return index


nums_1 = [1, 1, 2]
nums_2 = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]

print(Solution().removeDuplicates(nums_1))

print(Solution().removeDuplicates(nums_2))
