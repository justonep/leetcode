nums=[]
if nums == []:
    print(-1)
    exit()
target = 9
temp={}
temp[nums[0]]=0



for i in range(1,len(nums)):
    if target - nums[i] in temp.keys():
        print([temp[target - nums[i]],i])
        exit()
    else:
        temp[nums[i]]=i

print(-1)