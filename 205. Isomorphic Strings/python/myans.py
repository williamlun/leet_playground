class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        mydict1 = {}
        mydict2 = {}
        for i in range(len(s)):
            if s[i] in mydict1 and mydict1[s[i]] != t[i]:
                return False
            mydict1.update({s[i]: t[i]})
            if t[i] in mydict2 and mydict2[t[i]] != s[i]:
                return False
            mydict2.update({t[i]: s[i]})
        return True

    def isIsomorphic2(self, s: str, t: str) -> bool:
        mydict = {}
        for index, s_char in enumerate(s):
            if s_char in mydict and mydict[s_char] != t[index]:
                return False
            mydict.update({s_char: t[index]})
        mydict = {}
        for index, t_char in enumerate(t):
            if t_char in mydict and mydict[t_char] != s[index]:
                return False
            mydict.update({t_char: s[index]})
        return True


result = Solution().isIsomorphic(s="badc", t="baba")
print(result)


result = Solution().isIsomorphic(s="egg", t="add")
print(result)

result = Solution().isIsomorphic(s="foo", t="bar")
print(result)

result = Solution().isIsomorphic(s="paper", t="title")
print(result)
