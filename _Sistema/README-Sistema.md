---
tipo: moc
tags: [bscp, tipo/moc]
---

# ⚙️ Sistema de estudio (multi-agente)

Núcleo del vault: **preferencias + agentes** que cualquier motor de IA puede leer (Ollama en Obsidian o Claude). Cambias el motor, el sistema sigue igual.

## Tu memoria
- [[Preferencias]] — cómo quieres las cosas (se rellena una vez, todos la respetan).
- [[Dashboard]] — progreso y punto de partida diario.

## Los agentes
- 🧑‍🏫 [[Agente-Tutor]] — explica teoría y el porqué del patrón.
- 🎯 [[Agente-Examinador]] — simula el examen; le pegas labs en bruto y te entrena (sin resolverlos).
- ✍️ [[Agente-Redactor]] — crea y ordena notas con tu formato; toma notas de las sesiones.
- 🗺️ [[Agente-Planificador]] — lleva tu progresión y el repaso espaciado.
- 🌙 [[Agente-Diario]] — resumen diario y consolidación (segundo cerebro).

## Rutinas automáticas (skills)
Lo que se repite ya está automatizado (en `copilot/skills/`). Se disparan solas por frase:
- **bscp-post-lab** — al terminar un lab: actualiza estado, "Qué generalizo", checklist, tracker y progreso.
- **bscp-daily-summary** — resume el día en `_Diario/`.
- **bscp-new-lab** — crea la nota de un lab nuevo con formato correcto + tracker.

> Actívalas una vez en **Copilot → pestaña Skills** (marcarlas como habilitadas). Los disparadores están también en [[AGENTS]] por si el plugin resetea la carpeta.

## Todo unido en el vault
- **Conversaciones**: se autoguardan como notas (carpeta `copilot/`).
- **Skills** del plugin: viven en la carpeta del plugin dentro del vault.
- **Agentes**: aquí, en `_Sistema/Agentes/`.
- **Progreso**: [[Progreso-Academy]] · **Diario**: carpeta `_Diario/`.
- Todo enlazado desde [[MOC-BSCP]] y [[Dashboard]] → un solo cuerpo navegable.

## Regla de oro del sistema
Ningún agente te da la solución de un lab. Solo **pistas graduadas si las pides**, y **teoría para leer patrones**. Ver [[Preferencias]].

## Cómo se usa con el motor de IA
1. En tu plugin de IA (o en Claude), abres un chat.
2. Pegas el contenido del agente que quieras como **instrucción/system prompt**
   (o dices: "Actúa como [[Agente-Examinador]] y sigue [[Preferencias]]").
3. Trabajas. Al terminar, el [[Agente-Redactor]] ordena lo aprendido en el vault.

## Enlaces
- [[MOC-BSCP]] · [[Preferencias]] · [[Dashboard]]
