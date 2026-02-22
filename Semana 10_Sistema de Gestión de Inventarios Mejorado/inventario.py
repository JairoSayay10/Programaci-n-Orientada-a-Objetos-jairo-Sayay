# ============================================================
# inventario.py - Clase Inventario
# Gestiona la colección de productos y su persistencia en archivo
# NUEVO: lectura/escritura en inventario.txt + manejo de excepciones
# ============================================================

from producto import Producto

# Nombre del archivo donde se guardará el inventario
ARCHIVO_INVENTARIO = "inventario.txt"


class Inventario:
    def __init__(self):
        """
        Inicializa el inventario y carga los datos desde el archivo.
        Si el archivo no existe, lo crea vacío automáticamente.
        """
        self.productos = []
        self._cargar_desde_archivo()

    # ══════════════════════════════════════════════════════════
    # SECCIÓN 1 – PERSISTENCIA EN ARCHIVO
    # Métodos privados para leer y escribir en inventario.txt
    # ══════════════════════════════════════════════════════════

    def _cargar_desde_archivo(self):
        """
        Lee inventario.txt al iniciar el programa y reconstruye
        la lista de productos en memoria.

        Excepciones manejadas:
        - FileNotFoundError : el archivo aún no existe → se crea vacío.
        - PermissionError   : sin permisos de lectura → se avisa al usuario.
        - ValueError        : línea con formato corrupto → se omite y avisa.
        - Exception         : cualquier otro error inesperado.
        """
        try:
            with open(ARCHIVO_INVENTARIO, "r", encoding="utf-8") as archivo:
                lineas = archivo.readlines()

            productos_cargados = 0
            lineas_corruptas   = 0

            for numero_linea, linea in enumerate(lineas, start=1):
                # Ignorar líneas vacías o comentarios (líneas que empiecen con #)
                if linea.strip() == "" or linea.startswith("#"):
                    continue
                try:
                    producto = Producto.desde_linea_csv(linea)
                    self.productos.append(producto)
                    productos_cargados += 1
                except ValueError as e:
                    # Línea corrupta: se registra pero no detiene el programa
                    print(f"⚠️  Línea {numero_linea} ignorada (datos inválidos): {e}")
                    lineas_corruptas += 1

            print(f"📂 Inventario cargado: {productos_cargados} producto(s) recuperado(s)"
                  + (f" | {lineas_corruptas} línea(s) corrupta(s) ignorada(s)."
                     if lineas_corruptas else "."))

        except FileNotFoundError:
            # El archivo no existe todavía → lo creamos vacío
            print(f"📄 Archivo '{ARCHIVO_INVENTARIO}' no encontrado. "
                  "Se creará uno nuevo al añadir el primer producto.")
            self._crear_archivo_vacio()

        except PermissionError:
            print(f"🔒 Error: Sin permisos para leer '{ARCHIVO_INVENTARIO}'. "
                  "El inventario se iniciará vacío.")

        except Exception as e:
            print(f"❌ Error inesperado al cargar el inventario: {e}")

    def _guardar_en_archivo(self):
        """
        Sobreescribe inventario.txt con el estado actual de self.productos.
        Se llama automáticamente tras cada modificación (añadir/actualizar/eliminar).

        Excepciones manejadas:
        - PermissionError : sin permisos de escritura.
        - OSError         : disco lleno u otro error del sistema de archivos.
        - Exception       : cualquier otro error inesperado.

        Retorna True si se guardó correctamente, False si hubo error.
        """
        try:
            with open(ARCHIVO_INVENTARIO, "w", encoding="utf-8") as archivo:
                # Cabecera informativa dentro del archivo
                archivo.write("# Inventario - formato: id,nombre,cantidad,precio\n")
                for producto in self.productos:
                    archivo.write(producto.a_linea_csv())
            return True

        except PermissionError:
            print(f"🔒 Error: Sin permisos para escribir en '{ARCHIVO_INVENTARIO}'. "
                  "Los cambios NO se guardaron en el archivo.")
            return False

        except OSError as e:
            print(f"💾 Error del sistema de archivos al guardar: {e}")
            return False

        except Exception as e:
            print(f"❌ Error inesperado al guardar el inventario: {e}")
            return False

    def _crear_archivo_vacio(self):
        """
        Crea inventario.txt vacío (solo con la cabecera).
        Se llama cuando el archivo no existe al iniciar el programa.
        """
        try:
            with open(ARCHIVO_INVENTARIO, "w", encoding="utf-8") as archivo:
                archivo.write("# Inventario - formato: id,nombre,cantidad,precio\n")
            print(f"✅ Archivo '{ARCHIVO_INVENTARIO}' creado exitosamente.")
        except PermissionError:
            print(f"🔒 Error: Sin permisos para crear '{ARCHIVO_INVENTARIO}'.")
        except Exception as e:
            print(f"❌ Error al crear el archivo: {e}")

    # ══════════════════════════════════════════════════════════
    # SECCIÓN 2 – OPERACIONES DE INVENTARIO
    # Cada operación modifica la lista en memoria y luego
    # llama a _guardar_en_archivo() para persistir el cambio.
    # ══════════════════════════════════════════════════════════

    def añadir_producto(self, producto):
        """
        Añade un nuevo producto al inventario verificando que el ID sea único.
        Tras añadirlo en memoria, guarda el inventario en el archivo.
        """
        # Verificar ID único
        for p in self.productos:
            if p.get_id() == producto.get_id():
                print(f"⚠️  Error: Ya existe un producto con el ID {producto.get_id()}.")
                return False

        self.productos.append(producto)

        # Persistir en archivo e informar al usuario
        if self._guardar_en_archivo():
            print(f"✅ Producto '{producto.get_nombre()}' añadido y guardado en "
                  f"'{ARCHIVO_INVENTARIO}' exitosamente.")
        else:
            print(f"⚠️  Producto '{producto.get_nombre()}' añadido en memoria, "
                  "pero NO pudo guardarse en el archivo.")
        return True

    def eliminar_producto(self, id):
        """
        Elimina un producto del inventario por su ID.
        Tras eliminarlo en memoria, guarda el inventario en el archivo.
        """
        for i, producto in enumerate(self.productos):
            if producto.get_id() == id:
                nombre = producto.get_nombre()
                self.productos.pop(i)

                if self._guardar_en_archivo():
                    print(f"✅ Producto '{nombre}' eliminado y cambio guardado en "
                          f"'{ARCHIVO_INVENTARIO}'.")
                else:
                    print(f"⚠️  Producto '{nombre}' eliminado en memoria, "
                          "pero NO pudo guardarse en el archivo.")
                return True

        print(f"⚠️  Error: No se encontró un producto con el ID {id}.")
        return False

    def actualizar_producto(self, id, nueva_cantidad=None, nuevo_precio=None):
        """
        Actualiza cantidad y/o precio de un producto.
        Tras actualizar en memoria, guarda el inventario en el archivo.
        """
        for producto in self.productos:
            if producto.get_id() == id:
                if nueva_cantidad is not None:
                    producto.set_cantidad(nueva_cantidad)
                    print(f"✅ Cantidad actualizada a {nueva_cantidad}.")

                if nuevo_precio is not None:
                    producto.set_precio(nuevo_precio)
                    print(f"✅ Precio actualizado a ${nuevo_precio:.2f}.")

                if self._guardar_en_archivo():
                    print(f"💾 Cambios guardados correctamente en '{ARCHIVO_INVENTARIO}'.")
                else:
                    print("⚠️  Cambios aplicados en memoria, pero NO pudieron guardarse "
                          "en el archivo.")
                return True

        print(f"⚠️  Error: No se encontró un producto con el ID {id}.")
        return False

    # ══════════════════════════════════════════════════════════
    # SECCIÓN 3 – CONSULTAS (solo lectura, sin tocar el archivo)
    # ══════════════════════════════════════════════════════════

    def buscar_por_nombre(self, nombre):
        """
        Busca productos cuyo nombre contenga el texto indicado.
        La búsqueda es insensible a mayúsculas/minúsculas.
        Retorna una lista con los productos encontrados.
        """
        nombre_busqueda = nombre.lower()
        return [p for p in self.productos
                if nombre_busqueda in p.get_nombre().lower()]

    def mostrar_todos(self):
        """Muestra todos los productos del inventario en consola."""
        if not self.productos:
            print("📦 El inventario está vacío.")
            return

        print("\n" + "=" * 70)
        print("📦 INVENTARIO COMPLETO")
        print("=" * 70)
        for producto in self.productos:
            print(producto)
        print("=" * 70)
        print(f"Total de productos: {len(self.productos)}\n")

    def obtener_producto_por_id(self, id):
        """Retorna el producto con el ID indicado, o None si no existe."""
        for producto in self.productos:
            if producto.get_id() == id:
                return producto
        return None
