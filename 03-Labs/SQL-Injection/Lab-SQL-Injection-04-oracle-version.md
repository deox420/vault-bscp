---
tipo: lab
vuln: sqli
nivel: practitioner
tags: [bscp, tipo/lab, vuln/sqli, nivel/practitioner, estado/resuelto]
fase: [1-acceso]
url: {{LAB_URL}}
estado: resuelto
---

# SQL Injection · Lab 04 — Oracle version query (practitioner) ✅

## Objetivo
Obtener la cadena completa que muestra la versión y el tipo de la base de datos Oracle mediante una vulnerabilidad SQL Injection en el filtro de categoría.

## Fase(s)
- 1-acceso

## Pasos realizados
- Capturé la petición `GET /filter?category=…` con Burp Suite.
- Determiné que la consulta original devuelve **2 columnas** mediante pruebas `ORDER BY`.
- Construí una inyección `UNION SELECT` con `NULL` en la segunda columna para validar el número de columnas.
- Identifiqué que la **primera columna** era la que la UI mostraba (prueba con `'X'`).
- Sustituí esa columna por una sub‑consulta que concatena todas las filas de `v$version` usando `LISTAGG` y `CHR(10)`, logrando que la respuesta incluya todas las líneas de la versión.
- La petición final que resolvió el lab fue:

```
GET /filter?category=' UNION SELECT (SELECT LISTAGG(banner,CHR(10)) WITHIN GROUP (ORDER BY rownum) FROM v$version),NULL FROM dual--+ HTTP/2
```

## Payload usado
```text
{{CIERRE}} UNION SELECT (SELECT LISTAGG(banner,CHR(10)) WITHIN GROUP (ORDER BY rownum) FROM v$version),{{NULL}} FROM dual{{COMENTARIO}}
```
*(placeholders: `{{CIERRE}}` = `'`, `{{NULL}}` = `NULL`, `{{COMENTARIO}}` = `-- `) – nunca se incluye el valor real del lab.

## Qué generalizo
- **Uso de `LISTAGG`** para concatenar múltiples filas de una vista (`v$version`) en una sola cadena cuando la salida de la inyección debe contener varias líneas.
- **Detección del número de columnas** mediante `ORDER BY` y validación con `UNION SELECT NULL,…`.
- **Identificación de la columna visible** insertando un marcador (`'X'`) y observando cuál aparece en la UI.

## Enlace academy
{{LAB_URL}}
