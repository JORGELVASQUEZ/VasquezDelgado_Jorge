#hacer un programa que pida horas, minutos y segundos y las convierta a segundos

#solicita al usuario ingresar horas, minutos y segundos
horas = int(input("inmgresa las horas: "))
minutos = int(input("inmgresa los minutos: "))
segundos = int(input("inmgresa las segundos: "))

#convierte todo a segundos
conversionAsegundos = (horas *3600) + (minutos * 60) + (segundos * 1)
print("los segundos totales son: ", conversionAsegundos)

