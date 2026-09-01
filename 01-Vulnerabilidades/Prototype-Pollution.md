---
tipo: vulnerabilidad
vuln: prototype-pollution
tags: [bscp, tipo/vulnerabilidad, vuln/prototype-pollution]
niveles: [apprentice, practitioner]
cheatsheet: "[[CS-Prototype-Pollution]]"
academy: https://portswigger.net/web-security/prototype-pollution
estado: pendiente
---

# Prototype Pollution

## Qué es
Prototype Pollution: contaminar `Object.prototype` para inyectar propiedades globales.

## Cómo detectar
Contamina una propiedad de prueba y verifica en `Object.prototype`.

## Flujo de explotación
Contaminar el prototipo → hallar un gadget que el código lea → encadenar impacto.

## Escalada a impacto
Gadget → XSS en cliente o `isAdmin` en servidor → acceso admin.

## Gotchas de examen
En cliente usa DOM Invader; en servidor prueba `__proto__` y `constructor.prototype`.

## Cheat sheet
[[CS-Prototype-Pollution]]

## Labs
[[_Tracker-Prototype-Pollution]]

## Enlaces
- https://portswigger.net/web-security/prototype-pollution
