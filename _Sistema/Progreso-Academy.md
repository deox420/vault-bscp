---
tipo: moc
tags: [bscp, tipo/moc]
---

# 🏆 Progreso · Web Security Academy

Espejo **propio** del widget "Track your progress" de PortSwigger, dentro del vault.
No se sincroniza solo con tu cuenta (haría falta iniciar sesión ahí); lo llevamos aquí a mano / con el [[Agente-Planificador]] y el [[Agente-Diario]].

## Tu nivel
- Nivel actual: **NEWBIE** → resuelve **59 labs más** para llegar a *Apprentice*.
- Actualízalo cuando cambie tu widget de PortSwigger (no se sincroniza solo).

## Marcadores por nivel (última actualización: 2026-09-08)
> Totales oficiales de la Academy. Copia aquí los "hechos" de tu widget.

| Nivel | Hechos | Total | % |
|---|---|---|---|
| Apprentice | 2 | 61 | ~3% |
| Practitioner | 8 | 173 | ~5% |
| Expert | 0 | 39 | 0% |
| **Global** | **10** | **273** | **~3%** |

## Progreso real en el vault (Dataview, automático)
Cuenta tus notas de lab por estado. Crece según el [[Agente-Redactor]] añade labs.
```dataview
TABLE WITHOUT ID estado AS "Estado", length(rows) AS "Nº labs"
FROM "03-Labs"
WHERE tipo = "lab"
GROUP BY estado
```

## Labs resueltos por tema
```dataview
TABLE WITHOUT ID file.link AS "Lab", vuln AS "Tema", nivel
FROM "03-Labs"
WHERE tipo = "lab" AND estado = "resuelto"
SORT vuln ASC
```

## Estado por tema (frontmatter de las notas de vulnerabilidad)
```dataview
TABLE WITHOUT ID link(file.link, vuln) AS "Tema", estado
FROM "01-Vulnerabilidades"
WHERE tipo = "vulnerabilidad"
SORT estado ASC
```

## Cómo actualizarlo
- Al resolver un lab real, el [[Agente-Redactor]] crea/actualiza su nota (`estado: resuelto`) y sube la cuenta de arriba.
- Revisa esta nota en tu repaso semanal con el [[Agente-Planificador]].

## Enlaces
- [[Dashboard]] · [[MOC-BSCP]] · [[README-Sistema]]
