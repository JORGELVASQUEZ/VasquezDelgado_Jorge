#Pide al usuario ingresar 10 productos y almacenalos en una lista. Luego muestra la lista ordenada alfabeticamente.
productos = []
for i in range(10):
    producto = input("Ingresa el nombre del producto: ")
    productos.append(producto)
    productos.sort()

print("La lista de productos ordenada alfabeticamente es: ", productos)