#Bibliotecas
import uuid

# Usuario
class Usuario():
    def __init__(self, name, email ):
        self.id_usuario = uuid.uuid4()
        self.name = name
        self.email = email
    
    def is_admin(self):
        return False

# Hija Cliente
class Cliente (Usuario):
    def __init__(self, name, email, postcode):
        super().__init__(name, email)
        self.postcode = postcode

# Hija Admin
class Administrador (Usuario):
    def __init__(self, name, email):
        super().__init__(name, email)

    def is_admin(self):
        return True

"""
Contiene la clase base Usuario y las subclases Cliente y Administrador.
Permite diferenciar entre usuarios normales y administradores de la tienda,
añadiendo la dirección postal en clientes y permisos especiales en administradores.
Este archivo complementa el main.py ya que permite registrar los distintos usuarios
que luego pueden interactuar con la tienda y generar pedidos.
"""