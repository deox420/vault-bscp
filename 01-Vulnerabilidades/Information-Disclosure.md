---
tipo: vulnerabilidad
vuln: info-disclosure
tags: [bscp, tipo/vulnerabilidad, vuln/info-disclosure]
niveles: [apprentice, practitioner]
cheatsheet: "[[CS-Info-Disclosure]]"
academy: https://portswigger.net/web-security/information-disclosure
estado: pendiente
---

# Information Disclosure

## Qué es
Information Disclosure: fugas de datos por errores, backups, comentarios o ficheros de control.

## Cómo detectar
Provoca errores verbosos y revisa `robots.txt`, `.git`, backups y source maps.

## Flujo de explotación
Provocar/leer fugas → recolectar rutas/versiones/credenciales → reutilizarlas.

## Escalada a impacto
Usar lo filtrado (rutas, credenciales, tokens) para llegar a admin o leer `{{SECRET_PATH}}`.

## Gotchas de examen
Los source maps (`.map`) reconstruyen el código; cabeceras `Server`/`X-Powered-By` delatan versiones.

## Cheat sheet
[[CS-Info-Disclosure]]

## Labs
[[_Tracker-Information-Disclosure]]

## Enlaces
- https://portswigger.net/web-security/information-disclosure
