---
tipo: vulnerabilidad
vuln: nosqli
tags: [bscp, tipo/vulnerabilidad, vuln/nosqli]
niveles: [apprentice, practitioner]
cheatsheet: "[[CS-NoSQLi]]"
academy: https://portswigger.net/web-security/nosql-injection
estado: pendiente
---

# NoSQL Injection

## Qué es
NoSQL Injection: inyectar operadores/sintaxis de la base NoSQL (p. ej. MongoDB).

## Cómo detectar
Inyecta comillas y operadores (`$ne`, `$regex`) y observa cambios de respuesta.

## Flujo de explotación
Inyectar sintaxis Mongo → operadores para bypass o extracción ciega.

## Escalada a impacto
Bypass de login como `{{TARGET_USER}}` o extracción ciega de credenciales.

## Gotchas de examen
Distingue inyección en sintaxis (string) de inyección en operadores (JSON).

## Cheat sheet
[[CS-NoSQLi]]

## Labs
[[_Tracker-NoSQL-Injection]]

## Enlaces
- https://portswigger.net/web-security/nosql-injection
