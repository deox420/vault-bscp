---
tipo: cheatsheet
vuln: business-logic
tags: [bscp, tipo/cheatsheet, vuln/business-logic]
relacionada: "[[Business-Logic]]"
---

# CS · Business Logic

## Flujo repetible
1. Lista las suposiciones del desarrollador en cada flujo.
2. Rompe una por una (cliente controla lo que no debería).

## Detección
```
Revisa cada campo enviado ({{PARAM}}): precio, cantidad, rol, pasos. ¿El servidor confía en el cliente?
```

## Plantillas de payload
```
Cantidades/precios negativos o desbordamiento
Saltar pasos del flujo (ir directo a confirmar)
Reaplicar cupones/descuentos
Confianza excesiva en datos del cliente (rol, precio)
Parámetros ocultos / mass assignment
```

## Escalada al objetivo
Abusar de la lógica para comprar gratis, elevar rol o acceder a funciones de {{TARGET_USER}}.

## Checklist
- [ ] Probé valores fuera de rango
- [ ] Probé saltar/reordenar pasos
- [ ] Probé manipular campos de confianza

## Referencias
- https://portswigger.net/web-security/logic-flaws
