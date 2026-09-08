---
tipo: moc
vuln: csrf
tags: [bscp, tipo/moc, vuln/csrf]
---

# Tracker · CSRF

Registro de progreso. Relacionada: [[CSRF]] · Cheat sheet: [[CS-CSRF]].
Ordenado por **fecha de realización** (`fecha`); `orden` (ruta de aprendizaje) como desempate. Edita esos campos, no renombres ficheros.

```dataview
TABLE WITHOUT ID fecha AS "Fecha", file.link AS "Lab", nivel AS "Nivel", estado AS "Estado"
FROM "03-Labs/CSRF"
WHERE tipo = "lab"
SORT fecha ASC, orden ASC
```
