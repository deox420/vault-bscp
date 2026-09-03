---
name: bscp-post-lab
description: Actualiza el vault cuando la usuaria indica que ha RESUELTO o completado un lab de la Web Security Academy. DISPARADORES (en español o inglés): "he resuelto el lab", "resolví/acabé/completé el lab", "lo resolví", "márcalo como resuelto", "regístralo", o cuando PEGA el texto de un lab de PortSwigger que incluye "LAB Solved" o "Solved" sin pedir explicación. Crea la nota del lab como resuelto, sube el estado del tema, guarda la lección en "Qué generalizo", y actualiza el tracker y el progreso. NUNCA guarda la solución del lab, solo el patrón parametrizado con placeholders. Si en el MISMO mensaje pide además que le expliquen el lab, enseña primero y ofrece registrarlo al final.
license: MIT
metadata:
  copilot-enabled-agents: claude, codex, opencode
---

# BSCP · Registrar lab resuelto

Cuando indico que he **resuelto/completado** un lab, **actualiza el vault**. No te quedes solo en explicar. **No guardes la solución**, solo el **patrón** parametrizado (placeholders). Si el mismo mensaje pide además explicación, enseña primero y **ofrece registrarlo al final**.

## Cómo sé que debo actuar (disparadores)
- "he resuelto el lab", "resolví / acabé / completé el lab X", "lo resolví", "márcalo como resuelto", "regístralo en el vault".
- Pego el **texto de un lab de PortSwigger** que incluye **"LAB Solved" / "Solved"** y NO pido que me lo expliques.

## Pasos
0. **Extrae del texto que pego**: título del lab, **nivel** (apprentice/practitioner) y **tema** (mapea a su carpeta, p. ej. SQLi → `03-Labs/SQL-Injection/`). Si falta algo, pregúntame.
1. **Crea la nota del lab** `03-Labs/<Tema>/Lab-<Tema>-NN-<slug>.md` (si no existe) con frontmatter válido y `estado: resuelto`, tag `estado/resuelto`. Cuerpo: `## Objetivo`, `## Fase(s)`, `## Qué generalizo` (el patrón, no la solución), `## Enlace academy`. El payload va como plantilla parametrizada enlazando `[[CS-<Abrev>]]`, **nunca** con valores del lab.
2. **Estado del tema**: en `01-Vulnerabilidades/<Tema>.md`, sube `estado:` a `en-progreso` (o `dominado` si lo indico).
3. **Qué generalizo**: añade 1-2 viñetas del patrón aprendido a la nota del tema.
4. **Tracker**: añade la fila del lab (resuelto + fecha) en `_Tracker-<Tema>.md`.
5. **Progreso**: el Dataview de `[[Progreso-Academy]]` lo cuenta solo; recuérdame ajustar el número manual si sigo el widget de PortSwigger.

## Antes de guardar
- Muestra el resumen del cambio (diff) y confirma.
- Frontmatter y wikilinks válidos; **placeholders siempre** (también evita que Defender borre notas).
- No hace falta que te dé el payload exacto: guardas el **patrón**, no la solución.
