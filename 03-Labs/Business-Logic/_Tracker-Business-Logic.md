---
tipo: moc
vuln: business-logic
tags: [bscp, tipo/moc, vuln/business-logic]
---

# Tracker · Business Logic

Registro de progreso. Relacionada: [[Business-Logic]] · Cheat sheet: [[CS-Business-Logic]].
Ordenado por **orden de realización** (`orden`, = orden en que hiciste los labs). Edita `orden`/`fecha` si hace falta.

```dataview
TABLE WITHOUT ID fecha AS "Fecha", file.link AS "Lab", nivel AS "Nivel", estado AS "Estado"
FROM "03-Labs/Business-Logic"
WHERE tipo = "lab"
SORT orden ASC
```
