---
tipo: lab
vuln: sqli
nivel: apprentice
tags: [bscp, tipo/lab, vuln/sqli, nivel/apprentice, estado/resuelto]
fase: [1-acceso]
url: https://portswigger.net/web-security/sql-injection/lab-retrieve-hidden-data
estado: resuelto
---

# SQL Injection · Lab 02 — WHERE clause, retrieval of hidden data (apprentice) ✅

## Objetivo
Revelar filas que la app intenta ocultar manipulando un filtro que acaba en una cláusula `WHERE`.

## Fase(s)
- 1-acceso

## Pasos realizados
- Identifiqué que `{{PARAM}}` (un filtro de categoría) se refleja en un `WHERE`.
- Rompí la condición del filtro para que devolviera también las filas ocultas.
- *(Payload parametrizado, sin valores concretos del lab — ver [[CS-SQLi]].)*

## Payload usado (solución real)
En el filtro de categoría (parámetro `category`):

```
'+OR+1=1--
```

También sirve para una categoría concreta: `Gifts'--` (comenta el `AND released = 1` y muestra los no publicados).

## Qué generalizo
- Un **filtro reflejado en un `WHERE`** (categoría, estado, visibilidad) es candidato a SQLi: se inyecta para **neutralizar la condición** y aflorar filas ocultas.
- **Señal de detección:** cambiar `{{PARAM}}` altera el conjunto de resultados de forma inesperada.

## Enlace academy
- https://portswigger.net/web-security/sql-injection/lab-retrieve-hidden-data
