---
tipo: vulnerabilidad
vuln: host-header
tags: [bscp, tipo/vulnerabilidad, vuln/host-header]
niveles: [apprentice, practitioner]
cheatsheet: "[[CS-Host-Header]]"
academy: https://portswigger.net/web-security/host-header
estado: pendiente
---

# Host Header

## Qué es
Host Header attacks: la app confía en `Host`/`X-Forwarded-Host` para enlaces o routing.

## Cómo detectar
Manipula `Host`/`X-Forwarded-Host` y observa reflejo en enlaces o cambios de routing.

## Flujo de explotación
Manipular Host → observar reflejo/routing → encadenar con reset o cache poisoning.

## Escalada a impacto
Envenenar el enlace de reset de `{{VICTIM}}` para robar su token.

## Gotchas de examen
Prueba `Host: localhost` para funciones internas y encadena con caché.

## Cheat sheet
[[CS-Host-Header]]

## Labs
[[_Tracker-Host-Header]]

## Enlaces
- https://portswigger.net/web-security/host-header
