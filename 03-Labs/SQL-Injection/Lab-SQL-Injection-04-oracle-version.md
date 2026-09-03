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
- Capturé la petición del filtro con Burp (Proxy → Repeater).
- Determiné el nº de columnas con `ORDER BY {{N}}` hasta provocar error → 2 columnas.
- Confirmé con `UNION SELECT NULL,NULL` (en Oracle, todo `SELECT` exige `FROM`, p. ej. `FROM dual`).
- Localicé la columna de texto con un marcador (`'a'`) y volqué la versión desde `v$version`.

## Payload usado
Plantilla parametrizada (ver [[CS-SQLi]] → "Versión del motor" / UNION):

    {{CIERRE}} UNION SELECT banner,{{NULL}} FROM v$version{{COMENTARIO}}

## Qué generalizo
- **Oracle:** todo `SELECT` necesita `FROM` → usa `FROM dual`; la versión vive en `v$version`.
- **Nº de columnas:** `ORDER BY {{N}}` hasta el error, y confirma con `UNION SELECT NULL,…`.
- **Columna visible:** inserta un marcador de texto (`'a'`) para ver cuál se refleja en la UI.
- **Concatenar varias filas en una celda (Oracle):** `LISTAGG(col, CHR(10))`.

## Enlace academy
- https://portswigger.net/web-security/sql-injection/examining-the-database/lab-querying-database-version-oracle
