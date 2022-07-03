# Bucles [Python]
# Ejercicios de práctica

# Autor: Inove Coding School
# Version: 2.0

# IMPORTANTE: NO borrar los comentarios
# que aparecen en verde con el hashtag "#"

# Ejercicios con bucles "while"

x = 0
# Dado el siguiente "while", complete la condicion
# para que el "while" itere siempre que <x sea menor a 6>
# Además, complete la línea de código necesaria para que
# el valor de "x" incremente "1" en cada iteración
condicion = False

# reemplace "condicion" por lo que crea necesario
while x < 6:    
    print("Valor de x =", x)
    x += 1
    
print('terminó el bucle while')


    # Coloque la línea de código para que "x" incremente "1"

valor_maximo = 10
x = 5
# Dado el siguiente "while", complete la condicion
# para que el "while" itere siempre que <x sea mayor o igual a 0>
# Además, complete la línea de código necesaria para que
# el valor de "x" decremente "1" en cada iteración

while x < valor_maximo:
    if x == 9:
        print('Bucle interrumpido en x=', x)
        break

    print('Valor x=', x)
    x += 1



