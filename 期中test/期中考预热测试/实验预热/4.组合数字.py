#在指定位置编写代码，完成函数，根据给定的数字，给出组成该数字的所有单个数字
#排列构成的数字，例如字符串为123时，结果为123,132,213,231,312,321
def zuhe(num):
    ls = [eval(i) for i in num]
    lt = []

    def dfs(cur, lst):
        if len(cur) == len(ls):
            num = int("".join(cur))
            lt.append(num)
            return
        for i in lst:
            if str(i) in cur:
                continue
            cur.append(str(i))
            dfs(cur, lst)
            cur.pop(-1)

    dfs([], ls)
    print(lt)

nums='3456'
zuhe(nums)