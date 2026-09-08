---
tipo: moc
vuln: xss
tags: [bscp, tipo/moc, vuln/xss]
---

# Tracker · Cross-Site Scripting

Registro de progreso. Relacionada: [[Cross-Site-Scripting]] · Cheat sheet: [[CS-XSS]].
Ordenado por **fecha de realización** (`fecha`); `orden` (ruta de aprendizaje) como desempate. Edita esos campos, no renombres ficheros.

```dataview
TABLE WITHOUT ID fecha AS "Fecha", file.link AS "Lab", nivel AS "Nivel", estado AS "Estado"
FROM "03-Labs/Cross-Site-Scripting"
WHERE tipo = "lab"
SORT fecha ASC, orden ASC
```
