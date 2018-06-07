li = list(input('Введите строку: '))

def sort(li):
    for i in range(len(li)):
        x = li[i]
        j = i
        while (li[j - 1] > x) and (j > 0):
            li[j] = li[j - 1]
            j = j - 1
        li[j] = x
        #print(li)
    return li

print(sort(li))