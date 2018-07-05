class Solution:
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        nums1=sorted(nums1)
        nums2=sorted(nums2)
        temp=[]
        i=0
        j=0
        while True:
            if i == len(nums1):
                break
            if j == len(nums2):
                break
            if nums1[i] == nums2[j]:
                temp.append(nums1[i])
                i+=1
                j+=1
            elif nums1[i] > nums2[j]:
                j+=1
            else:
                i+=1

        return temp

s=Solution()
s.intersect([1,2,2,1],[2,2])