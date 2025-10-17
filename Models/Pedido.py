import uuid
import datetime
from Models.Usuario import Cliente
from Models.Producto import Producto

class Pedido:
    def __init__(self, cliente: Cliente, lista_productos: list):
        self.id_pedido = uuid.uuid4()
        self.fecha = datetime.datetime.now()
        self.cliente = cliente
        self.lista_productos = lista_productos

    def calcular_total(self):
        total = 0
        for producto, cantidad in self.lista_productos:
            total += (producto.precio * cantidad)
        return total

    def __str__(self):
        productos_str = ""
        for producto, cantidad in self.lista_productos:
            productos_str += f"- {producto.nombre} x {cantidad} = {producto.precio * cantidad}€\n"

        if not productos_str:
            productos_str = "No hay productos en este pedido\n"

        return (
            f"Pedido [{self.id_pedido}]\n"
            f"Cliente: {self.cliente.name}\n"
            f"Fecha: {self.fecha.strftime('%d/%m/%Y %H:%M:%S')}\n"
            f"Productos:\n{productos_str}"
            f"Total: {self.calcular_total()}€"
        )

"""
Implementa la clase Pedido, que relaciona un cliente con una lista de productos y cantidades.
Permite calcular el total de la compra y mostrar un resumen del pedido en texto legible.
Este archivo complementa el main.py proporcionando la estructura necesaria para crear pedidos
y mostrar su información junto con el stock actualizado de los productos.
"""
