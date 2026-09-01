---
tipo: vulnerabilidad
vuln: cmdi
tags: [bscp, tipo/vulnerabilidad, vuln/cmdi]
niveles: [apprentice, practitioner]
cheatsheet: "[[CS-CMDi]]"
academy: https://portswigger.net/web-security/os-command-injection
estado: pendiente
---

# Command Injection

## Qué es
OS Command Injection: la entrada se pasa a un comando del sistema.

## Cómo detectar
Inyecta separadores (`;`, `&`, `|`, `` ` ``, `$()`) seguidos de un comando.

## Flujo de explotación
Detectar `{{PARAM}}` que alimenta un comando → confirmar por retardo/OAST → recuperar salida.

## Escalada a impacto
RCE para leer `{{SECRET_PATH}}` o exfiltrar a `{{COLLAB}}`.

## Gotchas de examen
Si es ciego, usa `ping`/`nslookup`/`curl` o redirige la salida a un fichero servido por la web.

## Cheat sheet
[[CS-CMDi]]

## Labs
[[_Tracker-Command-Injection]]

## Enlaces
- https://portswigger.net/web-security/os-command-injection
