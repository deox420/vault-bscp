---
tipo: vulnerabilidad
vuln: jwt
tags: [bscp, tipo/vulnerabilidad, vuln/jwt]
niveles: [apprentice, practitioner]
cheatsheet: "[[CS-JWT]]"
academy: https://portswigger.net/web-security/jwt
estado: pendiente
---

# JWT

## Qué es
JWT inseguro: firma no verificada o verificable con clave que controlamos.

## Cómo detectar
Decodifica el token y observa `alg`, `kid`, `jwk/jku` y el claim de rol.

## Flujo de explotación
Identificar token → `alg:none`/secreto débil/confusión de algoritmo → forjar token.

## Escalada a impacto
Forjar un token con rol admin (usuario `{{TARGET_USER}}`) para entrar al panel.

## Gotchas de examen
Con `alg:none` deja el punto final; RS256→HS256 usa la pública como secreto HMAC.

## Cheat sheet
[[CS-JWT]]

## Labs
[[_Tracker-JWT]]

## Enlaces
- https://portswigger.net/web-security/jwt
