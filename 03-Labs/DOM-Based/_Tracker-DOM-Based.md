---
tipo: moc
vuln: dom
tags: [bscp, tipo/moc, vuln/dom]
---

# Tracker · DOM-based

Registro de progreso. Relacionada: [[DOM-Based]] · Cheat sheet: [[CS-DOM]].
Ordenado por **fecha de realización** (`fecha`); `orden` (ruta de aprendizaje) como desempate. Edita esos campos, no renombres ficheros.

```dataview
TABLE WITHOUT ID fecha AS "Fecha", file.link AS "Lab", nivel AS "Nivel", estado AS "Estado"
FROM "03-Labs/DOM-Based"
WHERE tipo = "lab"
SORT fecha ASC, orden ASC
```
