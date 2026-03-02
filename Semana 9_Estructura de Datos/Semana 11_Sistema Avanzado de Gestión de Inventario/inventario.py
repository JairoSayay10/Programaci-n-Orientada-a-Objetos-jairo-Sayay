# ============================================================
# inventario.py - Clase Inventario
# Gestiona todos los productos de la tienda
#
# COLECCIONES USADAS:
#   - Diccionario (self.productos): almacena productos con el ID como clave,
#     así buscar un producto por ID es casi instantáneo.
#   - Conjunto (self.nombres_registrados): guarda los nombres en minúsculas
#     para detectar rápido si ya existe un producto con el mismo nombre.
#   - Tupla (CATEGORIAS_VALIDAS en producto.py): categorías fijas que no cambian.
#   - Listas: se usan al momento de mostrar o filtrar resultados.
# ============================================================

from producto import Producto

ARCHIVO_INVENTARIO = "inventario.txt"


class Inventario:
    def __init__(self):
        """
        Prepara el inventario vacío y carga los datos del archivo si existe.
        """
        # DICCIONARIO: clave = ID del producto, valor = objeto Producto
        # Esto hace que buscar por ID sea súper rápido (O(1) en vez de recorrer lista)
        self.productos = {}

        # CONJUNTO: guarda los nombres (en minúsculas) de todos los productos
        # Sirve para avisar rápido si alguien intenta añadir un nombre duplicado
        self.nombres_registrados = set()

        self._cargar_desde_archivo()

    # ══════════════════════════════════════════════════════════
    # SECCIÓN 1 – LEER Y ESCRIBIR EN EL ARCHIVO
    # ══════════════════════════════════════════════════════════

    def _cargar_desde_archivo(self):
        """
        Lee inventario.txt y llena el diccionario con los productos guardados.
        Maneja varios errores para que el programa no se caiga.
        """
        try:
            with open(ARCHIVO_INVENTARIO, "r", encoding="utf-8") as archivo:
                lineas = archivo.readlines()

            productos_cargados = 0
            lineas_corruptas   = 0

            for numero_linea, linea in enumerate(lineas, start=1):
                # Saltamos líneas vacías y comentarios
                if linea.strip() == "" or linea.startswith("#"):
                    continue
                try:
                    producto = Producto.desde_linea_csv(linea)
                    # Guardamos en el diccionario usando el ID como clave
                    self.productos[producto.get_id()] = producto
                    # Registramos el nombre en el conjunto
                    self.nombres_registrados.add(producto.get_nombre().lower())
                    productos_cargados += 1
                except ValueError as e:
                    print(f"⚠️  Línea {numero_linea} ignorada (datos inválidos): {e}")
                    lineas_corruptas += 1

            print(f"📂 Inventario cargado: {productos_cargados} producto(s) recuperado(s)"
                  + (f" | {lineas_corruptas} línea(s) corrupta(s) ignorada(s)."
                     if lineas_corruptas else "."))

        except FileNotFoundError:
            print(f"📄 Archivo '{ARCHIVO_INVENTARIO}' no encontrado. "
                  "Se creará uno nuevo al añadir el primer producto.")
            self._crear_archivo_vacio()
        except PermissionError:
            print(f"🔒 Sin permisos para leer '{ARCHIVO_INVENTARIO}'. "
                  "El inventario inicia vacío.")
        except Exception as e:
            print(f"❌ Error inesperado al cargar el inventario: {e}")

    def _guardar_en_archivo(self):
        """
        Guarda todos los productos del diccionario en inventario.txt.
        Se llama automáticamente después de cada cambio.
        Devuelve True si funcionó, False si hubo algún problema.
        """
        try:
            with open(ARCHIVO_INVENTARIO, "w", encoding="utf-8") as archivo:
                archivo.write("# Inventario - formato: id,nombre,cantidad,precio,categoria\n")
                # Recorremos los valores del diccionario para escribir cada producto
                for producto in self.productos.values():
                    archivo.write(producto.a_linea_csv())
            return True
        except PermissionError:
            print(f"🔒 Sin permisos para escribir en '{ARCHIVO_INVENTARIO}'. Los cambios NO se guardaron.")
            return False
        except OSError as e:
            print(f"💾 Error del sistema al guardar: {e}")
            return False
        except Exception as e:
            print(f"❌ Error inesperado al guardar: {e}")
            return False

    def _crear_archivo_vacio(self):
        """Crea el archivo inventario.txt con solo la cabecera."""
        try:
            with open(ARCHIVO_INVENTARIO, "w", encoding="utf-8") as archivo:
                archivo.write("# Inventario - formato: id,nombre,cantidad,precio,categoria\n")
            print(f"✅ Archivo '{ARCHIVO_INVENTARIO}' creado exitosamente.")
        except PermissionError:
            print(f"🔒 Sin permisos para crear '{ARCHIVO_INVENTARIO}'.")
        except Exception as e:
            print(f"❌ Error al crear el archivo: {e}")

    # ══════════════════════════════════════════════════════════
    # SECCIÓN 2 – OPERACIONES SOBRE EL INVENTARIO
    # ══════════════════════════════════════════════════════════

    def añadir_producto(self, producto):
        """
        Añade un producto al diccionario si el ID no está repetido.
        También avisa si el nombre ya existe (usando el conjunto).
        """
        # Verificar ID único — con diccionario esto es directo
        if producto.get_id() in self.productos:
            print(f"⚠️  Ya existe un producto con el ID {producto.get_id()}.")
            return False

        # Avisar si el nombre ya está registrado (no impide añadir, solo avisa)
        if producto.get_nombre().lower() in self.nombres_registrados:
            print(f"ℹ️  Aviso: Ya hay un producto llamado '{producto.get_nombre()}' en el inventario.")

        # Añadir al diccionario y al conjunto de nombres
        self.productos[producto.get_id()] = producto
        self.nombres_registrados.add(producto.get_nombre().lower())

        if self._guardar_en_archivo():
            print(f"✅ Producto '{producto.get_nombre()}' añadido y guardado exitosamente.")
        else:
            print(f"⚠️  Producto añadido en memoria, pero NO pudo guardarse en el archivo.")
        return True

    def eliminar_producto(self, id):
        """
        Elimina un producto del diccionario usando su ID.
        Con diccionario, no necesitamos recorrer toda la lista — es directo.
        """
        if id not in self.productos:
            print(f"⚠️  No se encontró un producto con el ID {id}.")
            return False

        nombre = self.productos[id].get_nombre()
        # Quitamos del diccionario
        del self.productos[id]
        # Quitamos del conjunto de nombres
        self.nombres_registrados.discard(nombre.lower())

        if self._guardar_en_archivo():
            print(f"✅ Producto '{nombre}' eliminado y cambio guardado.")
        else:
            print(f"⚠️  Producto '{nombre}' eliminado en memoria, pero NO pudo guardarse.")
        return True

    def actualizar_producto(self, id, nueva_cantidad=None, nuevo_precio=None, nueva_categoria=None):
        """
        Actualiza los datos de un producto existente.
        Buscar por ID en el diccionario es instantáneo.
        """
        if id not in self.productos:
            print(f"⚠️  No se encontró un producto con el ID {id}.")
            return False

        producto = self.productos[id]

        if nueva_cantidad is not None:
            producto.set_cantidad(nueva_cantidad)
            print(f"✅ Cantidad actualizada a {nueva_cantidad}.")

        if nuevo_precio is not None:
            producto.set_precio(nuevo_precio)
            print(f"✅ Precio actualizado a ${nuevo_precio:.2f}.")

        if nueva_categoria is not None:
            producto.set_categoria(nueva_categoria)
            print(f"✅ Categoría actualizada a '{nueva_categoria}'.")

        if self._guardar_en_archivo():
            print(f"💾 Cambios guardados correctamente en '{ARCHIVO_INVENTARIO}'.")
        else:
            print("⚠️  Cambios aplicados en memoria, pero NO pudieron guardarse.")
        return True

    # ══════════════════════════════════════════════════════════
    # SECCIÓN 3 – CONSULTAS (solo lectura)
    # ══════════════════════════════════════════════════════════

    def buscar_por_nombre(self, nombre):
        """
        Busca productos cuyo nombre contenga el texto buscado.
        Retorna una LISTA con los resultados encontrados.
        La búsqueda no distingue mayúsculas de minúsculas.
        """
        nombre_busqueda = nombre.lower()
        # Recorremos los valores del diccionario y filtramos
        return [p for p in self.productos.values()
                if nombre_busqueda in p.get_nombre().lower()]

    def buscar_por_categoria(self, categoria):
        """
        Filtra y muestra todos los productos de una categoría específica.
        Retorna una LISTA con los productos encontrados.
        """
        categoria_busqueda = categoria.lower()
        return [p for p in self.productos.values()
                if p.get_categoria().lower() == categoria_busqueda]

    def obtener_categorias_en_uso(self):
        """
        Devuelve un CONJUNTO con las categorías que actualmente
        tienen al menos un producto. Útil para ver qué categorías están activas.
        """
        return {p.get_categoria() for p in self.productos.values()}

    def mostrar_todos(self):
        """Muestra todos los productos del inventario en consola."""
        if not self.productos:
            print("📦 El inventario está vacío.")
            return

        print("\n" + "=" * 70)
        print("📦 INVENTARIO COMPLETO")
        print("=" * 70)
        # Ordenamos por ID para mostrarlos en orden (los diccionarios no tienen orden fijo en Python antiguo)
        for id_key in sorted(self.productos.keys()):
            print(self.productos[id_key])
        print("=" * 70)
        print(f"Total de productos: {len(self.productos)}")

        # Mostramos las categorías activas usando el conjunto
        categorias_activas = self.obtener_categorias_en_uso()
        print(f"Categorías en uso:  {', '.join(sorted(categorias_activas))}\n")

    def obtener_producto_por_id(self, id):
        """
        Retorna el producto con ese ID, o None si no existe.
        Con el diccionario esto es directo y muy rápido.
        """
        return self.productos.get(id, None)

    def resumen_inventario(self):
        """
        Muestra un resumen rápido con estadísticas del inventario.
        Usa el diccionario para calcular totales.
        """
        if not self.productos:
            print("📦 El inventario está vacío.")
            return

        total_productos  = len(self.productos)
        total_unidades   = sum(p.get_cantidad() for p in self.productos.values())
        valor_total      = sum(p.get_cantidad() * p.get_precio() for p in self.productos.values())
        categorias_en_uso = self.obtener_categorias_en_uso()

        print("\n" + "=" * 50)
        print("📊 RESUMEN DEL INVENTARIO")
        print("=" * 50)
        print(f"  Tipos de productos   : {total_productos}")
        print(f"  Total de unidades    : {total_unidades}")
        print(f"  Valor total del stock: ${valor_total:.2f}")
        print(f"  Categorías activas   : {', '.join(sorted(categorias_en_uso))}")
        print("=" * 50 + "\n")
