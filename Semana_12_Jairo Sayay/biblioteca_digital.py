# ================================================
# Sistema de Gestión de Biblioteca Digital
# Autor: Jairo Estiven Sayay Alvarez
# ================================================


# ── Clase Libro ──────────────────────────────────
class Libro:
    def __init__(self, isbn, titulo, autor, categoria):
        self.isbn = isbn
        # Tupla inmutable: titulo y autor no cambian una vez creado el libro
        self.info = (titulo, autor)
        self.categoria = categoria
        self.disponible = True

    def get_titulo(self):
        return self.info[0]

    def get_autor(self):
        return self.info[1]

    def __str__(self):
        estado = "Disponible" if self.disponible else "Prestado"
        return f"[{self.isbn}] {self.get_titulo()} - {self.get_autor()} ({self.categoria}) | {estado}"


# ── Clase Usuario ────────────────────────────────
class Usuario:
    def __init__(self, id_usuario, nombre):
        self.id_usuario = id_usuario
        self.nombre = nombre
        # Lista para almacenar los libros prestados al usuario
        self.libros_prestados = []

    def __str__(self):
        return f"ID: {self.id_usuario} | Nombre: {self.nombre} | Libros prestados: {len(self.libros_prestados)}"


# ── Clase Biblioteca ─────────────────────────────
class Biblioteca:
    def __init__(self):
        # Diccionario: ISBN como clave y objeto Libro como valor
        self.catalogo = {}
        # Diccionario para almacenar usuarios
        self.usuarios = {}
        # Conjunto para garantizar IDs de usuario únicos
        self.ids_usuarios = set()

    # ── Gestión de libros ──

    def agregar_libro(self, isbn, titulo, autor, categoria):
        if isbn in self.catalogo:
            print(f"  Ya existe un libro con ISBN {isbn}.")
            return
        self.catalogo[isbn] = Libro(isbn, titulo, autor, categoria)
        print(f"  Libro '{titulo}' agregado correctamente.")

    def quitar_libro(self, isbn):
        if isbn not in self.catalogo:
            print("  Libro no encontrado.")
            return
        if not self.catalogo[isbn].disponible:
            print(f"  No se puede quitar '{self.catalogo[isbn].get_titulo()}', está prestado.")
            return
        titulo = self.catalogo[isbn].get_titulo()
        del self.catalogo[isbn]
        print(f"  Libro '{titulo}' eliminado del catálogo.")

    # ── Gestión de usuarios ──

    def registrar_usuario(self, id_usuario, nombre):
        if id_usuario in self.ids_usuarios:
            print(f"  El ID '{id_usuario}' ya está registrado.")
            return
        self.usuarios[id_usuario] = Usuario(id_usuario, nombre)
        self.ids_usuarios.add(id_usuario)
        print(f"  Usuario '{nombre}' registrado correctamente.")

    def dar_baja_usuario(self, id_usuario):
        if id_usuario not in self.ids_usuarios:
            print("  Usuario no encontrado.")
            return
        usuario = self.usuarios[id_usuario]
        if len(usuario.libros_prestados) > 0:
            print(f"  No se puede dar de baja a '{usuario.nombre}', tiene libros sin devolver.")
            return
        del self.usuarios[id_usuario]
        self.ids_usuarios.discard(id_usuario)
        print(f"  Usuario '{usuario.nombre}' dado de baja correctamente.")

    # ── Préstamos y devoluciones ──

    def prestar_libro(self, isbn, id_usuario):
        if isbn not in self.catalogo:
            print("  Libro no encontrado.")
            return
        if id_usuario not in self.ids_usuarios:
            print("  Usuario no registrado.")
            return
        libro = self.catalogo[isbn]
        if not libro.disponible:
            print(f"  '{libro.get_titulo()}' no está disponible.")
            return
        libro.disponible = False
        self.usuarios[id_usuario].libros_prestados.append(isbn)
        print(f"  Libro '{libro.get_titulo()}' prestado a {self.usuarios[id_usuario].nombre}.")

    def devolver_libro(self, isbn, id_usuario):
        if id_usuario not in self.ids_usuarios:
            print("  Usuario no registrado.")
            return
        usuario = self.usuarios[id_usuario]
        if isbn not in usuario.libros_prestados:
            print(f"  {usuario.nombre} no tiene ese libro prestado.")
            return
        self.catalogo[isbn].disponible = True
        usuario.libros_prestados.remove(isbn)
        print(f"  Libro '{self.catalogo[isbn].get_titulo()}' devuelto por {usuario.nombre}.")

    # ── Búsquedas ──

    def buscar_por_titulo(self, titulo):
        resultados = [l for l in self.catalogo.values() if titulo.lower() in l.get_titulo().lower()]
        return resultados

    def buscar_por_autor(self, autor):
        resultados = [l for l in self.catalogo.values() if autor.lower() in l.get_autor().lower()]
        return resultados

    def buscar_por_categoria(self, categoria):
        resultados = [l for l in self.catalogo.values() if categoria.lower() in l.categoria.lower()]
        return resultados

    # ── Listar libros prestados de un usuario ──

    def listar_prestamos_usuario(self, id_usuario):
        if id_usuario not in self.ids_usuarios:
            print("  Usuario no encontrado.")
            return
        usuario = self.usuarios[id_usuario]
        if len(usuario.libros_prestados) == 0:
            print(f"  {usuario.nombre} no tiene libros prestados.")
            return
        print(f"  Libros prestados a {usuario.nombre}:")
        for isbn in usuario.libros_prestados:
            print(f"    - {self.catalogo[isbn].get_titulo()}")


