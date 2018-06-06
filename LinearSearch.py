li = list(input('Введите строку: '))
x = input('Введите искомый символ: ')

def search(li, x):
    length = len(li)
    for i in range(length):
       if li[i] == x:
            return 'Символ найден ' + str(i+1) + ' по счету!'
    return 'Символ не найден!'

print(search(li, x))