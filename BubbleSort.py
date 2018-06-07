li = list(input('Введите строку: '))

def sort(li):
    for i in range(len(li),0,-1):
        for j in range(1, i):
            if li[j-1] > li[j]:
                x = li[j-1]
                li[j-1] = li[j]
                li[j] = x
                #print(li)
    return li

print(sort(li))