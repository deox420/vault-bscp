---
tipo: vulnerabilidad
vuln: access-control
tags: [bscp, tipo/vulnerabilidad, vuln/access-control]
niveles: [apprentice, practitioner]
cheatsheet: "[[CS-Access-Control]]"
academy: https://portswigger.net/web-security/access-control
estado: pendiente
---

# Access Control

## Qué es
Access Control roto: falta de comprobación de autorización en rutas o recursos.

## Cómo detectar
Prueba rutas admin directas, IDOR en identificadores y manipulación de rol.

## Flujo de explotación
Mapear roles/rutas → forced browsing/IDOR/manipular rol o headers de bypass.

## Escalada a impacto
Escalar a admin para borrar usuario o leer `{{SECRET_PATH}}`.

## Gotchas de examen
Prueba `X-Original-URL`, cambios de método y variaciones de mayúsculas en la ruta.

## Cheat sheet
[[CS-Access-Control]]

## Labs
[[_Tracker-Access-Control]]

## Enlaces
- https://portswigger.net/web-security/access-control
