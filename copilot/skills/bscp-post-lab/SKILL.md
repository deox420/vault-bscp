---
name: bscp-post-lab
description: Actualiza el vault cuando la usuaria indica que ha RESUELTO o completado un lab de la Web Security Academy. DISPARADORES (español o inglés): "he resuelto el lab", "resolví/acabé/completé el lab", "lo resolví", "márcalo como resuelto", "regístralo", o cuando PEGA el texto de un lab de PortSwigger que incluye "LAB Solved" o "Solved" sin pedir explicación. Crea la ficha del lab como resuelto, sube el estado del tema, guarda la lección en "Qué generalizo", y actualiza el tracker y el progreso. IMPORTANTE: en la FICHA del lab SÍ se registra el payload/solución REAL que usó (es su referencia personal); la regla de "no dar soluciones" es solo para el chat de estudio, no para la ficha. Si en el MISMO mensaje pide además que le expliquen el lab, enseña primero (sin resolver) y ofrece registrarlo al final.
license: MIT
metadata:
  copilot-enabled-agents: claude, codex, opencode
---

# BSCP · Registrar lab resuelto

Cuando indico que he **resuelto** un lab, **actualiza el vault**. La **ficha del lab es mi registro personal**: **incluye el payload/solución REAL** que usé. (La regla de "no dar la solución" es SOLO para el chat de estudio, no para la ficha.)

## Cómo sé que debo actuar (disparadores)
- "he resuelto el lab", "resolví / acabé / completé el lab X", "márcalo como resuelto", "regístralo".
- Pego el **texto de un lab de PortSwigger** con **"LAB Solved" / "Solved"** y NO pido que me lo expliques.

## Pasos (no dejes ninguno a medias)
0. **Extrae del texto que pego**: título, **nivel** (apprentice/practitioner) y **tema** (mapea a su carpeta, p. ej. SQLi → `03-Labs/SQL-Injection/`). Si falta algo, pregunta.
1. **Crea la ficha** `03-Labs/<Tema>/Lab-<Tema>-NN-<slug>.md` con frontmatter válido, `estado: resuelto`, tag `estado/resuelto`. **Rellena `url` con la URL REAL del lab (portswigger.net/...); NUNCA dejes `{{LAB_URL}}`.** Secciones: `## Objetivo`, `## Fase(s)`, `## Pasos realizados`, `## Payload usado (solución real)` ← **aquí va el payload literal que funcionó**, `## Qué generalizo` (el patrón), `## Enlace academy`.
2. **Estado del tema**: en `01-Vulnerabilidades/<Tema>.md`, sube `estado:` a `en-progreso` (o `dominado` si lo indico).
3. **Qué generalizo**: añade 1-2 viñetas del patrón a la nota del tema.
4. **Tracker (SIEMPRE)**: añade la fila del lab (resuelto + fecha) en `_Tracker-<Tema>.md`. No lo olvides.
5. **Progreso**: el Dataview de `[[Progreso-Academy]]` lo cuenta solo; recuérdame ajustar el número manual si sigo el widget.

## Antes de guardar
- Muestra el resumen del cambio (diff) y confirma.
- Frontmatter y wikilinks válidos.
- La **cheat sheet** (`CS-*`) se mantiene **genérica/parametrizada**; la **ficha del lab** lleva la **solución real**.

## Checklist de cierre (OBLIGATORIO — repásalo antes de decir "hecho")
- [ ] Leí el estado actual (nota del tema + `_Tracker-*`) antes de escribir.
- [ ] Ficha creada con `url` **REAL** (no `{{LAB_URL}}`).
- [ ] **Solución real** en la ficha (payload que funcionó).
- [ ] `estado:` del tema actualizado.
- [ ] Viñeta añadida en "## Qué generalizo".
- [ ] **Fila añadida en el `_Tracker-<Tema>.md`** (no lo olvides).
- [ ] Confirmado conmigo antes de guardar; si dije "sí", lo ejecuté (no re-propuse).
Si algún punto falta, complétalo antes de terminar.
