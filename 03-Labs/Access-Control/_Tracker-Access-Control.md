---
tipo: moc
vuln: access-control
tags: [bscp, tipo/moc, vuln/access-control]
---

# Tracker · Access Control

Registro de progreso. Relacionada: [[Access-Control]] · Cheat sheet: [[CS-Access-Control]].
Ordenado por **fecha de realización** (`fecha`); `orden` (ruta de aprendizaje) como desempate. Edita esos campos, no renombres ficheros.

```dataview
TABLE WITHOUT ID fecha AS "Fecha", file.link AS "Lab", nivel AS "Nivel", estado AS "Estado"
FROM "03-Labs/Access-Control"
WHERE tipo = "lab"
SORT fecha ASC, orden ASC
```
