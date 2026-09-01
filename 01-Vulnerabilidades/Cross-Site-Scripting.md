---
tipo: vulnerabilidad
vuln: xss
tags: [bscp, tipo/vulnerabilidad, vuln/xss]
niveles: [apprentice, practitioner]
cheatsheet: "[[CS-XSS]]"
academy: https://portswigger.net/web-security/cross-site-scripting
estado: pendiente
---

# Cross-Site Scripting

## Qué es
Cross-Site Scripting: la app refleja/almacena entrada que se ejecuta como JavaScript en el navegador de la víctima.

## Cómo detectar
Inyecta un marcador único y busca dónde y en qué contexto aparece (HTML, atributo, JS, URL).

## Flujo de explotación
Localizar reflexión → identificar contexto → romperlo → entregar vía `{{EXPLOIT}}` a `{{VICTIM}}`.

## Escalada a impacto
Ejecución en el navegador del admin → robo de sesión o acción autenticada (cambio de email).

## Gotchas de examen
Revisa CSP, codificación de salida y filtros; a veces basta un evento sin `script`.

## Cheat sheet
[[CS-XSS]]

## Labs
[[_Tracker-Cross-Site-Scripting]]

## Enlaces
- https://portswigger.net/web-security/cross-site-scripting
