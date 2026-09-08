---
tipo: moc
vuln: prototype-pollution
tags: [bscp, tipo/moc, vuln/prototype-pollution]
---

# Tracker · Prototype Pollution

Registro de progreso. Relacionada: [[Prototype-Pollution]] · Cheat sheet: [[CS-Prototype-Pollution]].
Ordenado por **fecha de realización** (`fecha`); `orden` (ruta de aprendizaje) como desempate. Edita esos campos, no renombres ficheros.

```dataview
TABLE WITHOUT ID fecha AS "Fecha", file.link AS "Lab", nivel AS "Nivel", estado AS "Estado"
FROM "03-Labs/Prototype-Pollution"
WHERE tipo = "lab"
SORT fecha ASC, orden ASC
```
