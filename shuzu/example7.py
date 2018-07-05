class Solution:
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        digits=list(reversed(digits))
        len_digits=len(digits)
        flag=0
        while True:
            if flag==len_digits:
                digits.append(0)
            if digits[flag] == 9:
                digits[flag]=0
                flag+=1
            else:
                digits[flag]=digits[flag]+1
                break
        return list(reversed(digits))

s=Solution()
result=s.plusOne([9,9,9,9])
print(result)