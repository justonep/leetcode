#https://leetcode-cn.com/explore/interview/card/top-interview-questions-easy/1/array/22/

# 计算一下 差值为正 则相加即可
class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        result=0
        for i in range(1,len(prices)):
            if prices[i] >prices[i-1]:
                result+=prices[i]-prices[i-1]
        return result

nums=[7,1,5,3,6,4]
s=Solution()
print(s.maxProfit(nums))
