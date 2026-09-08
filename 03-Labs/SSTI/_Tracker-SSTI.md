---
tipo: moc
vuln: ssti
tags: [bscp, tipo/moc, vuln/ssti]
---

# Tracker · SSTI

Registro de progreso. Relacionada: [[SSTI]] · Cheat sheet: [[CS-SSTI]].
Ordenado por **fecha de realización** (`fecha`); `orden` (ruta de aprendizaje) como desempate. Edita esos campos, no renombres ficheros.

```dataview
TABLE WITHOUT ID fecha AS "Fecha", file.link AS "Lab", nivel AS "Nivel", estado AS "Estado"
FROM "03-Labs/SSTI"
WHERE tipo = "lab"
SORT fecha ASC, orden ASC
```
