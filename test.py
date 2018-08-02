# coding=utf-8
# 最小子树

def get(nums):
    start=nums[0]
    result=nums[0]
    for i in range(1,len(nums)):
        if start>0:
            start=start+nums[i]
            result=start
        else:
            start=nums[i]

    return result

result=get([-1,1,2,3,4,-5,6,7])
print(result)