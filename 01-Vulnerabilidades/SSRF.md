---
tipo: vulnerabilidad
vuln: ssrf
tags: [bscp, tipo/vulnerabilidad, vuln/ssrf]
niveles: [apprentice, practitioner]
cheatsheet: "[[CS-SSRF]]"
academy: https://portswigger.net/web-security/ssrf
estado: pendiente
---

# SSRF

## Qué es
Server-Side Request Forgery: el servidor hace una petición a una URL que controlamos.

## Cómo detectar
Busca parámetros que acepten URL/host y apunta a localhost, red interna o metadata.

## Flujo de explotación
Localizar `{{PARAM}}` URL → apuntar a interno → si hay filtro, ofuscar; si es ciego, `{{COLLAB}}`.

## Escalada a impacto
Alcanzar la interfaz admin interna para una acción privilegiada o leer metadata cloud.

## Gotchas de examen
Notaciones alternativas (`127.1`, decimal, IPv6) y trucos con `@`/`#` para saltar filtros.

## Cheat sheet
[[CS-SSRF]]

## Labs
[[_Tracker-SSRF]]

## Enlaces
- https://portswigger.net/web-security/ssrf
