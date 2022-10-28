from typing import List


class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        sum_of_list = sum(nums)
        leftsum = 0
        for index, num in enumerate(nums):
            if leftsum == (sum_of_list - leftsum - num):
                return index
            leftsum = leftsum + nums[index]
        return -1


nums = [1, 2, 3]

output = Solution().pivotIndex(nums)
print(output)
