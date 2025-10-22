#haz un programa que solicite al usuario la base y la altura de un rectangulo y calcula su area y perimetro

base = int(input("ingresa la base de tu rectangulo: "))
altura = int(input("ingresa la altura de tu rectangulo : "))

area = (base * altura)
perimetro = ((base + altura) * 2)

print(f'el area del rectangulo es: {area}')
print(f'el perimetro del rectangulo es: {perimetro}')