# https://leetcode-cn.com/explore/interview/card/top-interview-questions-easy/1/array/21/


class Solution:
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 0
        j = 1
        for i in range(1, len(nums)):
            if nums[i] != nums[i - 1]:
                nums[j] = nums[i]
                j = j + 1
        return j


s = Solution()
nums = [1, 2, 3, 3, 4]
s.removeDuplicates(nums)
print(nums)
