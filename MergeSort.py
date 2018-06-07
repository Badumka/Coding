li = list(input('Введите строку: '))

def sort(li):
    #print("Разделение: ", li)
    if len(li)>1:
        mid = len(li) // 2
        leH = li[:mid]
        riH = li[mid:]

        sort(leH)
        sort(riH)

        a = 0
        b = 0
        c = 0
        while a < len(leH) and b < len(riH):
            if leH[a] < riH[b]:
                li[c] = leH[a]
                a = a+1
            else:
                li[c] = riH[b]
                b = b+1
            c = c+1

        while a < len(leH):
            li[c] = leH[a]
            a = a+1
            c = c+1

        while b < len(riH):
            li[c] = riH[b]
            b = b+1
            c = c+1
    #print("Соединение: ", li)

sort(li)
print(li)