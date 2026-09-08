---
tipo: moc
vuln: ssrf
tags: [bscp, tipo/moc, vuln/ssrf]
---

# Tracker · SSRF

Registro de progreso. Relacionada: [[SSRF]] · Cheat sheet: [[CS-SSRF]].
Ordenado por **fecha de realización** (`fecha`); `orden` (ruta de aprendizaje) como desempate. Edita esos campos, no renombres ficheros.

```dataview
TABLE WITHOUT ID fecha AS "Fecha", file.link AS "Lab", nivel AS "Nivel", estado AS "Estado"
FROM "03-Labs/SSRF"
WHERE tipo = "lab"
SORT fecha ASC, orden ASC
```
