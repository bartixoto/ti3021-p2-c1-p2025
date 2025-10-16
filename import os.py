import os

class producto:

    def __init__(self,nombre,stock):
        self.nombre: str = nombre
        self.stock: str = stock

    def __str__(self):
        return f"{self.nombre} {self.stock}"
    
inventario = []

def agregarProducto():
    nombre = input("Ingrese el nombre del producto")
    stockInicial = int (input("Ingrese el stock inicial: "))
    prducto: producto = producto(nombre=nombre, stock=stockInicial)
    inventario.append (producto)

def listarProducto():
    for producto in inventario:
        print(producto)

while True:
    print("1. Listar Inventario\n2. Crear Producto\n3. Salir")
    opcion = int (input("Ingrese una opcion [1-3]: "))
    if opcion == 1:
        os.system("cls")
        listarProducto()
    elif opcion == 2:
        os.system("cls")
        agregarProducto() 
               