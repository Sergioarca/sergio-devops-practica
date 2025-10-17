from Models.Producto import Producto
from Models.Usuario import Cliente, Administrador, Usuario
import Models.Usuario
from Models.Pedido import Pedido

class TiendaService:
    def __init__(self):
        self.catalogo = []
        self.carrito = []
        self.pedidos = []
        self.usuarios = []    

    def agregar_producto_catalogo(self, producto: Producto):
        self.catalogo.append(producto)

    def agregar_producto_al_carrito(self, producto: Producto, cantidad: int):
        if producto.compra_stock(cantidad):
            self.carrito.append((producto, cantidad))
        else:
            print(f"No se pudo añadir {cantidad} x {producto.name} al carrito")


    def crear_pedido(self, cliente: Cliente) -> Pedido:
        pedido = Pedido(cliente,self.carrito.copy())
        self.pedidos.append(pedido)
        self.carrito.clear()  # vaciar carrito tras compra
        return pedido

    def mostrar_catalogo(self):
        print("Catálogo de productos:")
        for producto in self.catalogo:
            print(producto)

    def mostrar_pedidos(self):
        for pedido in self.pedidos:
            print(pedido,"\n")
    
    def registrar_usuario(self, usuario: Usuario):
        self.usuarios.append(usuario)
        print(f"Usuario registrado: {usuario.name} ({'Admin' if usuario.is_admin() else 'Cliente'})")
        return usuario
    
    def eliminar_producto(self, id_producto):
        self.id_producto = id_producto
        for i in self.catalogo:
            if Producto.id_unico == (self.id_producto):
                self.catalogo.remove(Producto)
            print(f"Producto eliminado: {Producto.nombre} (ID: {Producto.id_unico})")
            return True
        
        print(f"No se encontró producto con ID {id_producto}")
        return False

    def pedidos_por_usuario(self, id_usuario):
        """Lista todos los pedidos de un usuario (filtrados por id_usuario) ordenados por fecha"""
        pedidos_usuario = [pedido for pedido in self.pedidos if pedido.cliente.id_usuario == id_usuario]
        pedidos_usuario.sort(key=lambda p: p.fecha)  # orden por fecha ascendente

        if not pedidos_usuario:
            print(f"No hay pedidos registrados para el usuario con ID {id_usuario}")
            return []

        print(f"\nTodos los pedidos del usuario {pedidos_usuario[0].cliente.name}:")
        for pedido in pedidos_usuario:
            print(pedido)

        return pedidos_usuario

"""
Define la clase TiendaService, que actúa como capa de servicios centralizada.
Permite registrar usuarios, gestionar el catálogo, eliminar productos por id, manejar el carrito
y crear pedidos verificando usuarios y stock disponible.
Además, permite mostrar el catálogo, los pedidos y el historial de pedidos de cada cliente.
Este archivo complementa el main.py gestionando toda la lógica de negocio de la tienda,
mientras que main.py se limita a probar su funcionamiento.
"""

