---
tipo: moc
tags: [bscp, tipo/moc]
---

# 📊 Dashboard · BSCP

Página única de **progreso + arranque diario**. Sistema: [[README-Sistema]] · Preferencias: [[Preferencias]] · Índice: [[MOC-BSCP]].

## Nivel en la Academy (widget de PortSwigger — manual)
> Última actualización: 2026-09-08. Pégame el widget y lo actualizo (no se sincroniza solo).

| Nivel | Hechos | Total |
|---|---|---|
| Apprentice | 2 | 61 |
| Practitioner | 8 | 173 |
| Expert | 0 | 39 |
| **Global** | **10** | **273 (3%)** |

Nivel actual: **NEWBIE** → 59 labs para *Apprentice*.

## Labs resueltos (automático, por fecha)
```dataview
TABLE WITHOUT ID fecha AS "Fecha", file.link AS "Lab", vuln AS "Tema", nivel AS "Nivel"
FROM "03-Labs"
WHERE tipo = "lab" AND estado = "resuelto"
SORT fecha DESC
```

## Estado por tema (automático)
```dataview
TABLE WITHOUT ID link(file.link, vuln) AS "Tema", estado AS "Estado"
FROM "01-Vulnerabilidades"
WHERE tipo = "vulnerabilidad"
SORT estado ASC, file.name ASC
```

## Empezar ahora
1. [[Agente-Planificador]] → siguiente tema.
2. [[Agente-Tutor]] → estudia el patrón.
3. [[Agente-Examinador]] → pega un lab en bruto.
4. [[Agente-Redactor]] → ordena lo aprendido.
5. [[Agente-Diario]] → cierra el día.

## Atajos
- [[Triage-Deteccion]] · [[Metodologia-Examen]] · [[Burp-Scanner]] · [[Extensiones-Burp]]
