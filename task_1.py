def interaction():
    array_n = []
    array_result = []
    

    n = int(input('Введите кол-во элементов первого множества: '))
    m = int(input('Введите кол-во элементов второго множества: '))

    for i in range(0, n):
        num = int(input('Введите элемент первого множества: '))
        array_n.append(num)
    
    set_n = set(array_n)

    for j in range(0, m):
        num = int(input('Введите элемент второго множества: '))
        if (num in set_n):
            array_result.append(num)

    array_result.sort()
    print(array_result)

interaction()