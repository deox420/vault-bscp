---
tipo: moc
vuln: cache-poisoning
tags: [bscp, tipo/moc, vuln/cache-poisoning]
---

# Tracker · Cache Poisoning

Registro de progreso. Relacionada: [[Cache-Poisoning]] · Cheat sheet: [[CS-Cache-Poisoning]].
Ordenado por **fecha de realización** (`fecha`); `orden` (ruta de aprendizaje) como desempate. Edita esos campos, no renombres ficheros.

```dataview
TABLE WITHOUT ID fecha AS "Fecha", file.link AS "Lab", nivel AS "Nivel", estado AS "Estado"
FROM "03-Labs/Cache-Poisoning"
WHERE tipo = "lab"
SORT fecha ASC, orden ASC
```
