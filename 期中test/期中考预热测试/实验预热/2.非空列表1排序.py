#给定一个非空列表figs，请将figs中所有1移动到列表的末尾，
#同时保持非1元素的相对顺序
arr = []
arr1 = []
arr2 = []
def pailie(list):
    for i in list:
        if i==1:
            arr1.append(i)
        else:
            arr2.append(i)
    arr = arr2 + arr1
    return arr

nums = [2,55,1,2,1,1,6,7,1]
print(pailie(nums))