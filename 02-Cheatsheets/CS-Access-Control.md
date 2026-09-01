---
tipo: cheatsheet
vuln: access-control
tags: [bscp, tipo/cheatsheet, vuln/access-control]
relacionada: "[[Access-Control]]"
---

# CS · Access Control

## Flujo repetible
1. Mapea roles y rutas privilegiadas.
2. Prueba acceso directo, IDOR y manipulación de rol.

## Detección
```
/admin                       (forced browsing: ¿accesible sin privilegios?)
GET /api/users/{{N}}         (¿devuelve datos ajenos?)
```

## Plantillas de payload
```
/admin                       (forced browsing)
id={{N}} -> id={{N+1}}       (IDOR)
role/isAdmin en cookie/body  (manipular)
X-Original-URL: /admin       (bypass front-end)
método POST->GET, caso /Admin
```

## Escalada al objetivo
IDOR para leer datos ajenos · escalada de rol → admin → borrar usuario / leer {{SECRET_PATH}}.

## Checklist
- [ ] Probé rutas admin directas
- [ ] Probé IDOR en identificadores
- [ ] Probé manipular rol y headers de bypass

## Referencias
- https://portswigger.net/web-security/access-control
