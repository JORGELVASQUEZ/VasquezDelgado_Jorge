#funcion en phyton

#definicion
def saludar():
    print("Hola, bienvenido a la clase de python")

#llamada a la funcion
saludar()

saludar()  #puedes llamar a la funcion varias veces

saludar()

#funcion con parametros
def saludar_persona(nombre, apellido, edad):
    print(f"Hola, {nombre} {apellido}, bienvenido a la clase de python. Tienes {edad} años.")

#llamada a la funcion con parametros
saludar_persona("Jorge", "Vasquez", 19)
saludar_persona("Ana", "Lopez", 22)
saludar_persona("Luis", "Martinez", 20)

#funciom con valor de retorno
def sumar(a, b):
    return a + b
print(sumar(5, 10))
resultado = sumar(15, 25)
print(f"El resultado de la suma es: {resultado}")