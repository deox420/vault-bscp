---
tipo: cheatsheet
vuln: api
tags: [bscp, tipo/cheatsheet, vuln/api]
relacionada: "[[API-Testing]]"
---

# CS · API Testing

## Flujo repetible
1. Descubre endpoints y métodos.
2. Prueba mass assignment y method/content-type tampering.

## Detección
```
Enumera rutas ({{BASE}}/api/...) y prueba métodos alternativos (OPTIONS, PUT) y esquemas.
```

## Plantillas de payload
```
Mass assignment: añadir "isAdmin":true / "role":"admin" al body
Method tampering: GET->POST->PUT · cambiar Content-Type
Server-side parameter pollution en la query interna
```

## Escalada al objetivo
Mass assignment de rol (isAdmin) → acceso admin → borrar usuario / leer {{SECRET_PATH}}.

## Checklist
- [ ] Enumeré endpoints y métodos
- [ ] Probé mass assignment
- [ ] Probé tampering de método/content-type

## Referencias
- https://portswigger.net/web-security/api-testing
