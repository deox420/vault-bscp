---
tipo: vulnerabilidad
vuln: api
tags: [bscp, tipo/vulnerabilidad, vuln/api]
niveles: [apprentice, practitioner]
cheatsheet: "[[CS-API]]"
academy: https://portswigger.net/web-security/api-testing
estado: pendiente
---

# API Testing

## Qué es
API Testing: enumerar endpoints y abusar de mass assignment y tampering de método/tipo.

## Cómo detectar
Descubre rutas y métodos; prueba verbos alternativos y cambios de Content-Type.

## Flujo de explotación
Descubrir endpoints → mass assignment → method/content-type tampering.

## Escalada a impacto
Mass assignment de rol (`isAdmin`) → admin → borrar usuario / leer `{{SECRET_PATH}}`.

## Gotchas de examen
Busca parámetros ocultos y server-side parameter pollution en la query interna.

## Cheat sheet
[[CS-API]]

## Labs
[[_Tracker-API-Testing]]

## Enlaces
- https://portswigger.net/web-security/api-testing
