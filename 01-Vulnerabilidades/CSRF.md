---
tipo: vulnerabilidad
vuln: csrf
tags: [bscp, tipo/vulnerabilidad, vuln/csrf]
niveles: [apprentice, practitioner]
cheatsheet: "[[CS-CSRF]]"
academy: https://portswigger.net/web-security/csrf
estado: pendiente
---

# CSRF

## Qué es
Cross-Site Request Forgery: forzar al navegador de la víctima a enviar una petición de cambio de estado.

## Cómo detectar
Comprueba si la acción exige token anti-CSRF, si está ligado a sesión y la política SameSite.

## Flujo de explotación
Elegir acción con estado → analizar la defensa → PoC auto-enviada desde `{{EXPLOIT}}`.

## Escalada a impacto
Cambiar email/contraseña de `{{VICTIM}}` para tomar la cuenta.

## Gotchas de examen
Prueba quitar token, POST→GET, token no ligado a sesión o en cookie, y SameSite Lax con GET.

## Cheat sheet
[[CS-CSRF]]

## Labs
[[_Tracker-CSRF]]

## Enlaces
- https://portswigger.net/web-security/csrf
