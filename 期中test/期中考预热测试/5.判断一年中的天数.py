# 5.	问题：输入某年某月某日，判断这一天是这一年的第几天？例如：
# # 3月5日，应该先把
# # 前两个月的天数加起来，然后再加上5天

import datetime
def func(year,month,day):
    date = datetime.date(year,month,day)
    return date.strftime('%j')  #%j十进制表示的每年的第几天


if __name__ == '__main__':
    y = int(input('请输入年份：'))
    m = int(input('请输入月份：'))
    d = int(input('请输入日：'))
    print(func(y,m,d))
