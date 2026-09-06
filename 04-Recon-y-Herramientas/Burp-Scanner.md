---
tipo: recurso
tags: [bscp, tipo/recurso]
---

# Burp Scanner (uso en el examen)

## Flujo repetible
1. Define el scope en `{{BASE}}` y activa el proxy.
2. Navega la app para poblar el site map (mejor cobertura del crawl).
3. Lanza un **scan** (crawl + audit) sobre el host objetivo.
4. Mientras escanea, sigue probando a mano con las cheat sheets.
5. Revisa la pestaña **Issues**: confirma cada hallazgo manualmente antes de explotarlo.

## Buenas prácticas
- Corre el scanner desde el minuto uno en ambas apps.
- Prioriza issues de severidad alta que encajen con el objetivo (SQLi, XSS, access control).
- No te fíes de falsos positivos: reproduce el issue en Repeater.
- Combina con Collaborator (`{{COLLAB}}`) para detectar vulnerabilidades ciegas.

## Extensiones útiles
- HTTP Request Smuggler, Param Miner, JWT Editor, InQL, DOM Invader, Turbo Intruder.
- Guía de uso para el examen → [[Extensiones-Burp]].

## Enlaces
- [[MOC-BSCP]]
- https://portswigger.net/burp/documentation/scanner
