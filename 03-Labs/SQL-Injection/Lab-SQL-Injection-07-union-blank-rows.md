---
tipo: lab
vuln: sqli
nivel: practitioner
tags: [bscp, tipo/lab, vuln/sqli, nivel/practitioner, estado/resuelto]
fase: [1-acceso]
url: https://portswigger.net/web-security/sql-injection/lab-union-blank-rows
estado: resuelto
orden: 70
fecha: 2026-09-08
---

# SQL Injection · Lab 07 — UNION attack, determining the number of columns returned by the query (practitioner) ✅

## Objetivo
Determinar el número de columnas devueltas por la consulta mediante un ataque UNION que devuelve una fila con valores `NULL`.

## Fase(s)
- 1-acceso

## Pasos realizados
1. Detecté la vulnerabilidad con una comilla simple (`'`) en el parámetro `category`.
2. Utilicé `ORDER BY` para probar los valores y confirmé que la consulta original tiene **3 columnas** (error al usar `ORDER BY 4`).
3. Ejecuté un payload UNION que devuelve tres valores `NULL` para validar el número de columnas:
   ```
   GET /filter?category=Corporate+gifts+' UNION SELECT NULL,NULL,NULL-- HTTP/2
   ```

## Payload usado (solución real)
```
GET /filter?category=Corporate+gifts+' UNION SELECT NULL,NULL,NULL-- HTTP/2
```

## Qué generalizo
- Para determinar el número de columnas en una consulta vulnerable a SQLi, usar `ORDER BY N` hasta generar un error, o probar `UNION SELECT NULL,…` con la cantidad de `NULL` coincidente con el número de columnas.
- El primer `NULL` suele mapearse a la columna visible en la UI; los valores adicionales pueden emplearse para extraer datos una vez descubierta la estructura.

## Enlace academy
- https://portswigger.net/web-security/sql-injection/lab-union-blank-rows