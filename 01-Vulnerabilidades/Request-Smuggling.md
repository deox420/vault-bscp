---
tipo: vulnerabilidad
vuln: smuggling
tags: [bscp, tipo/vulnerabilidad, vuln/smuggling]
niveles: [practitioner]
cheatsheet: "[[CS-Smuggling]]"
academy: https://portswigger.net/web-security/request-smuggling
estado: pendiente
---

# Request Smuggling

## Qué es
HTTP Request Smuggling: desincronizar front-end y back-end sobre dónde acaba una petición.

## Cómo detectar
Sonda de timing con `Transfer-Encoding`/`Content-Length` ambiguos (HTTP Request Smuggler).

## Flujo de explotación
Detectar desync → clasificar CL.TE/TE.CL/TE.TE/CL.0 → capturar petición ajena o saltar controles.

## Escalada a impacto
Capturar la petición de `{{VICTIM}}` (robar su cookie de admin) o bypass de `/admin`.

## Gotchas de examen
Cuida los CRLF exactos y usa HTTP/1.1; el single-packet no aplica aquí.

## Cheat sheet
[[CS-Smuggling]]

## Labs
[[_Tracker-Request-Smuggling]]

## Enlaces
- https://portswigger.net/web-security/request-smuggling
