# 📦 Sistema de Gestión de Inventarios — v2.0

Sistema de gestión de inventarios para una tienda, desarrollado en Python con **Programación Orientada a Objetos (POO)**, **persistencia en archivos** y **manejo robusto de excepciones**.

---

## 📋 Descripción

El programa permite gestionar el inventario de una tienda mediante una interfaz de consola interactiva. A partir de esta versión, **todos los cambios se guardan automáticamente** en `inventario.txt` y se recuperan al volver a iniciar el programa.

---

## 🚀 Funcionalidades

| Función | Descripción |
|---|---|
| ✅ Añadir productos | Registra productos con ID único, nombre, cantidad y precio |
| ❌ Eliminar productos | Remueve un producto por su ID |
| 🔄 Actualizar productos | Modifica cantidad o precio de un producto existente |
| 🔍 Buscar productos | Búsqueda parcial e insensible a mayúsculas por nombre |
| 📊 Mostrar inventario | Lista todos los productos registrados |
| 💾 Persistencia | Guarda y carga automáticamente desde `inventario.txt` |
| 🛡️ Manejo de errores | Captura `FileNotFoundError`, `PermissionError`, datos corruptos y más |

---

## 📁 Estructura del Proyecto

```
sistema-inventarios/
│
├── producto.py        # Clase Producto + serialización CSV
├── inventario.py      # Clase Inventario + lógica de archivos y excepciones
├── main.py            # Menú interactivo principal
├── inventario.txt     # Archivo de datos (se crea automáticamente)
└── README.md          # Este archivo
```

---

## 🛠️ Requisitos

- Python 3.6 o superior
- No requiere librerías externas

---

## 💻 Instalación y Ejecución

1. **Clonar el repositorio**:
   ```bash
   git clone https://github.com/tu-usuario/sistema-inventarios.git
   cd sistema-inventarios
   ```

2. **Ejecutar el programa**:
   ```bash
   python main.py
   ```

3. El programa cargará automáticamente `inventario.txt` si existe, o lo creará vacío si es la primera vez.

---

## 📖 Ejemplo de Uso

```
¡Bienvenido al Sistema de Gestión de Inventarios!
(Los datos se cargarán automáticamente desde el archivo guardado)

📂 Inventario cargado: 3 producto(s) recuperado(s).

==================================================
🏪  SISTEMA DE GESTIÓN DE INVENTARIOS
==================================================
1. Añadir nuevo producto
...

Seleccione una opción (1-6): 1

--- AÑADIR NUEVO PRODUCTO ---
Ingrese el ID del producto: 4
Ingrese el nombre del producto: Fresas
Ingrese la cantidad en stock: 80
Ingrese el precio del producto: 4.99
✅ Producto 'Fresas' añadido y guardado en 'inventario.txt' exitosamente.
```

---

## 🏗️ Clases y Métodos

### `Producto` — `producto.py`
- **Atributos**: `id`, `nombre`, `cantidad`, `precio`
- **Getters / Setters** para todos los atributos
- `a_linea_csv()` → serializa el producto como línea CSV para guardar en archivo
- `desde_linea_csv(linea)` *(estático)* → reconstruye un Producto desde una línea CSV

### `Inventario` — `inventario.py`

#### Métodos públicos
| Método | Descripción |
|---|---|
| `añadir_producto(p)` | Añade y persiste en archivo |
| `eliminar_producto(id)` | Elimina y persiste en archivo |
| `actualizar_producto(id, ...)` | Actualiza y persiste en archivo |
| `buscar_por_nombre(nombre)` | Búsqueda en memoria |
| `mostrar_todos()` | Imprime inventario en consola |
| `obtener_producto_por_id(id)` | Auxiliar de búsqueda por ID |

#### Métodos privados (manejo de archivos)
| Método | Descripción |
|---|---|
| `_cargar_desde_archivo()` | Lee `inventario.txt` al iniciar |
| `_guardar_en_archivo()` | Sobreescribe `inventario.txt` tras cada cambio |
| `_crear_archivo_vacio()` | Crea el archivo si no existe |

---

## 🛡️ Manejo de Excepciones

| Excepción | Dónde se maneja | Respuesta del programa |
|---|---|---|
| `FileNotFoundError` | `_cargar_desde_archivo` | Crea el archivo vacío automáticamente |
| `PermissionError` (lectura) | `_cargar_desde_archivo` | Avisa al usuario, inicia con inventario vacío |
| `PermissionError` (escritura) | `_guardar_en_archivo` | Avisa que el cambio no pudo guardarse |
| `ValueError` (línea corrupta) | `_cargar_desde_archivo` | Omite la línea e informa al usuario |
| `OSError` (disco lleno, etc.) | `_guardar_en_archivo` | Avisa del error del sistema de archivos |
| `Exception` genérica | Ambos métodos de archivo | Muestra el error sin cerrar el programa |
| `ValueError` (input inválido) | Funciones de menú en `main.py` | Solicita al usuario que ingrese datos válidos |

---

## 📄 Formato del Archivo `inventario.txt`

```
# Inventario - formato: id,nombre,cantidad,precio
1,Manzanas,50,2.5
2,Naranjas,30,1.8
3,Plátanos,100,0.99
```

- La primera línea es un comentario (ignorado al cargar).
- Cada línea representa un producto con cuatro campos separados por coma.

---

## 🎓 Objetivos de Aprendizaje

- Programación Orientada a Objetos (POO)
- Manipulación de archivos de texto (`open`, `read`, `write`)
- Manejo de excepciones (`try`, `except`, `FileNotFoundError`, `PermissionError`)
- Validación de datos de entrada
- Separación de responsabilidades entre clases
- Uso de Git y GitHub
- Documentación de código

---

## 👤 Autor

**Jairo Estiven Sayay Alvarez** — Estudiante de Programación

## 📝 Notas

Proyecto v2.0 desarrollado como continuación del ejercicio de aprendizaje de Python y POO, incorporando persistencia de datos y manejo robusto de excepciones.
