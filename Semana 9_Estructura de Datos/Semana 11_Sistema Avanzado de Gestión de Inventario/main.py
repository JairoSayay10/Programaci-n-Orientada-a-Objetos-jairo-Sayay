# ============================================================
# main.py - Programa Principal
# Menú interactivo del Sistema de Gestión de Inventarios
# NUEVO: opción de buscar por categoría y ver resumen del inventario
# ============================================================

from producto import Producto, CATEGORIAS_VALIDAS
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
    print("5. Buscar productos por categoría")
    print("6. Mostrar todos los productos")
    print("7. Ver resumen del inventario")
    print("8. Salir")
    print("=" * 50)


def mostrar_categorias():
    """Muestra las categorías disponibles para que el usuario elija."""
    print("\nCategorías disponibles:")
    # CATEGORIAS_VALIDAS es una tupla definida en producto.py
    for i, cat in enumerate(CATEGORIAS_VALIDAS, start=1):
        print(f"  {i}. {cat}")


def pedir_categoria():
    """
    Pide al usuario que elija una categoría del menú.
    Retorna la categoría elegida o 'otros' si la opción no es válida.
    """
    mostrar_categorias()
    try:
        opcion = int(input("Seleccione una categoría (número): "))
        if 1 <= opcion <= len(CATEGORIAS_VALIDAS):
            return CATEGORIAS_VALIDAS[opcion - 1]
        else:
            print("⚠️  Número fuera de rango. Se usará 'otros'.")
            return "otros"
    except ValueError:
        print("⚠️  Entrada inválida. Se usará 'otros'.")
        return "otros"


def añadir_producto_menu(inventario):
    """
    Pide los datos al usuario y añade el producto al inventario.
    """
    print("\n--- AÑADIR NUEVO PRODUCTO ---")
    try:
        id = int(input("Ingrese el ID del producto: "))
        nombre = input("Ingrese el nombre del producto: ").strip()

        if not nombre:
            print("⚠️  El nombre no puede estar vacío.")
            return
        if "," in nombre:
            print("⚠️  El nombre no puede contener comas.")
            return

        cantidad = int(input("Ingrese la cantidad en stock: "))
        precio   = float(input("Ingrese el precio del producto: "))

        if cantidad < 0 or precio < 0:
            print("⚠️  La cantidad y el precio deben ser valores positivos.")
            return

        # Pedir categoría con el menú
        categoria = pedir_categoria()

        nuevo_producto = Producto(id, nombre, cantidad, precio, categoria)
        inventario.añadir_producto(nuevo_producto)

    except ValueError:
        print("⚠️  Por favor ingrese valores numéricos válidos donde corresponde.")


def eliminar_producto_menu(inventario):
    """Pide el ID y elimina el producto."""
    print("\n--- ELIMINAR PRODUCTO ---")
    try:
        id = int(input("Ingrese el ID del producto a eliminar: "))
        inventario.eliminar_producto(id)
    except ValueError:
        print("⚠️  Por favor ingrese un ID numérico válido.")


def actualizar_producto_menu(inventario):
    """Permite actualizar cantidad, precio y/o categoría de un producto."""
    print("\n--- ACTUALIZAR PRODUCTO ---")
    try:
        id = int(input("Ingrese el ID del producto a actualizar: "))

        producto = inventario.obtener_producto_por_id(id)
        if producto is None:
            print(f"⚠️  No se encontró un producto con el ID {id}.")
            return

        print(f"\nProducto actual: {producto}")
        print("\n¿Qué desea actualizar?")
        print("1. Cantidad")
        print("2. Precio")
        print("3. Categoría")
        print("4. Cantidad y Precio")
        print("5. Todo (Cantidad, Precio y Categoría)")
        opcion = input("Seleccione una opción (1-5): ")

        nueva_cantidad  = None
        nuevo_precio    = None
        nueva_categoria = None

        if opcion in ("1", "4", "5"):
            nueva_cantidad = int(input("Ingrese la nueva cantidad: "))
            if nueva_cantidad < 0:
                print("⚠️  La cantidad no puede ser negativa.")
                return

        if opcion in ("2", "4", "5"):
            nuevo_precio = float(input("Ingrese el nuevo precio: "))
            if nuevo_precio < 0:
                print("⚠️  El precio no puede ser negativo.")
                return

        if opcion in ("3", "5"):
            nueva_categoria = pedir_categoria()

        if opcion not in ("1", "2", "3", "4", "5"):
            print("⚠️  Opción inválida.")
            return

        inventario.actualizar_producto(id, nueva_cantidad, nuevo_precio, nueva_categoria)

    except ValueError:
        print("⚠️  Por favor ingrese valores válidos.")


def buscar_por_nombre_menu(inventario):
    """Busca productos por nombre y muestra los resultados."""
    print("\n--- BUSCAR PRODUCTO POR NOMBRE ---")
    nombre = input("Ingrese el nombre o parte del nombre a buscar: ")
    resultados = inventario.buscar_por_nombre(nombre)

    if not resultados:
        print(f"❌ No se encontraron productos que contengan '{nombre}'.")
    else:
        print(f"\n✅ Se encontraron {len(resultados)} producto(s):")
        print("-" * 70)
        for producto in resultados:
            print(producto)
        print("-" * 70)


def buscar_por_categoria_menu(inventario):
    """Filtra productos por categoría y muestra los resultados."""
    print("\n--- BUSCAR PRODUCTOS POR CATEGORÍA ---")
    categoria = pedir_categoria()
    resultados = inventario.buscar_por_categoria(categoria)

    if not resultados:
        print(f"❌ No hay productos en la categoría '{categoria}'.")
    else:
        print(f"\n✅ Productos en la categoría '{categoria}' ({len(resultados)} encontrado(s)):")
        print("-" * 70)
        for producto in resultados:
            print(producto)
        print("-" * 70)


def main():
    """
    Función principal: arranca el programa y muestra el menú en bucle
    hasta que el usuario decida salir.
    """
    print("\n¡Bienvenido al Sistema de Gestión de Inventarios!")
    print("(Los datos se cargarán automáticamente desde el archivo guardado)\n")

    inventario = Inventario()

    while True:
        mostrar_menu()
        opcion = input("\nSeleccione una opción (1-8): ")

        if opcion == "1":
            añadir_producto_menu(inventario)
        elif opcion == "2":
            eliminar_producto_menu(inventario)
        elif opcion == "3":
            actualizar_producto_menu(inventario)
        elif opcion == "4":
            buscar_por_nombre_menu(inventario)
        elif opcion == "5":
            buscar_por_categoria_menu(inventario)
        elif opcion == "6":
            inventario.mostrar_todos()
        elif opcion == "7":
            inventario.resumen_inventario()
        elif opcion == "8":
            print("\n👋 ¡Gracias por usar el sistema! Hasta pronto.")
            break
        else:
            print("⚠️  Opción inválida. Por favor seleccione una opción del 1 al 8.")


if __name__ == "__main__":
    main()
