from typing import List


class Solution:
    def hIndex(self, citations: List[int]) -> int:
        citations.sort(reverse=True)
        h_index = 0
        for i in range(len(citations)):
            if i + 1 <= citations[i]:
                h_index = i + 1
        return h_index


test1 = [3, 0, 6, 1, 5]
test2 = [1, 3, 1]
test3 = [1, 2]
test4 = [0, 1]

print(Solution().hIndex(test1))
print(Solution().hIndex(test2))
print(Solution().hIndex(test3))
print(Solution().hIndex(test4))
