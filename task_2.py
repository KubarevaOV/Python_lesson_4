def interaction():
    gryadka = [1,2,3,4]
    max_yagod = 0

    n = int(input('Введите номер куста: '))

    current_kust = n - 2 if n - 2 >= 0 else len(gryadka)-1
    prev_kust = current_kust - 1 if current_kust - 1 >= 0 else len(gryadka)-1
    next_kust = n - 1

    max_yagod = gryadka[current_kust] + gryadka[prev_kust] + gryadka[next_kust]
    print(max_yagod)

interaction()