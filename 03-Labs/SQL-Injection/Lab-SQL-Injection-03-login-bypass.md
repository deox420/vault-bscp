---
tipo: lab
vuln: sqli
nivel: apprentice
tags: [bscp, tipo/lab, vuln/sqli, nivel/apprentice, estado/resuelto]
fase: [1-acceso]
url: https://portswigger.net/web-security/sql-injection/lab-login-bypass
estado: resuelto
---

# SQL Injection · Lab 03 — Login bypass (apprentice) ✅

## Objetivo
Iniciar sesión como `{{TARGET_USER}}` (administrator) sin la contraseña, mediante SQLi en la función de login.

## Fase(s)
- 1-acceso

## Pasos realizados
- Capturé la petición POST de login con Burp (Proxy → Repeater).
- Deduje la consulta: `SELECT * FROM users WHERE username='…' AND password='…'`.
- Inyecté para **anular la comprobación de contraseña**: cerrar la cadena, condición siempre verdadera y comentar el resto.
- La aplicación autenticó como administrador.

## Payload usado (solución real)
En el campo **usuario** del login:

```
administrator'--
```

La contraseña se deja en blanco/cualquiera: `--` comenta la comprobación `AND password='…'`.

## Qué generalizo
- **Bypass de login:** cerrar la cadena del parámetro, añadir una condición booleana siempre verdadera (`OR 1=1`) y **comentar** el resto (`--`) para saltar la verificación de contraseña.
- **Señal de detección:** usuario/contraseña se concatenan directamente en un `WHERE`; una comilla simple provoca error o comportamiento raro.

## Enlace academy
- https://portswigger.net/web-security/sql-injection/lab-login-bypass
