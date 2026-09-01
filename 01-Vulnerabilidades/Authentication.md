---
tipo: vulnerabilidad
vuln: auth
tags: [bscp, tipo/vulnerabilidad, vuln/auth]
niveles: [apprentice, practitioner]
cheatsheet: "[[CS-Auth]]"
academy: https://portswigger.net/web-security/authentication
estado: pendiente
---

# Authentication

## Qué es
Fallos de autenticación: enumeración, fuerza bruta, 2FA y flujos de reset débiles.

## Cómo detectar
Diferencias de respuesta/tiempo para enumerar usuarios; comportamiento del 2FA y del reset.

## Flujo de explotación
Enumerar → fuerza bruta con Intruder → atacar 2FA/reset/persistencia de sesión.

## Escalada a impacto
Comprometer `{{TARGET_USER}}` para acceder al panel admin.

## Gotchas de examen
Revisa saltar al endpoint post-2FA, tokens de reset predecibles y Host header poisoning.

## Cheat sheet
[[CS-Auth]]

## Labs
[[_Tracker-Authentication]]

## Enlaces
- https://portswigger.net/web-security/authentication
