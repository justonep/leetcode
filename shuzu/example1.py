# https://leetcode-cn.com/explore/interview/card/top-interview-questions-easy/1/array/21/


# 本题的解决思路就是 构造两个指针 一个标明实际位置 一个用来遍历整个数组 具体算法如下
class Solution:
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        #如果数组的长度为0 返回0
        if len(nums) == 0:
            return 0
        # 设立两个变量 一个i 一个j 同时指向第2个数
        # 假设有 nums = [1,2,3,3,3,4,4,5] 现在  i,j==1,nums[i],nums[j] == 2
        # nums[1] != nums[0]   nums[1]=nums[1]    |   i+=1 i=2, j+=1 j=2
        # nums[2] != nums[1]   nums[2]=nums[2]    |   i+=1 i=3, j+=1 j=3
        # nums[3] == nums[2]                      |   i+=1 i=4, j=3
        # nums[4] == nums[3]                      |   i+=1 i=5, j=3
        # nums[5] != nums[4]   nums[3]=nums[5]    |   i+=1 i=6, j=4
        # nums[6] == nums[5]                      |   i+=1 i=7, j=5
        # nums[7] != nums[6]   nums[5]=nums[7]    |   i+=1 i=8结束该循环
        j = 1
        for i in range(1, len(nums)):
            if nums[i] != nums[i - 1]:
                nums[j] = nums[i]
                j = j + 1

        print(j)


s = Solution()
nums = [1,2,3,3,3,4,4,5]
s.removeDuplicates(nums)
print(nums)
