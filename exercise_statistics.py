def statistics():
    """
    Ejercicio 5 - Estadísticas Simples

    Dados cuatro números, calcular e imprimir:
    1. El promedio
    2. El máximo
    3. El mínimo
    4. El rango (diferencia entre máximo y mínimo)
    """
    num1 = 15
    num2 = 8
    num3 = 23
    num4 = 12

    numbers= [15,8,23,12]

    print((num1+num2+num3+num4)/4)

    max_numbers=max(numbers)

    print(max_numbers)

    min_numbers=min(numbers)

    print(min_numbers)

    range_numbers=max_numbers-min_numbers

    print(range_numbers)


#statistics()