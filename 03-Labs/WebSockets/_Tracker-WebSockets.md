---
tipo: moc
vuln: websockets
tags: [bscp, tipo/moc, vuln/websockets]
---

# Tracker · WebSockets

Registro de progreso. Relacionada: [[WebSockets]] · Cheat sheet: [[CS-WebSockets]].
Ordenado por **fecha de realización** (`fecha`); `orden` (ruta de aprendizaje) como desempate. Edita esos campos, no renombres ficheros.

```dataview
TABLE WITHOUT ID fecha AS "Fecha", file.link AS "Lab", nivel AS "Nivel", estado AS "Estado"
FROM "03-Labs/WebSockets"
WHERE tipo = "lab"
SORT fecha ASC, orden ASC
```
