#Haz un programa que pida al usuario dos numeros y muestre su suma, resta, multiplicación y división

num1 = int(input("ingresa el primer numero: "))
num2 = int(input("ingresa el segundo numero: "))

suma = (num1 + num2)
resta = (num1 - num2)
multiplicacion = (num1 * num2)
division = (num1 / num2)

print(f'la suma de los dos numeros es: {suma}')
print(f'la resta los dos numeros es: {resta}')
print(f'la multiplicación de los dos numeros es: {multiplicacion}')
print(f'la división de los dos numeros es: {division}')