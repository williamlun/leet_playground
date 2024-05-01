class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
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


print(Solution().isAnagram("anagram", "nagaram"))
print(Solution().isAnagram("rat", "car"))
