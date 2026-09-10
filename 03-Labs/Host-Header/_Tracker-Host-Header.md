---
tipo: moc
vuln: host-header
tags: [bscp, tipo/moc, vuln/host-header]
---

# Tracker · Host Header

Registro de progreso. Relacionada: [[Host-Header]] · Cheat sheet: [[CS-Host-Header]].
Ordenado por **orden de realización** (`orden`, = orden en que hiciste los labs). Edita `orden`/`fecha` si hace falta.

```dataview
TABLE WITHOUT ID fecha AS "Fecha", file.link AS "Lab", nivel AS "Nivel", estado AS "Estado"
FROM "03-Labs/Host-Header"
WHERE tipo = "lab"
SORT orden ASC
```
