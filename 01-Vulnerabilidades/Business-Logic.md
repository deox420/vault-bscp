---
tipo: vulnerabilidad
vuln: business-logic
tags: [bscp, tipo/vulnerabilidad, vuln/business-logic]
niveles: [apprentice, practitioner]
cheatsheet: "[[CS-Business-Logic]]"
academy: https://portswigger.net/web-security/logic-flaws
estado: pendiente
---

# Business Logic

## Qué es
Business Logic: fallos por suposiciones incorrectas del desarrollador sobre el flujo.

## Cómo detectar
Lista las suposiciones de cada flujo y comprueba si el servidor confía en el cliente.

## Flujo de explotación
Enumerar suposiciones → romperlas una a una (valores, orden de pasos, campos de confianza).

## Escalada a impacto
Comprar gratis, elevar rol o acceder a funciones de `{{TARGET_USER}}`.

## Gotchas de examen
Prueba valores negativos/desbordamiento, saltar pasos y reaplicar cupones.

## Cheat sheet
[[CS-Business-Logic]]

## Labs
[[_Tracker-Business-Logic]]

## Enlaces
- https://portswigger.net/web-security/logic-flaws
