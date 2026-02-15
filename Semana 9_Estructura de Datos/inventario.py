# Importamos la clase Producto del archivo producto.py
from producto import Producto

# Clase Inventario
# Esta clase maneja la colección de todos los productos de la tienda

class Inventario:
    def __init__(self):
        """
        Inicializa el inventario con una lista vacía de productos
        """
        self.productos = []  # Lista que almacenará todos los productos
    
    def añadir_producto(self, producto):
        """
        Añade un nuevo producto al inventario
        Verifica que el ID sea único antes de añadirlo
        """
        # Revisamos si ya existe un producto con ese ID
        for p in self.productos:
            if p.get_id() == producto.get_id():
                print(f"⚠️  Error: Ya existe un producto con el ID {producto.get_id()}")
                return False
        
        # Si el ID es único, añadimos el producto
        self.productos.append(producto)
        print(f"✅ Producto '{producto.get_nombre()}' añadido exitosamente")
        return True
    
    def eliminar_producto(self, id):
        """
        Elimina un producto del inventario usando su ID
        """
        # Buscamos el producto con ese ID
        for i, producto in enumerate(self.productos):
            if producto.get_id() == id:
                nombre = producto.get_nombre()
                self.productos.pop(i)  # Eliminamos el producto de la lista
                print(f"✅ Producto '{nombre}' eliminado exitosamente")
                return True
        
        # Si no encontramos el producto
        print(f"⚠️  Error: No se encontró un producto con el ID {id}")
        return False
    
    def actualizar_producto(self, id, nueva_cantidad=None, nuevo_precio=None):
        """
        Actualiza la cantidad o precio de un producto
        id: ID del producto a actualizar
        nueva_cantidad: nueva cantidad en stock (opcional)
        nuevo_precio: nuevo precio (opcional)
        """
        # Buscamos el producto
        for producto in self.productos:
            if producto.get_id() == id:
                # Actualizamos solo lo que se proporcionó
                if nueva_cantidad is not None:
                    producto.set_cantidad(nueva_cantidad)
                    print(f"✅ Cantidad actualizada a {nueva_cantidad}")
                
                if nuevo_precio is not None:
                    producto.set_precio(nuevo_precio)
                    print(f"✅ Precio actualizado a ${nuevo_precio:.2f}")
                
                return True
        
        # Si no encontramos el producto
        print(f"⚠️  Error: No se encontró un producto con el ID {id}")
        return False
    
    def buscar_por_nombre(self, nombre):
        """
        Busca productos cuyo nombre contenga el texto buscado
        Retorna una lista con los productos encontrados
        """
        productos_encontrados = []
        
        # Buscamos en minúsculas para que no importe mayúsculas/minúsculas
        nombre_busqueda = nombre.lower()
        
        for producto in self.productos:
            if nombre_busqueda in producto.get_nombre().lower():
                productos_encontrados.append(producto)
        
        return productos_encontrados
    
    def mostrar_todos(self):
        """
        Muestra todos los productos en el inventario
        """
        if len(self.productos) == 0:
            print("📦 El inventario está vacío")
            return
        
        print("\n" + "="*70)
        print("📦 INVENTARIO COMPLETO")
        print("="*70)
        
        for producto in self.productos:
            print(producto)
        
        print("="*70)
        print(f"Total de productos: {len(self.productos)}\n")
    
    def obtener_producto_por_id(self, id):
        """
        Método auxiliar para obtener un producto por su ID
        """
        for producto in self.productos:
            if producto.get_id() == id:
                return producto
        return None
