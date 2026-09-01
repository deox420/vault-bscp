---
tipo: vulnerabilidad
vuln: dom
tags: [bscp, tipo/vulnerabilidad, vuln/dom]
niveles: [apprentice, practitioner]
cheatsheet: "[[CS-DOM]]"
academy: https://portswigger.net/web-security/dom-based
estado: pendiente
---

# DOM-based

## Qué es
DOM-based: la vulnerabilidad vive en el JavaScript del cliente que lleva una fuente a un sumidero peligroso.

## Cómo detectar
Traza fuentes (`location.hash`, `document.URL`, `postMessage`) hasta sumideros (`innerHTML`, `eval`).

## Flujo de explotación
Identificar fuente→sumidero (DOM Invader) → construir el payload adecuado al sink.

## Escalada a impacto
DOM XSS ejecutado por `{{VICTIM}}` o open redirect para robar tokens.

## Gotchas de examen
El payload depende del sumidero; parte de la entrada puede no salir al servidor.

## Cheat sheet
[[CS-DOM]]

## Labs
[[_Tracker-DOM-Based]]

## Enlaces
- https://portswigger.net/web-security/dom-based
