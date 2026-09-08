---
tipo: moc
vuln: smuggling
tags: [bscp, tipo/moc, vuln/smuggling]
---

# Tracker · Request Smuggling

Registro de progreso. Relacionada: [[Request-Smuggling]] · Cheat sheet: [[CS-Smuggling]].
Ordenado por **fecha de realización** (`fecha`); `orden` (ruta de aprendizaje) como desempate. Edita esos campos, no renombres ficheros.

```dataview
TABLE WITHOUT ID fecha AS "Fecha", file.link AS "Lab", nivel AS "Nivel", estado AS "Estado"
FROM "03-Labs/Request-Smuggling"
WHERE tipo = "lab"
SORT fecha ASC, orden ASC
```
