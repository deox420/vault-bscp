---
tipo: moc
vuln: cmdi
tags: [bscp, tipo/moc, vuln/cmdi]
---

# Tracker · Command Injection

Registro de progreso. Relacionada: [[Command-Injection]] · Cheat sheet: [[CS-CMDi]].
Ordenado por **fecha de realización** (`fecha`); `orden` (ruta de aprendizaje) como desempate. Edita esos campos, no renombres ficheros.

```dataview
TABLE WITHOUT ID fecha AS "Fecha", file.link AS "Lab", nivel AS "Nivel", estado AS "Estado"
FROM "03-Labs/Command-Injection"
WHERE tipo = "lab"
SORT fecha ASC, orden ASC
```
