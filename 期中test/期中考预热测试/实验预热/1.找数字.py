#给定一个无序列表，列表中元素均为不重复的整数。请找出列表中有没有比它前面都小，
#比它后面都大的数，如果不存在则返回-1，存在则显示索引
def find(nums):
    if len(nums)<1:
        return -1
    res=[]
    for i in range(len(nums)):
        left_min = min(nums[:i+1])
        right_max = max(nums[i:])
        if nums[i] <=left_min and nums[i] >=right_max:
            res.append(i)
    if res:
        return res
    else:
        return -1

nums = [23,34,11,10,3,7,1,8]
print(find(nums))