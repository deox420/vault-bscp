---
tipo: vulnerabilidad
vuln: path-traversal
tags: [bscp, tipo/vulnerabilidad, vuln/path-traversal]
niveles: [apprentice, practitioner]
cheatsheet: "[[CS-Path-Traversal]]"
academy: https://portswigger.net/web-security/file-path-traversal
estado: pendiente
---

# Path Traversal

## Qué es
Path Traversal: manipular un nombre de fichero para salir del directorio previsto.

## Cómo detectar
Sube directorios con `../`; si hay filtro, codifica o anida las secuencias.

## Flujo de explotación
Localizar `{{PARAM}}` de fichero → traversal directo/codificado/anidado o ruta absoluta.

## Escalada a impacto
Leer ficheros sensibles o `{{SECRET_PATH}}` para obtener credenciales.

## Gotchas de examen
Prueba doble codificación, anidado `....//` y (legacy) null byte.

## Cheat sheet
[[CS-Path-Traversal]]

## Labs
[[_Tracker-Path-Traversal]]

## Enlaces
- https://portswigger.net/web-security/file-path-traversal
