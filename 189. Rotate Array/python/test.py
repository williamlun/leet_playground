from typing import List


class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        for i in range(k):
            nums.insert(0, nums.pop())
        print(nums)


class Solution2:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k = k % len(nums)
        if k == 0:
            return
        length = len(nums) - k
        nums[:] = nums[-k:] + nums[:length]
        print(nums)


nums1 = [1, 2, 3, 4, 5, 6, 7]
k1 = 3
nums2 = [-1, -100, 3, 99]
k2 = 2
Solution2().rotate(nums1, k1)
Solution2().rotate(nums2, k2)
