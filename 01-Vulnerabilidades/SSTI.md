---
tipo: vulnerabilidad
vuln: ssti
tags: [bscp, tipo/vulnerabilidad, vuln/ssti]
niveles: [apprentice, practitioner]
cheatsheet: "[[CS-SSTI]]"
academy: https://portswigger.net/web-security/server-side-template-injection
estado: pendiente
---

# SSTI

## Qué es
Server-Side Template Injection: la entrada se evalúa como plantilla del servidor.

## Cómo detectar
Prueba expresiones (`{{7*7}}`, `${7*7}`, `<%= 7*7 %>`) y observa si se evalúan.

## Flujo de explotación
Confirmar evaluación → identificar el motor → escalar a lectura de fichero/RCE.

## Escalada a impacto
RCE según el motor para leer `{{SECRET_PATH}}`.

## Gotchas de examen
La sintaxis que evalúe delata el motor (Jinja2, Twig, Freemarker, ERB).

## Cheat sheet
[[CS-SSTI]]

## Labs
[[_Tracker-SSTI]]

## Enlaces
- https://portswigger.net/web-security/server-side-template-injection
