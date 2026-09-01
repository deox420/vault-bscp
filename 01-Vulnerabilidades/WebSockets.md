---
tipo: vulnerabilidad
vuln: websockets
tags: [bscp, tipo/vulnerabilidad, vuln/websockets]
niveles: [apprentice, practitioner]
cheatsheet: "[[CS-WebSockets]]"
academy: https://portswigger.net/web-security/websockets
estado: pendiente
---

# WebSockets

## Qué es
WebSockets: canal bidireccional que puede transportar inyecciones y sufrir CSWSH.

## Cómo detectar
Intercepta el handshake y los mensajes; comprueba si valida `Origin`.

## Flujo de explotación
Interceptar/manipular mensajes → probar XSS/SQLi → CSWSH si no valida Origin.

## Escalada a impacto
CSWSH sobre la sesión de `{{VICTIM}}` para leer sus datos y escalar.

## Gotchas de examen
La sesión sólo por cookie sin validar Origin habilita el hijacking desde `{{EXPLOIT}}`.

## Cheat sheet
[[CS-WebSockets]]

## Labs
[[_Tracker-WebSockets]]

## Enlaces
- https://portswigger.net/web-security/websockets
