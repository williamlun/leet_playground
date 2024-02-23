from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = {}
        length = len(nums) / 2
        for num in nums:
            if num in count:
                count[num] += 1
            else:
                count[num] = 1
            if count[num] > length:
                return num


nums1 = [3, 2, 3]
nums2 = [2, 2, 1, 1, 1, 2, 2]
print(Solution().majorityElement(nums1))
print(Solution().majorityElement(nums2))
