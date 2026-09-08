---
tipo: vulnerabilidad
vuln: sqli
tags: [bscp, tipo/vulnerabilidad, vuln/sqli]
niveles: [apprentice, practitioner]
cheatsheet: "[[CS-SQLi]]"
academy: https://portswigger.net/web-security/sql-injection
estado: en-progreso
---

# SQL Injection

## Qué es
Inyección de SQL: entrada del usuario que se concatena en una consulta y altera su lógica.

## Cómo detectar
Comilla simple que rompe la query, operadores booleanos con respuestas distintas, y retardos por tiempo.

## Flujo de explotación
Detectar → determinar contexto y motor → UNION/error/blind → enumerar esquema → extraer credenciales.

## Escalada a impacto
Robar credenciales de `{{TARGET_USER}}` para iniciar sesión como admin y cumplir el objetivo.

## Gotchas de examen
Cuida los comentarios según motor (`--`, `#`, `--+`), el número exacto de columnas y el tipo de dato.

## Qué generalizo
- Un **filtro reflejado en un `WHERE`** (categoría/estado/visibilidad) es candidato a SQLi: se inyecta para **neutralizar la condición** y revelar filas ocultas. *(Lab [[Lab-SQL-Injection-02-where-clause-hidden-data]], apprentice ✅)*
- **Bypass de login:** cerrar la cadena, `OR 1=1` y comentar el resto (`--`) salta la comprobación de contraseña y entra como `{{TARGET_USER}}`. *(Lab [[Lab-SQL-Injection-03-login-bypass]], apprentice ✅)*
- **Enumerar versión (Oracle):** `UNION SELECT banner,NULL FROM v$version` (Oracle exige `FROM`); nº de columnas con `ORDER BY`. *(Lab [[Lab-SQL-Injection-04-oracle-version]], practitioner ✅)
- **Enumerar versión (MySQL / Microsoft):** `UNION SELECT NULL, @@version` (MySQL) o `UNION SELECT NULL, @@VERSION` (Microsoft); nº de columnas con `ORDER BY`. *(Lab [[Lab-SQL-Injection-05-mysql-microsoft-version]], practitioner ✅)*

## Cheat sheet
[[CS-SQLi]]

## Labs
[[_Tracker-SQL-Injection]]

## Enlaces
- https://portswigger.net/web-security/sql-injection
