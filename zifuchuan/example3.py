class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s)!=len(t):
            return False
        for i in range(0,len(s)):
            print(s[i:] + s[:i])
            if s[i:]+s[:i]==t:
                return True
        return False

s=Solution()
result=s.isAnagram("anagram","nagaram")
print(result)