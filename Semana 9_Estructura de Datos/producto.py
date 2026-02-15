# Clase Producto
# Esta clase representa un producto individual en nuestra tienda

class Producto:
    # Constructor: método que se ejecuta cuando creamos un nuevo producto
    def __init__(self, id, nombre, cantidad, precio):
        """
        Inicializa un nuevo producto con sus datos básicos
        id: número único para identificar el producto
        nombre: nombre del producto (ej: "Manzanas")
        cantidad: cuántos productos tenemos en stock
        precio: precio unitario del producto
        """
        self.id = id
        self.nombre = nombre
        self.cantidad = cantidad
        self.precio = precio
    
    # Métodos getter: permiten obtener los valores de los atributos
    def get_id(self):
        return self.id
    
    def get_nombre(self):
        return self.nombre
    
    def get_cantidad(self):
        return self.cantidad
    
    def get_precio(self):
        return self.precio
    
    # Métodos setter: permiten cambiar los valores de los atributos
    def set_nombre(self, nombre):
        self.nombre = nombre
    
    def set_cantidad(self, cantidad):
        self.cantidad = cantidad
    
    def set_precio(self, precio):
        self.precio = precio
    
    # Método especial para mostrar el producto de forma legible
    def __str__(self):
        """
        Retorna una representación del producto en texto
        Esto hace más fácil imprimir la información del producto
        """
        return f"ID: {self.id} | Nombre: {self.nombre} | Cantidad: {self.cantidad} | Precio: ${self.precio:.2f}"
