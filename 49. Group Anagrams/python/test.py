from typing import List


def isAnagram(s: str, t: str) -> bool:
    seen = {}
    for char in s:
        seen[char] = seen.get(char, 0) + 1
    for char in t:
        if char not in seen:
            return False
        seen[char] -= 1
        if seen[char] == 0:
            del seen[char]
    return len(seen) == 0


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans = []
        while len(strs) > 0:
            target = strs.pop(0)
            temp = [target]
            for str in strs[:]:
                if isAnagram(target, str):
                    temp.append(str)
                    strs.remove(str)
            ans.append(temp)
        return ans


print("Sol1")
print(Solution().groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))
print(Solution().groupAnagrams([""]))
print(Solution().groupAnagrams(["a"]))


class Solution2:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans = {}
        for str in strs:
            key = "".join(sorted(str))
            if key not in ans:
                ans[key] = [str]
            else:
                ans[key].append(str)
        return list(ans.values())


print("Sol2")
print(Solution2().groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))
print(Solution2().groupAnagrams([""]))
print(Solution2().groupAnagrams(["a"]))
