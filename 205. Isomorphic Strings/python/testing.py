class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        mydict = {}
        for index, s_char in enumerate(s):
            mydict.update({s_char: t[index]})
        result: str = ""
        for char in s:
            result = result + mydict[char]
        if result == t:
            return True
        return False


result = Solution().isIsomorphic(s="egg", t="add")
