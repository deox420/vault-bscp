---
tipo: lab
vuln: sqli
nivel: practitioner
tags: [bscp, tipo/lab, vuln/sqli, nivel/practitioner, estado/resuelto]
fase: [1-acceso]
url: https://portswigger.net/web-security/sql-injection/examining-the-database/lab-querying-database-version-mysql-microsoft
estado: resuelto
---

# SQL Injection · Lab 05 — MySQL & Microsoft DB version (practitioner) ✅

## Objetivo
Obtener el tipo y la versión del motor de base de datos (MySQL o Microsoft SQL Server) mediante una inyección UNION en el filtro de categoría.

## Fase(s)
- 1-acceso

## Pasos realizados
- Capturé la petición del filtro con Burp y determiné el número de columnas usando `ORDER BY` (error en 3 → 2 columnas).
- Construí una carga UNION que funciona para MySQL (`@@version`) y para Microsoft (`@@VERSION`).
- Identifiqué la columna visible mediante un marcador de texto (`'a'`) y verifiqué que la versión se muestra en la UI.

## Payload usado (solución real)
```
'+UNION SELECT NULL, @@version--
```
- En Microsoft SQL Server el mismo payload también funciona ya que `@@VERSION` es aceptado.

## Qué generalizo
- **MySQL / Microsoft:** la versión del motor está disponible como variable del sistema (`@@version` o `@@VERSION`).
- **Número de columnas:** usar `ORDER BY` hasta el error para encontrar cuántas columnas necesita la UNION.
- **Columna visible:** insertar un marcador (`'a'`) para determinar cuál se refleja.

## Enlace academy
- https://portswigger.net/web-security/sql-injection/examining-the-database/lab-querying-database-version-mysql-microsoft
