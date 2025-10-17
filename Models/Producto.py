# Bibliotecas
import uuid

class Producto ():

    def __init__(self, nombre, precio, stock):
        self.id_unico = uuid.uuid4() # Genera el id único con la librería uuid
        self.nombre = nombre
        self.precio= precio
        self.__stock = stock # Atributo Privado

    # Extraer stock sin modificarlo
    def get_stock(self):
        return self.__stock
    
    # Actualizar stock en función de compras etc
    def set_stock(self, reposicion):
        if reposicion > self.__stock:
            self.__stock = reposicion

    def compra_stock(self, compra):
        if compra <= self.__stock:
            self.__stock -= compra
            return True
        else:
            print(f"No hay suficiente stock para el producto {self.name}, su stock es de: {self.get_stock()}")
            return False

    
    def __str__(self):
        return f"El producto {self.nombre} de id [{self.id_unico}], tiene un precio de {self.precio}€ y un stock de {self.get_stock()} stock"

class ProductoElectronico (Producto):
    def __init__(self, nombre, precio, stock, garantia):
        super().__init__(nombre, precio, stock)
        self.garantia = garantia
    
    def __str__(self):
        return f"Esta producto electrónico ({self.nombre}) de id [{self.id_unico}], con precio de {self.precio}€ y {self.get_stock()} stock, tiene una garantía de {self.garantia}"

class ProductoRopa (Producto):
    def __init__(self, nombre, precio, stock, talla, color):
        super().__init__(nombre, precio, stock)
        self.talla = talla
        self.color = color

    def __str__(self):
        return f"Esta ropa de nombre {self.nombre} de id [{self.id_unico}] , con precio de {self.precio}€ y stock {self.get_stock()} stock, tiene una talla {self.talla} y color {self.color}"
    
"""
Define la clase base Producto y sus subclases ProductoElectronico y ProductoRopa.
Gestiona el stock de los productos, su identificación única y sus características específicas.
Este archivo complementa el main.py permitiendo crear y manipular los diferentes productos
que se añaden al catálogo de la tienda.
"""
