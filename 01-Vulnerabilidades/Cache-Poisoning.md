---
tipo: vulnerabilidad
vuln: cache-poisoning
tags: [bscp, tipo/vulnerabilidad, vuln/cache-poisoning]
niveles: [practitioner]
cheatsheet: "[[CS-Cache-Poisoning]]"
academy: https://portswigger.net/web-security/web-cache-poisoning
estado: pendiente
---

# Cache Poisoning

## Qué es
Web Cache Poisoning: envenenar la caché con una respuesta maliciosa vía inputs no incluidos en la clave.

## Cómo detectar
Añade headers no incluidos en la clave y observa si se reflejan; usa cache buster.

## Flujo de explotación
Hallar input no incluido en la clave → reflejar payload → forzar el guardado en caché.

## Escalada a impacto
Servir XSS/redirect cacheado a todas las víctimas, incluido `{{VICTIM}}`.

## Gotchas de examen
Trabaja con cache buster mientras pruebas para no envenenar entradas reales.

## Cheat sheet
[[CS-Cache-Poisoning]]

## Labs
[[_Tracker-Cache-Poisoning]]

## Enlaces
- https://portswigger.net/web-security/web-cache-poisoning
