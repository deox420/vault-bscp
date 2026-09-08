---
tipo: moc
vuln: jwt
tags: [bscp, tipo/moc, vuln/jwt]
---

# Tracker · JWT

Registro de progreso. Relacionada: [[JWT]] · Cheat sheet: [[CS-JWT]].
Ordenado por **fecha de realización** (`fecha`); `orden` (ruta de aprendizaje) como desempate. Edita esos campos, no renombres ficheros.

```dataview
TABLE WITHOUT ID fecha AS "Fecha", file.link AS "Lab", nivel AS "Nivel", estado AS "Estado"
FROM "03-Labs/JWT"
WHERE tipo = "lab"
SORT fecha ASC, orden ASC
```
