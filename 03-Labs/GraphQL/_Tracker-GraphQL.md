---
tipo: moc
vuln: graphql
tags: [bscp, tipo/moc, vuln/graphql]
---

# Tracker · GraphQL

Registro de progreso. Relacionada: [[GraphQL]] · Cheat sheet: [[CS-GraphQL]].
Ordenado por **fecha de realización** (`fecha`); `orden` (ruta de aprendizaje) como desempate. Edita esos campos, no renombres ficheros.

```dataview
TABLE WITHOUT ID fecha AS "Fecha", file.link AS "Lab", nivel AS "Nivel", estado AS "Estado"
FROM "03-Labs/GraphQL"
WHERE tipo = "lab"
SORT fecha ASC, orden ASC
```
