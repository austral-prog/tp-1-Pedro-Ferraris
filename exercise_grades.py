def grades():
    """
    Ejercicio 11 - Promedio de Calificaciones

    Dadas tres notas, calcular e imprimir:
    1. El promedio de las tres notas
    2. La nota máxima
    3. La nota mínima
    4. Cuántos puntos faltan del promedio a 10
    """
    nota1 = 8
    nota2 = 7
    nota3 = 9

    notas=[8,7,9]
    promedio=(8+7+9)/3
    nota_max=max(notas)
    nota_min=min(notas)
    dif_10=10-promedio


    print(promedio)
    print(nota_max)
    print(nota_min)
    print(dif_10)

#grades()