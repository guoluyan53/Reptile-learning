def check_data(a):
    wordcount = {}
    for i in a:
        for j in i:
            if wordcount.get(j) == 1:
                return False
            wordcount[j] = wordcount.get(j, 0) + 1
    return True

b = [[1,2,3],[4,5,6],[7,8,9]]
print(check_data(b))