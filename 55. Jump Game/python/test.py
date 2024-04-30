from typing import List


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        zero_pointer = 0
        if len(nums) == 1:
            return True
        if nums[0] == 0:
            return False
        while zero_pointer < len(nums) - 1:
            if nums[zero_pointer] == 0:
                pivot = zero_pointer - 1
                while pivot < zero_pointer:
                    if nums[pivot] > zero_pointer - pivot:
                        break
                    pivot -= 1
                    if pivot < 0:
                        return False
            zero_pointer += 1
        return True


test1 = [2, 3, 1, 1, 4]
test2 = [3, 2, 1, 0, 4]
test3 = [2, 0, 0]

print(Solution().canJump(test1))
print(Solution().canJump(test2))
print(Solution().canJump(test3))
