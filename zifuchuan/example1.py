class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        if -10<x<10:
            return x
        x = str(x)
        if x[0] == '-':
            x=int('-'+x[::-1][:-1])
        else:
            x=int(x[::-1])

        if not (-2147483648 < x < 2147483647):
            return 0
        return x
s=Solution()
result=s.reverse('-123121')
print result