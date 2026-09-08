---
tipo: moc
vuln: nosqli
tags: [bscp, tipo/moc, vuln/nosqli]
---

# Tracker · NoSQL Injection

Registro de progreso. Relacionada: [[NoSQL-Injection]] · Cheat sheet: [[CS-NoSQLi]].
Ordenado por **fecha de realización** (`fecha`); `orden` (ruta de aprendizaje) como desempate. Edita esos campos, no renombres ficheros.

```dataview
TABLE WITHOUT ID fecha AS "Fecha", file.link AS "Lab", nivel AS "Nivel", estado AS "Estado"
FROM "03-Labs/NoSQL-Injection"
WHERE tipo = "lab"
SORT fecha ASC, orden ASC
```
