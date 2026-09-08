---
tipo: moc
vuln: xxe
tags: [bscp, tipo/moc, vuln/xxe]
---

# Tracker · XXE

Registro de progreso. Relacionada: [[XXE]] · Cheat sheet: [[CS-XXE]].
Ordenado por **fecha de realización** (`fecha`); `orden` (ruta de aprendizaje) como desempate. Edita esos campos, no renombres ficheros.

```dataview
TABLE WITHOUT ID fecha AS "Fecha", file.link AS "Lab", nivel AS "Nivel", estado AS "Estado"
FROM "03-Labs/XXE"
WHERE tipo = "lab"
SORT fecha ASC, orden ASC
```
