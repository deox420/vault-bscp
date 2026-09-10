---
tipo: moc
vuln: file-upload
tags: [bscp, tipo/moc, vuln/file-upload]
---

# Tracker · File Upload

Registro de progreso. Relacionada: [[File-Upload]] · Cheat sheet: [[CS-File-Upload]].
Ordenado por **orden de realización** (`orden`, = orden en que hiciste los labs). Edita `orden`/`fecha` si hace falta.

```dataview
TABLE WITHOUT ID fecha AS "Fecha", file.link AS "Lab", nivel AS "Nivel", estado AS "Estado"
FROM "03-Labs/File-Upload"
WHERE tipo = "lab"
SORT orden ASC
```
