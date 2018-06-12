abc = 'aбвгдеёждзийклмнопрстуфхцчшщъьэюя'
txt = input('Введите строку на русском языке: ').lower()
x = input('Введите слово ключ: ')

cipher = ''
cipherArray = []

for i in txt:
    if i not in abc:
        cipherArray.append(i)
    else:
        cipherArray.append(abc[(abc.index(i) + len(x)) % len(abc)])
for i in range(len(cipherArray)):
    cipher += cipherArray[i]
print('Ваш шифр: ' + cipher)