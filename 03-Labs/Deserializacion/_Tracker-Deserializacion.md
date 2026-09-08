---
tipo: moc
vuln: deserializacion
tags: [bscp, tipo/moc, vuln/deserializacion]
---

# Tracker · Deserializacion

Registro de progreso. Relacionada: [[Deserializacion]] · Cheat sheet: [[CS-Deserializacion]].
Ordenado por **fecha de realización** (`fecha`); `orden` (ruta de aprendizaje) como desempate. Edita esos campos, no renombres ficheros.

```dataview
TABLE WITHOUT ID fecha AS "Fecha", file.link AS "Lab", nivel AS "Nivel", estado AS "Estado"
FROM "03-Labs/Deserializacion"
WHERE tipo = "lab"
SORT fecha ASC, orden ASC
```
