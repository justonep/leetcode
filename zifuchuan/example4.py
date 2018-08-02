class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return False
        dic1 = {}
        dic2 = {}
        for i in s:
            if i not in dic1.keys():
                dic1[i] = 1
            else:
                dic1[i] += 1
        for i in t:
            if i not in dic2.keys():
                dic2[i] = 1
            else:
                dic2[i] += 1
        if dic1 == dic2:
            return True
        else:
            return False
