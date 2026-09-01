---
tipo: cheatsheet
vuln: oauth
tags: [bscp, tipo/cheatsheet, vuln/oauth]
relacionada: "[[OAuth]]"
---

# CS · OAuth

## Flujo repetible
1. Traza el flujo (authorization code / implicit).
2. Ataca redirect_uri, state y fuga de code.

## Detección
```
Observa el parámetro redirect_uri y si existe state en la petición de {{BASE}}.
```

## Plantillas de payload
```
redirect_uri manipulable -> robar code/token hacia {{EXPLOIT}}
falta de state (CSRF)    -> vincular cuenta de {{VICTIM}} a la tuya
fuga de code vía Referer
email no verificado / account linking inseguro
```

## Escalada al objetivo
Robar el code/token de {{VICTIM}} o vincular su cuenta → acceso a su sesión → admin.

## Checklist
- [ ] Probé redirect_uri alterado
- [ ] Probé ausencia de state
- [ ] Revisé fugas del code

## Referencias
- https://portswigger.net/web-security/oauth
