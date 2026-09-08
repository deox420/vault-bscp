---
tipo: moc
vuln: path-traversal
tags: [bscp, tipo/moc, vuln/path-traversal]
---

# Tracker · Path Traversal

Registro de progreso. Relacionada: [[Path-Traversal]] · Cheat sheet: [[CS-Path-Traversal]].
Ordenado por **fecha de realización** (`fecha`); `orden` (ruta de aprendizaje) como desempate. Edita esos campos, no renombres ficheros.

```dataview
TABLE WITHOUT ID fecha AS "Fecha", file.link AS "Lab", nivel AS "Nivel", estado AS "Estado"
FROM "03-Labs/Path-Traversal"
WHERE tipo = "lab"
SORT fecha ASC, orden ASC
```
