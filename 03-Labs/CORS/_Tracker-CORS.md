---
tipo: moc
vuln: cors
tags: [bscp, tipo/moc, vuln/cors]
---

# Tracker · CORS

Registro de progreso. Relacionada: [[CORS]] · Cheat sheet: [[CS-CORS]].
Ordenado por **fecha de realización** (`fecha`); `orden` (ruta de aprendizaje) como desempate. Edita esos campos, no renombres ficheros.

```dataview
TABLE WITHOUT ID fecha AS "Fecha", file.link AS "Lab", nivel AS "Nivel", estado AS "Estado"
FROM "03-Labs/CORS"
WHERE tipo = "lab"
SORT fecha ASC, orden ASC
```
