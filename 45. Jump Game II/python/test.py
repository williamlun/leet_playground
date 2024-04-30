from typing import List


class Solution:
    def jump(self, nums: List[int]) -> int:
        step = 0
        pivot = 0
        while pivot < len(nums) - 1:
            max_reach = nums[pivot] + pivot
            jump_to = pivot + 1
            temp_max = nums[jump_to]
            while jump_to <= max_reach:
                temp_max = nums[jump_to] if nums[jump_to] > temp_max else temp_max
                jump_to += 1
                if jump_to >= len(nums):
                    break
            pivot = jump_to
            step += 1
        return step


class Solution1:
    def jump(self, nums: List[int]) -> int:
        step = 0
        index = 0
        if len(nums) == 1:
            return 0
        if len(nums) - 1 <= nums[0]:
            return 1
        while index < len(nums) - 1:
            max_reach = nums[index] + index
            if max_reach >= len(nums) - 1:
                return step + 1
            target_index = index + 1
            temp_max_index = target_index
            while target_index <= max_reach:
                temp_max_index = (
                    target_index
                    if nums[target_index] + target_index
                    > nums[temp_max_index] + temp_max_index
                    else temp_max_index
                )
                target_index += 1

            index = temp_max_index
            step += 1
        return step


test1 = [2, 3, 1, 1, 4]
test2 = [2, 3, 0, 1, 4]
test3 = [1, 2, 3]
test4 = [3, 4, 3, 2, 5, 4, 3]


print(Solution1().jump(test1))
print(Solution1().jump(test2))
print(Solution1().jump(test3))
print(Solution1().jump(test4))
