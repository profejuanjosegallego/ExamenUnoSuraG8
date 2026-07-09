# Taller evaluativo #1 🎾

Envio: https://forms.gle/Ket62ZmuhoxntjRo9

## Contexto
Una academia deportiva necesita un prototipo en Python para gestionar información básica de jugadores de tenis y el registro de sus partidos.  
El objetivo del taller es practicar **listas**, **diccionarios**, **métodos de listas** y **funciones (`def`)**, junto con un flujo simple de **registro/login con intentos limitados**.

---

## Objetivo de aprendizaje
Al finalizar, el estudiante será capaz de:
- Construir soluciones con **funciones** y flujo de control.
- Gestionar **listas** con métodos: `append`, `insert`, `remove`, `pop`, `sort`.
- Trabajar con **lista de diccionarios** (mínimo 10 registros).
- Implementar un **login/registro** con control de intentos e información al usuario.
- Generar y procesar datos relacionados con el desempeño de jugadores de tenis.

---

## Requisitos del ejercicio

### 1) Registro y Login (con 3 intentos)
Implementa un sistema que permita:

**Registro**
- Permitir crear un usuario con:
  - `correo`
  - `password`
- Guardar el usuario registrado en una estructura simple (diccionario o lista de diccionarios).

**Login**
- Pedir correo y contraseña.
- Permitir **máximo 3 intentos**.
- En cada intento fallido debe mostrar:
  - `"Credenciales incorrectas. Intentos restantes: X"`
- Si inicia sesión correctamente, mostrar:
  - `"Login exitoso"` y permitir continuar con el menú.
- Si se agotan los intentos:
  - `"Cuenta bloqueada temporalmente"` y finalizar el programa.

---

### 2) Registro de N diccionarios (lista de diccionarios)
Crear una lista llamada `jugadores_tenis` que contenga **10 diccionarios**, cada uno con esta estructura mínima:

- `id` (int)
- `nombre` (str)
- `pais` (str)
- `edad` (int)
- `partidosGanados` (crear un listado numérico de los partidos ganados en diferentes torneos o temporadas)
- `estado` (str: "ACTIVO" o "LESIONADO")

Debe existir un menú para:
- Mostrar todos los jugadores registrados
- Ordenar jugadores por cantidad de partidos ganados de menor a mayor

---

## Funciones obligatorias
Tu solución debe estar organizada usando funciones `def`.

---

## Menú sugerido (después del login)
1. Gestionar jugadores de tenis
2. Salir

---

## Criterios de evaluación (guía)
- (30%) Incluir diseño de los módulos a programar
- (30%) Implementación de las funciones
- (10%) Unificación de todo en un menú
- (30%) Correcto uso de Git y GitHub

---

Éxitos. La idea es que sea sencillo, completo y bien organizado.
