li = list(input('Введите строку: '))

def sort(li):
    for i in range(len(li)):
        min = i
        for j in range(i+1, len(li)):
            if li[j] < li[min]:
                min = j
        x = li[min]
        li[min] = li[i]
        li[i] = x
    return li

print(sort(li))