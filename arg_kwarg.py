def multiply(*args):
    print(args[0])
    print(args[-1])
    print(len(args))
    for i in args:
        if i > 6:
            print(f'zarabia za duzo, bo az {i}')

multiply(5, 6, 7, 12, 1)


def welcome(**kwargs):
    if 'imie' in kwargs and 'nazwisko' in kwargs:
        print('Hello ',kwargs['imie'],kwargs['nazwisko'])
    elif 'imie' in kwargs:
        print('Hello ',kwargs['imie'])

welcome(imie='Kamil', nazwisko='Musial', wiek=34)
#sdgf