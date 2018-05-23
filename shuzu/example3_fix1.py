class Solution:
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        # i ->  (i+k)%len(nums)
        temp=[]
        for i in nums:
            temp.append(i)
        for i in range(0,len(nums)):
            temp[(i+k)%len(nums)]=nums[i]
        print(temp)

s=Solution()
nums=[1,2,3,4,5,6,7,8,9]
s.rotate(nums,3)