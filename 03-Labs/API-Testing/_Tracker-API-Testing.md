---
tipo: moc
vuln: api
tags: [bscp, tipo/moc, vuln/api]
---

# Tracker · API Testing

Registro de progreso. Relacionada: [[API-Testing]] · Cheat sheet: [[CS-API]].
Ordenado por **fecha de realización** (`fecha`); `orden` (ruta de aprendizaje) como desempate. Edita esos campos, no renombres ficheros.

```dataview
TABLE WITHOUT ID fecha AS "Fecha", file.link AS "Lab", nivel AS "Nivel", estado AS "Estado"
FROM "03-Labs/API-Testing"
WHERE tipo = "lab"
SORT fecha ASC, orden ASC
```
