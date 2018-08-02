class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if (len(s) == 0) or (len(s) == 1):
            return True
        import re
        s = re.sub('[^a-zA-Z0-9]', '', s.lower())
        return s == s[::-1]

