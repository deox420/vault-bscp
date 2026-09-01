---
tipo: vulnerabilidad
vuln: clickjacking
tags: [bscp, tipo/vulnerabilidad, vuln/clickjacking]
niveles: [apprentice, practitioner]
cheatsheet: "[[CS-Clickjacking]]"
academy: https://portswigger.net/web-security/clickjacking
estado: pendiente
---

# Clickjacking

## Qué es
Clickjacking: superponer la app objetivo en un iframe invisible para robar clics de la víctima.

## Cómo detectar
Comprueba si la página se puede enmarcar (falta `X-Frame-Options`/`frame-ancestors`).

## Flujo de explotación
Confirmar framing → alinear un señuelo sobre el control sensible → engañar a `{{VICTIM}}`.

## Escalada a impacto
La víctima ejecuta sin querer una acción sensible (cambiar email, borrar cuenta).

## Gotchas de examen
Ajusta el offset del señuelo; algunas acciones requieren pre-rellenar campos vía URL.

## Cheat sheet
[[CS-Clickjacking]]

## Labs
[[_Tracker-Clickjacking]]

## Enlaces
- https://portswigger.net/web-security/clickjacking
