# ============================================================
# main.py - Programa Principal
# Menú interactivo del Sistema de Gestión de Inventarios
# NUEVO: notificaciones sobre operaciones de archivo
# ============================================================

from producto import Producto
from inventario import Inventario


def mostrar_menu():
    """Muestra el menú principal con todas las opciones disponibles."""
    print("\n" + "=" * 50)
    print("🏪  SISTEMA DE GESTIÓN DE INVENTARIOS")
    print("=" * 50)
    print("1. Añadir nuevo producto")
    print("2. Eliminar producto")
    print("3. Actualizar producto")
    print("4. Buscar producto por nombre")
    print("5. Mostrar todos los productos")
    print("6. Salir")
    print("=" * 50)


def añadir_producto_menu(inventario):
    """
    Solicita los datos al usuario y añade un producto al inventario.
    Informa si el producto se guardó correctamente en el archivo.
    """
    print("\n--- AÑADIR NUEVO PRODUCTO ---")
    try:
        id       = int(input("Ingrese el ID del producto: "))
        nombre   = input("Ingrese el nombre del producto: ").strip()
        if not nombre:
            print("⚠️  Error: El nombre no puede estar vacío.")
            return
        # Validar que el nombre no contenga comas (romperían el formato CSV)
        if "," in nombre:
            print("⚠️  Error: El nombre no puede contener comas.")
            return
        cantidad = int(input("Ingrese la cantidad en stock: "))
        precio   = float(input("Ingrese el precio del producto: "))

        if cantidad < 0 or precio < 0:
            print("⚠️  Error: La cantidad y el precio deben ser valores positivos.")
            return

        nuevo_producto = Producto(id, nombre, cantidad, precio)
        inventario.añadir_producto(nuevo_producto)

    except ValueError:
        print("⚠️  Error: Por favor ingrese valores numéricos válidos.")


def eliminar_producto_menu(inventario):
    """
    Solicita el ID y elimina el producto del inventario.
    Informa si la eliminación se reflejó en el archivo.
    """
    print("\n--- ELIMINAR PRODUCTO ---")
    try:
        id = int(input("Ingrese el ID del producto a eliminar: "))
        inventario.eliminar_producto(id)
    except ValueError:
        print("⚠️  Error: Por favor ingrese un ID numérico válido.")


def actualizar_producto_menu(inventario):
    """
    Permite actualizar la cantidad y/o precio de un producto.
    Informa si la actualización se guardó correctamente en el archivo.
    """
    print("\n--- ACTUALIZAR PRODUCTO ---")
    try:
        id = int(input("Ingrese el ID del producto a actualizar: "))

        producto = inventario.obtener_producto_por_id(id)
        if producto is None:
            print(f"⚠️  Error: No se encontró un producto con el ID {id}.")
            return

        print(f"\nProducto actual: {producto}")
        print("\n¿Qué desea actualizar?")
        print("1. Cantidad")
        print("2. Precio")
        print("3. Ambos")
        opcion = input("Seleccione una opción (1-3): ")

        nueva_cantidad = None
        nuevo_precio   = None

        if opcion in ("1", "3"):
            nueva_cantidad = int(input("Ingrese la nueva cantidad: "))
            if nueva_cantidad < 0:
                print("⚠️  La cantidad no puede ser negativa.")
                return

        if opcion in ("2", "3"):
            nuevo_precio = float(input("Ingrese el nuevo precio: "))
            if nuevo_precio < 0:
                print("⚠️  El precio no puede ser negativo.")
                return

        if opcion not in ("1", "2", "3"):
            print("⚠️  Opción inválida.")
            return

        inventario.actualizar_producto(id, nueva_cantidad, nuevo_precio)

    except ValueError:
        print("⚠️  Error: Por favor ingrese valores válidos.")


def buscar_producto_menu(inventario):
    """Busca productos por nombre y muestra los resultados."""
    print("\n--- BUSCAR PRODUCTO ---")
    nombre = input("Ingrese el nombre o parte del nombre a buscar: ")
    productos_encontrados = inventario.buscar_por_nombre(nombre)

    if not productos_encontrados:
        print(f"❌ No se encontraron productos que contengan '{nombre}'.")
    else:
        print(f"\n✅ Se encontraron {len(productos_encontrados)} producto(s):")
        print("-" * 70)
        for producto in productos_encontrados:
            print(producto)
        print("-" * 70)


def main():
    """
    Función principal que ejecuta el programa.
    Al iniciar, el inventario carga automáticamente los datos desde el archivo.
    """
    print("\n¡Bienvenido al Sistema de Gestión de Inventarios!")
    print("(Los datos se cargarán automáticamente desde el archivo guardado)\n")

    # Al crear el inventario, se intenta cargar inventario.txt automáticamente
    inventario = Inventario()

    while True:
        mostrar_menu()
        opcion = input("\nSeleccione una opción (1-6): ")

        if opcion == "1":
            añadir_producto_menu(inventario)

        elif opcion == "2":
            eliminar_producto_menu(inventario)

        elif opcion == "3":
            actualizar_producto_menu(inventario)

        elif opcion == "4":
            buscar_producto_menu(inventario)

        elif opcion == "5":
            inventario.mostrar_todos()

        elif opcion == "6":
            print("\n👋 ¡Gracias por usar el sistema! Hasta pronto.")
            break

        else:
            print("⚠️  Opción inválida. Por favor seleccione una opción del 1 al 6.")


# Este bloque se ejecuta solo si corremos este archivo directamente
if __name__ == "__main__":
    main()
