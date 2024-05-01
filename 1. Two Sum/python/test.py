from typing import List


# O(n^2)
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]


print("Sol1")
print(Solution().twoSum([2, 7, 11, 15], 9))
print(Solution().twoSum([3, 2, 4], 6))
print(Solution().twoSum([3, 3], 6))


class Solution2:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            if nums[i] + nums[i + 1] == target:
                return [i, i + 1]


print("Solution2")
print(Solution2().twoSum([2, 7, 11, 15], 9))
print(Solution2().twoSum([3, 2, 4], 6))
print(Solution2().twoSum([3, 3], 6))


class Solution3:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            find = target - nums[i]
            if find in nums[i + 1 :]:
                return [i, nums.index(find, i + 1)]


print("Solution3")
print(Solution3().twoSum([2, 7, 11, 15], 9))
print(Solution3().twoSum([3, 2, 4], 6))
print(Solution3().twoSum([3, 3], 6))


class Ans1:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numMap = {}
        n = len(nums)

        # Build the hash table
        for i in range(n):
            numMap[nums[i]] = i

        # Find the complement
        for i in range(n):
            complement = target - nums[i]
            if complement in numMap and numMap[complement] != i:
                return [i, numMap[complement]]

        return []  # No solution found


print("Ans1")
print(Ans1().twoSum([2, 7, 11, 15], 9))
print(Ans1().twoSum([3, 2, 4], 6))
print(Ans1().twoSum([3, 3], 6))
