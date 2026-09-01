---
tipo: cheatsheet
vuln: host-header
tags: [bscp, tipo/cheatsheet, vuln/host-header]
relacionada: "[[Host-Header]]"
---

# CS · Host Header

## Flujo repetible
1. Manipula Host / X-Forwarded-Host y observa reflejo o routing.
2. Encadena con reset de contraseña o cache poisoning.

## Detección
```
Cambia Host: {{EXPLOIT}} y observa si se refleja en enlaces/respuesta o cambia el routing.
```

## Plantillas de payload
```
Host: {{EXPLOIT}}                 (poisoning del enlace de reset)
X-Forwarded-Host: {{EXPLOIT}}
Host: localhost                   (funcionalidad interna)
```

## Escalada al objetivo
Envenenar el enlace de reset de {{VICTIM}} para robar su token → toma de cuenta.

## Checklist
- [ ] Probé Host y X-Forwarded-Host
- [ ] Encadené con reset o caché

## Referencias
- https://portswigger.net/web-security/host-header
