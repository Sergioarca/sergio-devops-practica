from Models.Producto import Producto, ProductoElectronico, ProductoRopa
from Models.Usuario import Cliente, Administrador
from Services.Tienda_service import TiendaService

# Instanciar tienda
tienda = TiendaService()

# Crear clientes y admin
cliente1 = Cliente("Alberto", "alberto@gmail.com", 36211)
cliente2 = Cliente("Juan", "juan@gmail.com", 36201)
cliente3 = Cliente("Bartolo", "bartolo@gmail.com", 36270)
admin1 = Administrador("Eustaquio", "eustaquio@tiendaservice.admin")

# Registrar usuarios en la tienda
tienda.registrar_usuario(cliente1)
tienda.registrar_usuario(cliente2)
tienda.registrar_usuario(cliente3)
tienda.registrar_usuario(admin1)

print("\n") # Para correcta visualización en terminal

# Crear productos y agregarlos al catálogo
producto1 = ProductoRopa("Camiseta", 29.99, 50, "M", "White")
producto2 = ProductoElectronico("Portátil", 256.32, 20, 12)
producto3 = ProductoRopa("Pantalón Vaquero", 57.34, 15, "L", "Blue")
producto4 = ProductoElectronico("Cascos", 99.97, 34, 12)
producto5 = Producto("Libro", 15.60, 20)

tienda.agregar_producto_catalogo(producto1) 
tienda.agregar_producto_catalogo(producto2)
tienda.agregar_producto_catalogo(producto3)
tienda.agregar_producto_catalogo(producto4)
tienda.agregar_producto_catalogo(producto5)

tienda.mostrar_catalogo()

print("\n") # Para correcta visualización en terminal

# Pedido 1
tienda.agregar_producto_al_carrito(producto1, 2)
tienda.agregar_producto_al_carrito(producto2, 1)
pedido1 = tienda.crear_pedido(cliente1)

# Pedido 2
tienda.agregar_producto_al_carrito(producto3, 1)
tienda.agregar_producto_al_carrito(producto5, 3)
pedido2 = tienda.crear_pedido(cliente2)

# Pedido 3
tienda.agregar_producto_al_carrito(producto4, 2)
pedido3 = tienda.crear_pedido(cliente3)

print("PEDIDOS: \n")
# Mostrar todos los pedidos
tienda.mostrar_pedidos()

print("\nStock actualizado después del Pedido 1:")
print(f"- {producto1.nombre}: {producto1.get_stock()} de stock")
print(f"- {producto2.nombre}: {producto2.get_stock()} de stock")
print(f"- {producto3.nombre}: {producto3.get_stock()} de stock")
print(f"- {producto4.nombre}: {producto4.get_stock()} de stock")
print(f"- {producto5.nombre}: {producto5.get_stock()} de stock")

tienda.pedidos_por_usuario(cliente1.id_usuario)

"""
Crea una instancia de TiendaService, registra usuarios y administradores, 
añade productos al catálogo, simula varios pedidos y muestra en consola 
los resultados de cada pedido junto con el stock actualizado.
Este archivo utiliza todas las clases definidas en Producto.py, Usuario.py, Pedido.py 
y los métodos de Tienda_service.py para demostrar que el sistema de la tienda online funciona.
"""
