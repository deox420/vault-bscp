---
tipo: moc
vuln: auth
tags: [bscp, tipo/moc, vuln/auth]
---

# Tracker · Authentication

Registro de progreso. Relacionada: [[Authentication]] · Cheat sheet: [[CS-Auth]].
Ordenado por **fecha de realización** (`fecha`); `orden` (ruta de aprendizaje) como desempate. Edita esos campos, no renombres ficheros.

```dataview
TABLE WITHOUT ID fecha AS "Fecha", file.link AS "Lab", nivel AS "Nivel", estado AS "Estado"
FROM "03-Labs/Authentication"
WHERE tipo = "lab"
SORT fecha ASC, orden ASC
```
