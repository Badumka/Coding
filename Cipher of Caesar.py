abc = 'aбвгдеёждзийклмнопрстуфхцчшщъьэюя'
txt = input('Введите строку на русском языке: ').lower()
x = int(input('Введите число сдвига: '))

cipher = ''
cipherArray = []

for i in txt:
    if i not in abc:
        cipherArray.append(i)
    else:
        cipherArray.append(abc[abc.index(i) + x])
for i in range(len(cipherArray)):
    cipher += cipherArray[i]
print('Ваш шифр: ' + cipher)