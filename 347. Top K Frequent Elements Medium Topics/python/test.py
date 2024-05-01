from typing import List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        for num in nums:
            if num in count:
                count[num] = count.get(num, 0) + 1
            else:
                count[num] = 1
        needed = sorted(list(count.values()), reverse=True)[:k]
        return [key for key in count.keys() if count[key] in needed]


print("Sol1")


# print(Solution().topKFrequent([1, 1, 1, 2, 2, 3], 2))
# print(Solution().topKFrequent([1], 1))
# print(Solution().topKFrequent([1, 2], 2))
# print(Solution().topKFrequent([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 10))
# print(Solution().topKFrequent([1, 1, 1, 1, 1, 1, 1, 1, 1, 1], 1))


# def test():
#     test = {"a": 2, "b": 3, "c": 4, "d": 5, "e": 6}
#     list_of_v = list(test.values())
#     c = sorted(list_of_v, reverse=True)
#     needed = c[:2]
#     my_key = [key for key in test.keys() if test[key] in needed]
#     print(my_key)


# test()


class Solution2:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        for num in nums:
            if num in count:
                count[num] = count.get(num, 0) + 1
            else:
                count[num] = 1
        for key, value in count.items():
            ans[value] = key


print("Sol2")


print(Solution2().topKFrequent([1, 1, 1, 2, 2, 3], 2))
print(Solution2().topKFrequent([1], 1))
print(Solution2().topKFrequent([1, 2], 2))
print(Solution2().topKFrequent([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 10))
print(Solution2().topKFrequent([1, 1, 1, 1, 1, 1, 1, 1, 1, 1], 1))
