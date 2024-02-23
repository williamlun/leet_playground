from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = 0

        for num in nums:
            if count == 0:
                candidate = num
            count += 1 if num == candidate else -1
        return candidate


nums1 = [3, 2, 3]
nums2 = [2, 2, 1, 1, 1, 2, 2]
print(Solution().majorityElement(nums1))
print(Solution().majorityElement(nums2))
