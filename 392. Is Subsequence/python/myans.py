class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        index = 0
        for char in s:
            tar = t.find(char)
            if tar == -1:
                return False
            index = tar
            t = t[index + 1 :]

        return True


result = Solution().isSubsequence(s="abc", t="ahbgdc")
print(result)

result = Solution().isSubsequence(s="axc", t="ahbgdc")
print(result)

result = Solution().isSubsequence(s="ab", t="baab")
print(result)

result = Solution().isSubsequence(
    s="twn",
    t="xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxtxxxxxxxxxxxxxxxxxxxxwxxxxxxxxxxxxxxxxxxxxxxxxxn",
)
print(result)
