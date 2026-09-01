---
tipo: cheatsheet
vuln: smuggling
tags: [bscp, tipo/cheatsheet, vuln/smuggling]
relacionada: "[[Request-Smuggling]]"
---

# CS · Request Smuggling

## Flujo repetible
1. Detecta desincronización por timing (extensión HTTP Request Smuggler).
2. Clasifica CL.TE / TE.CL / TE.TE / CL.0.
3. Explota: capturar petición ajena o saltar controles front-end.

## Detección
```
# Sonda de timing: petición con TE ambiguo que retrasa la respuesta => desync
# Usa la extensión "HTTP Request Smuggler" sobre {{BASE}}
```

## Plantillas de payload
```
# CL.TE (esquema)
Content-Length: 6
Transfer-Encoding: chunked
0
X
```
```
# TE.TE (ofuscación del header)
Transfer-Encoding: chunked
Transfer-Encoding: x
```

## Escalada al objetivo
Capturar la petición de {{VICTIM}} (robar cookie admin) o bypass de /admin.

## Checklist
- [ ] Confirmé desincronización
- [ ] Clasifiqué la variante
- [ ] Capturé datos de otro usuario / salté control

## Referencias
- https://portswigger.net/web-security/request-smuggling
