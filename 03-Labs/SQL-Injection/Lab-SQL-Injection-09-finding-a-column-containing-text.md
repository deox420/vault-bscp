---
tipo: lab
vuln: sqli
nivel: practitioner
tags: [bscp, tipo/lab, vuln/sqli, nivel/practitioner, estado/resuelto]
fase: [1-acceso]
url: https://portswigger.net/web-security/sql-injection/lab-finding-a-column-containing-text
estado: resuelto
orden: 90
fecha: 2026-09-08
---

# SQL Injection · Lab 09 — Finding a column containing text (practitioner) ✅

## Objetivo
Identificar cuál de las columnas devueltas por la consulta vulnerable acepta datos de tipo texto, usando un valor aleatorio proporcionado por el lab.

## Fase(s)
- 1-acceso

## Pasos realizados
1. Detecté la vulnerabilidad con una comilla simple (`'`) en el parámetro `category`.
2. Utilicé `ORDER BY` para confirmar que la consulta original tiene **3 columnas** (error al usar `ORDER BY 4`).
3. Probé `UNION SELECT` colocando el valor aleatorio provisto (`tFmGnR`) en cada posición hasta que apareció en la UI. La posición que mostró el string corresponde a la columna de texto.
4. Payload final que confirmó la columna de texto:
   ```
   GET /filter?category=Pets+' UNION SELECT NULL,'tFmGnR',NULL-- HTTP/2
   ```
   La respuesta mostró `tFmGnR`, indicando que la segunda columna acepta texto.

## Payload usado (solución real)
```
GET /filter?category=Pets+' UNION SELECT NULL,'tFmGnR',NULL-- HTTP/2
```

## Qué generalizo
- **Encontrar columna de texto:** usar `UNION SELECT 'a',NULL,NULL--` (o colocar el valor aleatorio en cada posición) para descubrir cuál columna de la consulta original es la visible y acepta texto. Esta técnica permite luego volcar datos arbitrarios.

## Enlace academy
- https://portswigger.net/web-security/sql-injection/lab-finding-a-column-containing-text