# ── Menú principal ───────────────────────────────

def mostrar_menu():
    print("\n╔══════════════════════════════════════╗")
    print("║     BIBLIOTECA DIGITAL - MENÚ         ║")
    print("╠══════════════════════════════════════╣")
    print("║  1. Agregar libro                     ║")
    print("║  2. Quitar libro                      ║")
    print("║  3. Registrar usuario                 ║")
    print("║  4. Dar de baja usuario               ║")
    print("║  5. Prestar libro                     ║")
    print("║  6. Devolver libro                    ║")
    print("║  7. Buscar libro                      ║")
    print("║  8. Ver préstamos de un usuario       ║")
    print("║  9. Ver catálogo completo             ║")
    print("║  0. Salir                             ║")
    print("╚══════════════════════════════════════╝")


def main():
    biblioteca = Biblioteca()

    while True:
        mostrar_menu()
        opcion = input("Selecciona una opción: ").strip()

        if opcion == "1":
            print("\n-- Agregar libro --")
            isbn = input("ISBN: ").strip()
            titulo = input("Título: ").strip()
            autor = input("Autor: ").strip()
            categoria = input("Categoría: ").strip()
            biblioteca.agregar_libro(isbn, titulo, autor, categoria)

        elif opcion == "2":
            print("\n-- Quitar libro --")
            isbn = input("ISBN del libro a quitar: ").strip()
            biblioteca.quitar_libro(isbn)

        elif opcion == "3":
            print("\n-- Registrar usuario --")
            id_usuario = input("ID de usuario: ").strip()
            nombre = input("Nombre completo: ").strip()
            biblioteca.registrar_usuario(id_usuario, nombre)

        elif opcion == "4":
            print("\n-- Dar de baja usuario --")
            id_usuario = input("ID del usuario: ").strip()
            biblioteca.dar_baja_usuario(id_usuario)

        elif opcion == "5":
            print("\n-- Prestar libro --")
            isbn = input("ISBN del libro: ").strip()
            id_usuario = input("ID del usuario: ").strip()
            biblioteca.prestar_libro(isbn, id_usuario)

        elif opcion == "6":
            print("\n-- Devolver libro --")
            isbn = input("ISBN del libro: ").strip()
            id_usuario = input("ID del usuario: ").strip()
            biblioteca.devolver_libro(isbn, id_usuario)

        elif opcion == "7":
            print("\n-- Buscar libro --")
            print("  1. Por título")
            print("  2. Por autor")
            print("  3. Por categoría")
            sub = input("Opción: ").strip()
            termino = input("Término de búsqueda: ").strip()

            if sub == "1":
                resultados = biblioteca.buscar_por_titulo(termino)
            elif sub == "2":
                resultados = biblioteca.buscar_por_autor(termino)
            elif sub == "3":
                resultados = biblioteca.buscar_por_categoria(termino)
            else:
                print("  Opción no válida.")
                continue

            if len(resultados) == 0:
                print("  No se encontraron resultados.")
            else:
                print(f"  {len(resultados)} resultado(s):")
                for libro in resultados:
                    print(f"    {libro}")

        elif opcion == "8":
            print("\n-- Préstamos de un usuario --")
            id_usuario = input("ID del usuario: ").strip()
            biblioteca.listar_prestamos_usuario(id_usuario)

        elif opcion == "9":
            print("\n-- Catálogo completo --")
            if len(biblioteca.catalogo) == 0:
                print("  El catálogo está vacío.")
            else:
                for libro in biblioteca.catalogo.values():
                    print(f"  {libro}")

        elif opcion == "0":
            print("\n  Hasta luego, Jairo!")
            break

        else:
            print("  Opción no válida, intenta de nuevo.")


main()
