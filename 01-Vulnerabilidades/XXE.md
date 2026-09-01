---
tipo: vulnerabilidad
vuln: xxe
tags: [bscp, tipo/vulnerabilidad, vuln/xxe]
niveles: [apprentice, practitioner]
cheatsheet: "[[CS-XXE]]"
academy: https://portswigger.net/web-security/xxe
estado: pendiente
---

# XXE

## Qué es
XML External Entity: un parser XML procesa entidades externas que definimos.

## Cómo detectar
Detecta entradas XML (body, SOAP, subida SVG/DOCX) y prueba una entidad que se resuelva.

## Flujo de explotación
Detectar XML → leer fichero con `SYSTEM file://` → si es ciego, DTD OOB en `{{EXPLOIT}}`.

## Escalada a impacto
Leer credenciales/ficheros o pivotar a SSRF interno vía XXE.

## Gotchas de examen
Si no controlas el DOCTYPE, usa XInclude; la exfiltración ciega va por `{{COLLAB}}`.

## Cheat sheet
[[CS-XXE]]

## Labs
[[_Tracker-XXE]]

## Enlaces
- https://portswigger.net/web-security/xxe
