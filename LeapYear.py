print('Для старта программы нажмите любую клавишу или "выход" для завершения работы')
year = input()

while True:
    year = input('Введите год')
    if year == 'выход':
        break
    else:
        year = int(year)
        if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
            print('Год високосный')
        else:
            print('Год не является високосным')
print('Программа завершена')
