# 📦 Sistema de Gestión de Inventarios — v3.0

Sistema de gestión de inventarios desarrollado en Python con **Programación Orientada a Objetos (POO)**, **colecciones** (diccionario, conjunto, tupla, lista), **persistencia en archivos** y **manejo de excepciones**.

---

## 📋 Descripción

El programa permite gestionar el inventario de una tienda desde la consola. Todos los cambios se guardan automáticamente en `inventario.txt` y se recuperan al volver a iniciar el programa. Esta versión incorpora el uso de distintas colecciones de Python para hacer el sistema más eficiente.

---

## 🚀 Funcionalidades

| Función | Descripción |
|---|---|
| ✅ Añadir productos | Registra productos con ID, nombre, cantidad, precio y categoría |
| ❌ Eliminar productos | Remueve un producto por su ID |
| 🔄 Actualizar productos | Modifica cantidad, precio y/o categoría |
| 🔍 Buscar por nombre | Búsqueda parcial e insensible a mayúsculas |
| 🏷️ Buscar por categoría | Filtra productos según su tipo |
| 📊 Mostrar todos | Lista todos los productos del inventario |
| 📈 Resumen | Muestra estadísticas: total de unidades, valor del stock, categorías activas |
| 💾 Persistencia | Guarda y carga automáticamente desde `inventario.txt` |
| 🛡️ Manejo de errores | Captura errores de archivo, permisos y datos corruptos |

---

## 📁 Estructura del Proyecto

```
sistema-inventarios/
│
├── producto.py        # Clase Producto + serialización CSV
├── inventario.py      # Clase Inventario con diccionario + colecciones
├── main.py            # Menú interactivo principal
├── inventario.txt     # Archivo de datos (se crea automáticamente)
└── README.md          # Este archivo
```

---

## 🗂️ Uso de Colecciones

Esta es la parte más importante de la versión 3.0. Se usaron cuatro tipos de colecciones:

### 📘 Diccionario — `self.productos` en `Inventario`
- **Qué es**: una colección que guarda pares clave-valor.
- **Cómo se usa**: la clave es el ID del producto y el valor es el objeto `Producto`.
- **Por qué**: buscar un producto por ID es inmediato (`self.productos[id]`), sin necesidad de recorrer toda la lista uno por uno.

```python
# Añadir al diccionario
self.productos[producto.get_id()] = producto

# Buscar por ID (directo, sin bucle)
producto = self.productos.get(5, None)

# Eliminar por ID
del self.productos[5]
```

### 📗 Conjunto — `self.nombres_registrados` en `Inventario`
- **Qué es**: una colección sin elementos repetidos.
- **Cómo se usa**: guarda los nombres de todos los productos (en minúsculas) para detectar duplicados rápidamente.
- **Por qué**: verificar si un nombre existe en un conjunto es mucho más eficiente que recorrer todos los productos.

```python
# Al añadir
self.nombres_registrados.add(producto.get_nombre().lower())

# Al eliminar
self.nombres_registrados.discard(nombre.lower())

# Para obtener categorías únicas activas
categorias = {p.get_categoria() for p in self.productos.values()}
```

### 📙 Tupla — `CATEGORIAS_VALIDAS` en `producto.py`
- **Qué es**: una colección de elementos que no pueden modificarse.
- **Cómo se usa**: almacena las categorías válidas del sistema.
- **Por qué**: las categorías no deben cambiar durante la ejecución, así que una tupla es más apropiada que una lista.

```python
CATEGORIAS_VALIDAS = ("alimentos", "bebidas", "limpieza", "higiene", "otros")
```

### 📕 Lista — resultados de búsqueda
- **Qué es**: la colección más común en Python.
- **Cómo se usa**: se genera al filtrar productos por nombre o categoría.
- **Por qué**: los resultados de búsqueda son temporales y pueden tener cualquier tamaño.

```python
return [p for p in self.productos.values() if nombre in p.get_nombre().lower()]
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

---

## 📖 Ejemplo de Uso

```
¡Bienvenido al Sistema de Gestión de Inventarios!

📄 Archivo 'inventario.txt' no encontrado. Se creará uno nuevo al añadir el primer producto.

==================================================
🏪  SISTEMA DE GESTIÓN DE INVENTARIOS
==================================================
1. Añadir nuevo producto
...

Seleccione una opción (1-8): 1

--- AÑADIR NUEVO PRODUCTO ---
Ingrese el ID del producto: 1
Ingrese el nombre del producto: Manzanas
Ingrese la cantidad en stock: 50
Ingrese el precio del producto: 2.50
Categorías disponibles:
  1. alimentos
  2. bebidas
  ...
Seleccione una categoría (número): 1
✅ Producto 'Manzanas' añadido y guardado exitosamente.
```

---

## 📄 Formato del Archivo `inventario.txt`

```
# Inventario - formato: id,nombre,cantidad,precio,categoria
1,Manzanas,50,2.5,alimentos
2,Jugo de Naranja,30,1.8,bebidas
3,Detergente,15,4.99,limpieza
```

---

## 🛡️ Manejo de Excepciones

| Excepción | Dónde se maneja | Qué hace el programa |
|---|---|---|
| `FileNotFoundError` | `_cargar_desde_archivo` | Crea el archivo vacío automáticamente |
| `PermissionError` (lectura) | `_cargar_desde_archivo` | Avisa e inicia con inventario vacío |
| `PermissionError` (escritura) | `_guardar_en_archivo` | Avisa que el cambio no se guardó |
| `ValueError` (línea corrupta) | `_cargar_desde_archivo` | Omite la línea y avisa |
| `OSError` | `_guardar_en_archivo` | Avisa del error del sistema de archivos |
| `ValueError` (entrada del usuario) | Funciones de `main.py` | Pide que se ingrese un valor válido |

---

## 👤 Autor

**Jairo Estiven Sayay Alvarez** — Estudiante de Tecnologias de la informacion 
Asignatura: Programacion Orinetada a Objetos

## 📝 Notas

Proyecto v3.0 — mejora de la v2.0 incorporando colecciones de Python (diccionario, conjunto, tupla, lista) para gestionar el inventario de forma más eficiente, más una nueva categoría por producto y nuevas opciones en el menú.
