---
name: bscp-post-lab
description: Ejecutar SIEMPRE justo después de que la usuaria resuelve o termina un lab de la Web Security Academy. Actualiza el vault de forma consistente — pone el estado del tema, guarda la lección generalizada en "## Qué generalizo", marca el checklist de la cheat sheet y actualiza el tracker y el progreso. NUNCA escribe la solución del lab, solo patrones parametrizados con placeholders. Úsala cuando diga cosas como "terminé el lab", "resolví X", "acabé este lab".
license: MIT
metadata:
  copilot-enabled-agents: claude, codex, opencode
---

# BSCP · Rutina post-lab

Automatiza el cierre de un lab. **No resuelvas nada ni copies el walkthrough**: captura el aprendizaje. Usa placeholders (`{{BASE}}`, `{{PARAM}}`, `{{COLLAB}}`…), nunca hosts reales (además evita que Windows Defender borre notas).

## Pasos (hazlos en orden)
1. **Identifica el tema** (p. ej. SQLi → nota `01-Vulnerabilidades/SQL-Injection.md`). Si no está claro, pregunta cuál.
2. **Estado**: actualiza el campo `estado:` del frontmatter de esa nota según lo que diga la usuaria: `pendiente → en-progreso → dominado`.
3. **Lección**: en la sección `## Qué generalizo` de esa nota, añade 3-5 viñetas con el **patrón** aprendido (señales de detección, gotcha, cómo escalar en genérico). Crea la sección si no existe.
4. **Cheat sheet**: si aporta algo reproducible, marca la casilla correspondiente del `## Checklist` en `02-Cheatsheets/CS-<Abrev>.md` o añade una nota breve parametrizada.
5. **Tracker**: actualiza la fila del lab en `03-Labs/<Tema>/_Tracker-<Tema>.md` (columna Estado y Notas).
6. **Progreso**: si fue un lab real resuelto, sube la cuenta en `_Sistema/Progreso-Academy.md` (tabla de niveles).

## Antes de guardar
- Muestra un **resumen del cambio (diff)** y pide confirmación.
- **Preserva** el resto del frontmatter y no rompas wikilinks.
- Al terminar, sugiere pasar al Planificador para recalcular el siguiente tema.
