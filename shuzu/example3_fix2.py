class Solution:
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        # i ->  (i+k)%len(nums)
        # temp=[]
        # for i in nums:
        #     temp.append(i)
        # for i in range(0,len(nums)):
        #     temp[(i+k)%len(nums)]=nums[i]
        # print(temp)
        # k=k+1
        # for i in range(0,len(nums)-k):
        #     if i<(len(nums)-k)/2:
        #         nums[i],nums[len(nums)-k-i]=nums[len(nums)-k-i], nums[i]
        #
        # for j in range(i,len(nums)):
        #     if j<((len(nums)+i)/2):
        #         # nums[j],nums[len(nums)-j+k]=nums[len(nums)-j+k],nums[j]
        #         print('hi')
        # print(nums)

        k=k%len(nums)
        k=k+1
        for i in range(0,len(nums)-k):
            if i<(len(nums)-k)/2:
                nums[i],nums[len(nums)-k-i]=nums[len(nums)-k-i],nums[i]

        # print(nums)

        for j in range(len(nums)-k+1,len(nums)):
            if j<(len(nums)-k/2):
                nums[j],nums[2*len(nums)-j-k]=nums[2*len(nums)-j-k],nums[j]

        # print(nums)


        for p in range(0,len(nums)-1):
            if p<len(nums)/2:
                nums[p],nums[len(nums)-1-p]=nums[len(nums)-1-p],nums[p]

        # print(nums)

s=Solution()
nums=[0,1,2,3,4,5,6,7,8,9]
s.rotate(nums,3)