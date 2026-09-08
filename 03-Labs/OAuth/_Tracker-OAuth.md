---
tipo: moc
vuln: oauth
tags: [bscp, tipo/moc, vuln/oauth]
---

# Tracker · OAuth

Registro de progreso. Relacionada: [[OAuth]] · Cheat sheet: [[CS-OAuth]].
Ordenado por **fecha de realización** (`fecha`); `orden` (ruta de aprendizaje) como desempate. Edita esos campos, no renombres ficheros.

```dataview
TABLE WITHOUT ID fecha AS "Fecha", file.link AS "Lab", nivel AS "Nivel", estado AS "Estado"
FROM "03-Labs/OAuth"
WHERE tipo = "lab"
SORT fecha ASC, orden ASC
```
