---
tipo: vulnerabilidad
vuln: oauth
tags: [bscp, tipo/vulnerabilidad, vuln/oauth]
niveles: [apprentice, practitioner]
cheatsheet: "[[CS-OAuth]]"
academy: https://portswigger.net/web-security/oauth
estado: pendiente
---

# OAuth

## Qué es
Fallos de OAuth: validación débil de `redirect_uri`, ausencia de `state` y fugas de `code`.

## Cómo detectar
Observa `redirect_uri`, si existe `state` y por dónde puede filtrarse el `code`.

## Flujo de explotación
Trazar el flujo → atacar `redirect_uri`/`state`/fuga de `code`.

## Escalada a impacto
Robar el `code`/token de `{{VICTIM}}` o vincular su cuenta para tomar su sesión.

## Gotchas de examen
Cuida el account linking con email no verificado y el `code` en `Referer`.

## Cheat sheet
[[CS-OAuth]]

## Labs
[[_Tracker-OAuth]]

## Enlaces
- https://portswigger.net/web-security/oauth
