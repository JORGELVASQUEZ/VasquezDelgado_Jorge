#Haz un programa que pida dos numeros y muestre si el primero es mayor, menor o igual al segundo

num1 = int(input("ingresa el primer numero: "))
num2 = int(input("ingresa el segundo numero: "))

resultado = (num1 < num2)
resultado2 = (num1 > num2)
resultado3 = (num1 == num2)
print(f'¿el primer numero es mayor que el segundo? {resultado}')
print(f'¿el primer numero es menor que el segundo? {resultado2}')
print(f'¿el primer numero es igual que el segundo? {resultado3}')
