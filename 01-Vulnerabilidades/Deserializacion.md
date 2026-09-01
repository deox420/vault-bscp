---
tipo: vulnerabilidad
vuln: deserializacion
tags: [bscp, tipo/vulnerabilidad, vuln/deserializacion]
niveles: [apprentice, practitioner]
cheatsheet: "[[CS-Deserializacion]]"
academy: https://portswigger.net/web-security/deserialization
estado: pendiente
---

# Deserializacion

## Qué es
Deserialización insegura: datos serializados manipulables que la app reconstruye en objetos.

## Cómo detectar
Identifica formatos serializados (PHP `O:...`, Java `rO0AB`/`ac ed 00 05`).

## Flujo de explotación
Identificar formato → manipular campos para escalar → gadget chain si toca RCE.

## Escalada a impacto
Elevar privilegios o RCE para leer `{{SECRET_PATH}}`.

## Gotchas de examen
Abusa de `__wakeup`/`__destruct` y considera PHAR; en Java, ysoserial `⚠️`.

## Cheat sheet
[[CS-Deserializacion]]

## Labs
[[_Tracker-Deserializacion]]

## Enlaces
- https://portswigger.net/web-security/deserialization
