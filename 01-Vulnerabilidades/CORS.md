---
tipo: vulnerabilidad
vuln: cors
tags: [bscp, tipo/vulnerabilidad, vuln/cors]
niveles: [apprentice, practitioner]
cheatsheet: "[[CS-CORS]]"
academy: https://portswigger.net/web-security/cors
estado: pendiente
---

# CORS

## Qué es
CORS mal configurado: la app refleja tu Origin y confía en él con credenciales.

## Cómo detectar
Envía `Origin` controlado y observa `Access-Control-Allow-Origin`/`-Credentials`.

## Flujo de explotación
Confirmar reflejo con credenciales → exfiltrar datos autenticados desde `{{EXPLOIT}}`.

## Escalada a impacto
Robar datos sensibles (API keys) de `{{VICTIM}}` para escalar a admin.

## Gotchas de examen
Prueba `Origin: null`, subdominios con XSS y validaciones por prefijo/sufijo.

## Cheat sheet
[[CS-CORS]]

## Labs
[[_Tracker-CORS]]

## Enlaces
- https://portswigger.net/web-security/cors
