---
tipo: moc
vuln: info-disclosure
tags: [bscp, tipo/moc, vuln/info-disclosure]
---

# Tracker · Information Disclosure

Registro de progreso. Relacionada: [[Information-Disclosure]] · Cheat sheet: [[CS-Info-Disclosure]].
Ordenado por **fecha de realización** (`fecha`); `orden` (ruta de aprendizaje) como desempate. Edita esos campos, no renombres ficheros.

```dataview
TABLE WITHOUT ID fecha AS "Fecha", file.link AS "Lab", nivel AS "Nivel", estado AS "Estado"
FROM "03-Labs/Information-Disclosure"
WHERE tipo = "lab"
SORT fecha ASC, orden ASC
```
