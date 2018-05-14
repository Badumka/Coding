monetki = [0, 0, 0, 0]
nominal = [50, 10, 5, 1]
summa = input('Сколько копеек нужно выдать сдачи: ')
s = int(summa)
print('Ваша сдача:')
length = len(nominal)
for i in range(length):
    while s >= nominal[i]:
        s -= nominal[i]
        monetki[i] += 1
    print(monetki[i], 'монетки по', nominal[i], 'копеек')
print('Спасибо за покупку! Приходите еще!')
