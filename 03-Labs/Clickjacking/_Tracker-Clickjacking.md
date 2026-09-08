---
tipo: moc
vuln: clickjacking
tags: [bscp, tipo/moc, vuln/clickjacking]
---

# Tracker · Clickjacking

Registro de progreso. Relacionada: [[Clickjacking]] · Cheat sheet: [[CS-Clickjacking]].
Ordenado por **fecha de realización** (`fecha`); `orden` (ruta de aprendizaje) como desempate. Edita esos campos, no renombres ficheros.

```dataview
TABLE WITHOUT ID fecha AS "Fecha", file.link AS "Lab", nivel AS "Nivel", estado AS "Estado"
FROM "03-Labs/Clickjacking"
WHERE tipo = "lab"
SORT fecha ASC, orden ASC
```
