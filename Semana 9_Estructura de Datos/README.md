# 📦 Sistema de Gestión de Inventarios

Sistema simple de gestión de inventarios para una tienda, desarrollado en Python utilizando Programación Orientada a Objetos (POO).

## 📋 Descripción

Este proyecto permite gestionar el inventario de una tienda mediante una interfaz de consola interactiva. El usuario puede añadir, eliminar, actualizar y buscar productos de forma sencilla.

## 🚀 Funcionalidades

- ✅ **Añadir productos**: Registrar nuevos productos con ID único, nombre, cantidad y precio
- ❌ **Eliminar productos**: Remover productos del inventario por su ID
- 🔄 **Actualizar productos**: Modificar la cantidad o precio de productos existentes
- 🔍 **Buscar productos**: Encontrar productos por nombre (búsqueda parcial)
- 📊 **Mostrar inventario**: Ver todos los productos registrados

## 📁 Estructura del Proyecto

```
sistema-inventarios/
│
├── producto.py       # Clase Producto con sus atributos y métodos
├── inventario.py     # Clase Inventario con la lógica de gestión
├── main.py          # Programa principal con menú interactivo
└── README.md        # Este archivo
```

## 🛠️ Requisitos

- Python 3.6 o superior
- PyCharm (recomendado) o cualquier IDE de Python

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

3. **Usar el menú interactivo**: Sigue las instrucciones en pantalla para gestionar tu inventario

## 📖 Ejemplo de Uso

```
🏪  SISTEMA DE GESTIÓN DE INVENTARIOS
==================================================
1. Añadir nuevo producto
2. Eliminar producto
3. Actualizar producto
4. Buscar producto por nombre
5. Mostrar todos los productos
6. Salir
==================================================

Seleccione una opción (1-6): 1

--- AÑADIR NUEVO PRODUCTO ---
Ingrese el ID del producto: 1
Ingrese el nombre del producto: Manzanas
Ingrese la cantidad en stock: 50
Ingrese el precio del producto: 2.50
✅ Producto 'Manzanas' añadido exitosamente
```

## 🏗️ Clases y Métodos

### Clase Producto
- **Atributos**: `id`, `nombre`, `cantidad`, `precio`
- **Métodos**: 
  - Getters: `get_id()`, `get_nombre()`, `get_cantidad()`, `get_precio()`
  - Setters: `set_nombre()`, `set_cantidad()`, `set_precio()`

### Clase Inventario
- **Atributos**: `productos` (lista)
- **Métodos**:
  - `añadir_producto()`: Añade un producto verificando ID único
  - `eliminar_producto()`: Elimina un producto por ID
  - `actualizar_producto()`: Actualiza cantidad o precio
  - `buscar_por_nombre()`: Busca productos por nombre
  - `mostrar_todos()`: Muestra todos los productos

## 🎓 Objetivos de Aprendizaje

Este proyecto ayuda a practicar:
- Programación Orientada a Objetos (POO)
- Estructuras de datos (listas)
- Manejo de entrada/salida en consola
- Validación de datos
- Uso de Git y GitHub
- Documentación de código

## 👤 Autor

[Jairo Estiven Sayay Alvarez] - Estudiante de Programación

## 📝 Notas

Proyecto desarrollado como parte de un ejercicio de aprendizaje de Python y POO.
