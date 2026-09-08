---
tipo: moc
vuln: race-conditions
tags: [bscp, tipo/moc, vuln/race-conditions]
---

# Tracker · Race Conditions

Registro de progreso. Relacionada: [[Race-Conditions]] · Cheat sheet: [[CS-Race-Conditions]].
Ordenado por **fecha de realización** (`fecha`); `orden` (ruta de aprendizaje) como desempate. Edita esos campos, no renombres ficheros.

```dataview
TABLE WITHOUT ID fecha AS "Fecha", file.link AS "Lab", nivel AS "Nivel", estado AS "Estado"
FROM "03-Labs/Race-Conditions"
WHERE tipo = "lab"
SORT fecha ASC, orden ASC
```
