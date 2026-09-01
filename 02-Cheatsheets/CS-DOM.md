---
tipo: cheatsheet
vuln: dom
tags: [bscp, tipo/cheatsheet, vuln/dom]
relacionada: "[[DOM-Based]]"
---

# CS · DOM-based

## Flujo repetible
1. Traza fuentes controlables hasta sumideros peligrosos (usa DOM Invader).
2. Inyecta según el sumidero.

## Detección
```
Fuentes: location(.hash/.search), document.URL, referrer, postMessage
Sumideros: innerHTML, document.write, eval, setTimeout, location, srcdoc
```

## Plantillas de payload
```
Ejemplo: #<img src=x onerror=alert(1)>   (hash -> innerHTML)
{{PARAM}} controlado -> sumidero (elige el payload según el sink)
```

## Escalada al objetivo
DOM XSS ejecutado por {{VICTIM}} → robo de sesión / acción autenticada; también open redirect.

## Checklist
- [ ] Identifiqué fuente->sumidero
- [ ] Ejecuté según el sumidero
- [ ] Revisé DOM open redirect

## Referencias
- https://portswigger.net/web-security/dom-based
