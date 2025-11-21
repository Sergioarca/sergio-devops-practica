# Práctica 02 - Tienda Online - GitHub
Sergio Arca Montenegro
# Mini Tienda Online en Python (POO)

Este proyecto es una simulación sencilla de una tienda online desarrollada en Python utilizando Programación Orientada a Objetos. Permite registrar usuarios (clientes y administradores), gestionar un catálogo de productos, manejar un carrito de compra y crear pedidos, actualizando el stock de los productos en cada compra. 

## Funcionalidades principales

- Registro de usuarios (clientes y administradores).
- Gestión de catálogo de productos (ropa, electrónica y productos genéricos).
- Carrito de la compra con control de stock.
- Creación de pedidos asociados a cada cliente.
- Cálculo automático del total de cada pedido.
- Listado de pedidos y consulta de pedidos por usuario. 

## Estructura del proyecto

- **`main.py`**  
  Script de ejemplo que crea la tienda, registra usuarios, añade productos al catálogo, simula varios pedidos y muestra por consola el catálogo, los pedidos y el stock actualizado tras las compras. 

- **`Producto.py`**  
  Define la clase base `Producto` y las subclases `ProductoElectronico` y `ProductoRopa`. Gestiona el identificador único de cada producto, su precio, el stock disponible y atributos específicos como garantía, talla o color.

- **`Usuario.py`**  
  Contiene la clase base `Usuario` y las subclases `Cliente` y `Administrador`. Permite diferenciar entre usuarios normales y administradores, añadiendo datos como el código postal en clientes y permisos especiales en administradores. 

- **`Pedido.py`**  
  Implementa la clase `Pedido`, que relaciona un cliente con una lista de productos (y sus cantidades), calcula el total del pedido y genera un resumen legible con fecha, cliente y detalle de líneas de compra.
  
- **`Tienda_service.py`**  
  Define la clase `TiendaService`, encargada de la lógica de negocio: gestión del catálogo, carrito, creación de pedidos, registro de usuarios, eliminación de productos por id y consulta del historial de pedidos por usuario. 

## Objetivo educativo

El proyecto está pensado como ejemplo didáctico para practicar:

- Programación Orientada a Objetos en Python.
- Herencia y composición entre clases.
- Gestión de listas de objetos (catálogo, carrito, pedidos, usuarios).
- Simulación de la lógica básica de una tienda online en consola.

## Docker

- Dockerfile
- requirements.txt  
- README.md
- Command para construir la imagen: docker build . -t tiendaonline
- Command para correr el contenedor: docker run -t tiendaonline