---
tipo: moc
vuln: jwt
tags: [bscp, tipo/moc, vuln/jwt]
---

# Tracker · JWT

Registro de progreso. Relacionada: [[JWT]] · Cheat sheet: [[CS-JWT]].
Ordenado por **orden de realización** (`orden`, = orden en que hiciste los labs). Edita `orden`/`fecha` si hace falta.

```dataview
TABLE WITHOUT ID fecha AS "Fecha", file.link AS "Lab", nivel AS "Nivel", estado AS "Estado"
FROM "03-Labs/JWT"
WHERE tipo = "lab"
SORT orden ASC
```
