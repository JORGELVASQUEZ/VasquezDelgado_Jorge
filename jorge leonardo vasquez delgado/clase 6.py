#for variable in terable:
#      bloque de codigo


# funcion range(inicio, fin, paso)

for i in range(0, 11, 2):
    print(i)


    #Ejercicio 1: haz un programa que muestre los numeros del 1 al 20
    print("Numeros del 1 al 20:")
    for numero in range(1, 21):
        print(numero)

#Ejercicio 2: haz un programa que muestre la tabla de multiplicar de un numero dado por el usuario (del 1 al 10)

numero_usuario = int(input("Introduce un numero: "))
print(f"Tabla de multiplicar del {numero_usuario}: ")
print("________________________________")
for i in range(1, 11):
    resultado = numero_usuario * i
    print(f'{numero_usuario} x {i} = {resultado}')
    print("● █▀█▄ Ɑ͞ ̶͞ ̶͞ ̶͞ لں͞!")
print("________________________________")