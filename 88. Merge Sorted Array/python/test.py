from typing import List


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """

        if n == 0:
            return
        last_index = len(nums1) - 1
        while n > 0 and m > 0:
            if nums2[n - 1] >= nums1[m - 1]:
                nums1[last_index] = nums2[n - 1]
                n -= 1
            else:
                nums1[last_index] = nums1[m - 1]
                m -= 1
            last_index -= 1
        while n > 0:
            nums1[last_index] = nums2[n - 1]
            m -= 1
            last_index -= 1
        print(nums1)


nums1 = [1, 2, 3, 0, 0, 0]
m = 3
nums2 = [2, 5, 6]
n = 3

Solution().merge(nums1, m, nums2, n)
