---
tipo: vulnerabilidad
vuln: graphql
tags: [bscp, tipo/vulnerabilidad, vuln/graphql]
niveles: [apprentice, practitioner]
cheatsheet: "[[CS-GraphQL]]"
academy: https://portswigger.net/web-security/graphql
estado: pendiente
---

# GraphQL

## Qué es
GraphQL: abusar de introspección, aliasing/batching e IDOR en la API de grafo.

## Cómo detectar
Localiza el endpoint y confirma con `__typename`; corre introspección.

## Flujo de explotación
Encontrar endpoint → introspección → abusar aliasing/batching e IDOR.

## Escalada a impacto
Leer datos de `{{TARGET_USER}}` o forzar credenciales por batching → admin.

## Gotchas de examen
El aliasing salta rate-limits; la introspección puede estar deshabilitada (prueba sugerencias).

## Cheat sheet
[[CS-GraphQL]]

## Labs
[[_Tracker-GraphQL]]

## Enlaces
- https://portswigger.net/web-security/graphql
