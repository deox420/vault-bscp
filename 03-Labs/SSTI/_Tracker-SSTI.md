---
tipo: moc
vuln: ssti
tags: [bscp, tipo/moc, vuln/ssti]
---

# Tracker · SSTI

Registro de progreso. Relacionada: [[SSTI]] · Cheat sheet: [[CS-SSTI]].
Ordenado por **orden de realización** (`orden`, = orden en que hiciste los labs). Edita `orden`/`fecha` si hace falta.

```dataview
TABLE WITHOUT ID fecha AS "Fecha", file.link AS "Lab", nivel AS "Nivel", estado AS "Estado"
FROM "03-Labs/SSTI"
WHERE tipo = "lab"
SORT orden ASC
```
