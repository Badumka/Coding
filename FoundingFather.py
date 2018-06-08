fathers = {
    'Kenneth Eugene Iverson': 'APL',
    'Alfred Vaino Aho': 'AWK',
    'Roberto Ierusalimschy': 'Lua',
    'Tomas Eugene Kurtz': 'Basic',
    'John McCarthy': 'Lisp',
    'Niklaus Emil Wirth': 'Pascal',
    'Dennis MacAlistair Ritchie': 'C',
    'Don Syme': 'F Sharp',
    'Bjarne Stroustrup': 'C++',
    'Jeremy Ashkenas': 'CoffeeScript',
    'Walter Bright': 'D',
    'Don Woods': 'Intercal',
    'Barbara Liskov': 'Clu',
    'Seymour Papert': 'Logo',
    'Ole-Johan Dahl': 'Simula',
    'Rodrigo Barreto de Oliveira': 'Boo',
    'Rich Hickey': 'Clojure',
    'John Warner Backus': 'Fortran',
    'Guido van Rossum': 'Pyton',
    'Slava Pestrov': 'Factor',
    'James Gosling': 'Java',
    'Yukihiro Matsumoto': 'Ruby',
    'Paul Graham': 'Lisp',
    'Larry Wall': 'Perl',
    'Xavier Leroy': 'OCaml',
    'Jean David Ichbian': 'Ada',
    'Grace Hopper': 'Cobol',
    'Alan Curtis Kay': 'Smalltalk',
    'John Ousterhout': 'Tcl & Tk',
    'Charles H. Moore': 'Forth',
    'Bertrand Meyer': 'Eiffel'
}

print('Список всех имен:')
for names in fathers:
    print(names + ' — ' + fathers[names])

print('')
print('')

print('Что вы хотите сделать?')
print('Введите «sorted» для сортировки')
print('Введите «search» для поиска имени')
choose = input('Введите кодовое слово: ')
print()
if choose == 'search':
    poisk = input('Введите нужное имя для поиска: ')
    for names, value in fathers.items():
        if names == poisk:
           print(poisk + ' создал язык програмирования: ' + fathers[names] + '!')
           break
        else:
           print('Идет поиск... Или вы неверно ввели имя.')
elif choose == 'sorted':
     sort = sorted(fathers)
     for names in sort:
        print(names + ' — ' + fathers[names])

else:
    print('Вы неверно ввели команду. Попробуйте еще раз.')

print('')
print('Спасибо за пользование словаря. Ищите еще!')

