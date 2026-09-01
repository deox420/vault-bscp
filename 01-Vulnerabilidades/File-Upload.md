---
tipo: vulnerabilidad
vuln: file-upload
tags: [bscp, tipo/vulnerabilidad, vuln/file-upload]
niveles: [apprentice, practitioner]
cheatsheet: "[[CS-File-Upload]]"
academy: https://portswigger.net/web-security/file-upload
estado: pendiente
---

# File Upload

## Qué es
File Upload inseguro: subir un fichero ejecutable y lograr que el servidor lo interprete.

## Cómo detectar
Sube un fichero y localiza su ruta; comprueba qué filtro aplica.

## Flujo de explotación
Subir código → localizar la ruta → evadir el filtro → ejecutar.

## Escalada a impacto
Ejecutar el shell para leer `{{SECRET_PATH}}`.

## Gotchas de examen
Evasiones: doble extensión, `.phtml`, Content-Type spoof, magic bytes, traversal, `.htaccess`.

## Cheat sheet
[[CS-File-Upload]]

## Labs
[[_Tracker-File-Upload]]

## Enlaces
- https://portswigger.net/web-security/file-upload
