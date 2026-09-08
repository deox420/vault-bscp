---
name: bscp-post-lab
description: Actualiza el vault cuando la usuaria indica que ha RESUELTO o completado un lab de la Web Security Academy. DISPARADORES (español o inglés): "he resuelto el lab", "resolví/acabé/completé el lab", "lo resolví", "márcalo como resuelto", "regístralo", "sí"/"confirmar" tras proponer el registro, o cuando PEGA el texto de un lab de PortSwigger que incluye "LAB Solved"/"Solved"/"Congratulations, you solved" sin pedir explicación. Crea la ficha del lab como resuelto, sube el estado del tema, guarda la lección en "Qué generalizo", y actualiza el tracker. En la FICHA se registra el payload/solución REAL (referencia personal); la regla de "no dar soluciones" es solo para el chat de estudio. Registra con UNA sola confirmación y ejecuta todo de golpe, sin volver a preguntar.
license: MIT
metadata:
  copilot-enabled-agents: claude, codex, opencode
---

# BSCP · Registrar lab resuelto

Cuando indico que he **resuelto** un lab, **actualiza el vault** de una vez. La ficha lleva la **solución real**.

## Autonomía (evita el ida y vuelta)
- Registra con **UNA sola confirmación**. Si pego el lab con "Solved"/"Congratulations", o digo "sí"/"regístralo", **ejecuta directamente**.
- **Tras el "sí", NO vuelvas a preguntar** "¿quieres que registre?". Hazlo y reporta.

## Reglas de nombres y numeración (CRÍTICO — aquí fallaba)
- **Guiones SOLO ASCII `-`** (U+002D). **Prohibido** `‑` (no-break), `–`, `—` en nombres de fichero y en wikilinks. Los links rotos vienen de aquí.
- **Número `NN`:** LISTA primero `03-Labs/<Tema>/` y usa el **siguiente número libre**. **Nunca** reutilices un NN ni lo adivines (nada de dos labs `05`).
- El **wikilink debe coincidir EXACTAMENTE** con el nombre del fichero (mismos guiones, mismo slug).
- **No** te auto-enlaces (no metas un "Enlace al lab" que apunte a la propia ficha).

## Pasos (no dejes ninguno a medias)
0. **Extrae del texto**: título, `nivel` (apprentice/practitioner) y tema → carpeta `03-Labs/<Tema>/`.
1. **Elige NN** = siguiente libre de la carpeta (ver reglas de arriba).
2. **Crea la ficha** `03-Labs/<Tema>/Lab-<Tema>-NN-<slug>.md`: frontmatter válido, `estado: resuelto`, tag `estado/resuelto`, **`url` = URL REAL** (nunca `{{LAB_URL}}`). Secciones: `## Objetivo`, `## Fase(s)`, `## Pasos realizados`, `## Payload usado (solución real)` (el payload literal que funcionó), `## Qué generalizo` (el patrón), `## Enlace academy`.
3. **Estado del tema**: en `01-Vulnerabilidades/<Tema>.md`, sube `estado:` a `en-progreso` (o `dominado` si lo indico).
4. **Qué generalizo**: añade 1 viñeta del patrón a la nota del tema, enlazando `[[Lab-<Tema>-NN-<slug>]]` (guiones ASCII).
5. **Tracker (SIEMPRE)**: añade la fila en `_Tracker-<Tema>.md`.

## Checklist de cierre (OBLIGATORIO antes de decir "hecho")
- [ ] `NN` es el **siguiente libre** (sin duplicados).
- [ ] Nombres y wikilinks con **guion ASCII `-`** (ningún `‑`/`–`/`—`).
- [ ] Cada wikilink apunta a un **fichero existente** (mismo nombre exacto).
- [ ] `url` **real** (no `{{LAB_URL}}`) y **solución real** en la ficha.
- [ ] `estado:` del tema · viñeta en "Qué generalizo" · **fila en el tracker**.
- [ ] Confirmé una vez; tras "sí" lo ejecuté (no re-pregunté).

> La **cheat sheet** (`CS-*`) se mantiene genérica; la **ficha** lleva la solución real.
