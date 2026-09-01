---
tipo: moc
tags: [bscp, tipo/moc]
---

# 📊 Dashboard de estudio · BSCP

Portada de progreso. Punto de partida diario. Sistema: [[README-Sistema]] · Preferencias: [[Preferencias]].

## Progreso por tema (Dataview)
```dataview
TABLE WITHOUT ID link(file.link, vuln) AS "Tema", estado, cheatsheet AS "Cheat sheet"
FROM "01-Vulnerabilidades"
WHERE tipo = "vulnerabilidad"
SORT estado ASC, file.name ASC
```

## Resumen de estados
```dataview
TABLE length(rows) AS "Nº temas"
FROM "01-Vulnerabilidades"
WHERE tipo = "vulnerabilidad"
GROUP BY estado
```

## Labs por estado
```dataview
TABLE WITHOUT ID file.link AS "Lab", vuln, nivel, fase
FROM "03-Labs"
WHERE tipo = "lab"
SORT estado ASC, vuln ASC
```

## Tabla de respaldo (si no tienes Dataview)
> Cambia el estado a mano en el frontmatter de cada nota de `01-Vulnerabilidades/`.
> Estados: `pendiente` · `en-progreso` · `dominado`.

- Punto de entrada de temas: [[MOC-BSCP]]
- Metodología: [[Metodologia-Examen]] · [[Metodologia-Discovery]]

## Progreso Academy
- Panel espejo del widget de PortSwigger: [[Progreso-Academy]].

## Empezar ahora
1. Abre el [[Agente-Planificador]] y pídele el siguiente tema.
2. Estudia con el [[Agente-Tutor]].
3. Practica pegando un lab en bruto al [[Agente-Examinador]].
4. Ordena lo aprendido con el [[Agente-Redactor]].
5. Al final del día, resume con el [[Agente-Diario]].
