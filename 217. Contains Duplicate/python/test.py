from typing import List


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        seen = {}
        for num in nums:
            if num in seen:
                return True
            seen[num] = 1
        return False


print(Solution().containsDuplicate([1, 2, 3, 1]))
print(Solution().containsDuplicate([1, 2, 3, 4]))
print(Solution().containsDuplicate([1, 1, 1, 3, 3, 4, 3, 2, 4, 2]))


class Solution2:
    def containsDuplicate(self, nums: List[int]) -> bool:
        seen = set()
        for num in nums:
            if num in seen:
                return True
            seen.add(num)
        return False


print(Solution2().containsDuplicate([1, 2, 3, 1]))
print(Solution2().containsDuplicate([1, 2, 3, 4]))
print(Solution2().containsDuplicate([1, 1, 1, 3, 3, 4, 3, 2, 4, 2]))


class Solution3:
    def containsDuplicate(self, nums: List[int]) -> bool:
        set_num = set(nums)
        if len(set_num) == len(nums):
            return False
        else:
            return True


print("Solution3")
print(Solution3().containsDuplicate([1, 2, 3, 1]))
print(Solution3().containsDuplicate([1, 2, 3, 4]))
print(Solution3().containsDuplicate([1, 1, 1, 3, 3, 4, 3, 2, 4, 2]))
