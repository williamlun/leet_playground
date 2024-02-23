from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        index = 1
        count = 0
        pivot = nums[0]
        for i in range(len(nums)):
            if i == 0:
                continue
            if nums[i] == pivot:
                count += 1
                if count < 2:
                    nums[index] = nums[i]
                    index += 1
            else:
                nums[index] = nums[i]
                index += 1
                pivot = nums[i]
                count = 0
        print(nums)
        return index


nums1 = [1, 1, 1, 2, 2, 3]
nums2 = [0, 0, 1, 1, 1, 1, 2, 3, 3]

print(Solution().removeDuplicates(nums1))
print(Solution().removeDuplicates(nums2))
