li = list(input('Введите строку: '))
x = input('Введите искомый символ: ')

def search(li, x):
    l = 0
    r = len(li)-1
    m = (l + r) // 2
    while li[m] != x and l < r:
        if x > li[m]:
            l = m + 1
        else:
            r = m - 1
        m = int((l + r) / 2)
    if l > r:
        return 'Символ не найден!'
    else:
        return 'Символ найден ' + m + ' по счету!'

print(search(li, x))