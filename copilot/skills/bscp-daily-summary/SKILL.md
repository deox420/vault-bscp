---
name: bscp-daily-summary
description: Crear o actualizar el resumen diario de estudio del BSCP en la carpeta _Diario. Úsala cuando la usuaria diga "resume el día", "cierra el día", "diario de hoy" o al terminar una sesión de estudio. Destila lo aprendido (patrones, no walkthroughs), enlaza temas y actualiza el plan de mañana. Nunca copia soluciones de labs.
license: MIT
metadata:
  copilot-enabled-agents: claude, codex, opencode
---

# BSCP · Resumen diario

Convierte la sesión en una nota diaria enlazada (base del segundo cerebro). **Resumen honesto**, sin volcar todo el chat ni soluciones.

## Pasos
1. Reúne lo trabajado en la sesión / notas recientes.
2. Crea o actualiza **`_Diario/AAAA-MM-DD.md`** (fecha de hoy) con estas secciones:
   - `## Qué estudié` — temas y labs, con wikilinks.
   - `## Qué aprendí` — 3-5 viñetas de patrones/señales reutilizables.
   - `## Dudas abiertas` — lo que quedó a medias.
   - `## Progreso` — qué `estado` cambió; enlaza `[[Progreso-Academy]]`.
   - `## Plan de mañana` — 1-3 pasos (coordina con el Planificador).
3. Enlaza el día anterior si existe, para encadenar el diario.

## Antes de guardar
- Frontmatter mínimo válido: `tipo: recurso`, `tags: [bscp, tipo/recurso]`.
- Muestra la nota y pide confirmación.
- Si surge teoría reutilizable, sugiere ejecutar `bscp-post-lab` para llevarla al tema.
