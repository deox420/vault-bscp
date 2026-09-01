---
name: bscp-new-lab
description: Crear una nota de lab nueva en el vault con el formato correcto y añadirla a su tracker. Úsala cuando la usuaria diga "nuevo lab", "voy a empezar un lab de X", "crea la nota de este lab". Genera el frontmatter y los tags válidos y NO incluye solución, solo el andamiaje y placeholders.
license: MIT
metadata:
  copilot-enabled-agents: claude, codex, opencode
---

# BSCP · Nueva nota de lab

Andamiaje reproducible para un lab. **Sin solución**: solo estructura y placeholders.

## Datos que necesitas (pregunta si faltan)
- Tema (p. ej. SQLi → carpeta `03-Labs/SQL-Injection/`).
- Nombre/slug del lab, `nivel` (`apprentice`|`practitioner`), `fase` (`1-acceso`|`2-admin`|`3-secret`), `url` (opcional).

## Pasos
1. Crea `03-Labs/<Tema>/Lab-<Tema>-NN-<slug>.md` a partir de `[[Plantilla-Lab]]` con este frontmatter:
   ```yaml
   ---
   tipo: lab
   vuln: <slug>
   nivel: <nivel>
   tags: [bscp, tipo/lab, vuln/<slug>, nivel/<nivel>, estado/pendiente]
   fase: [<fase>]
   url: <url>
   estado: pendiente
   ---
   ```
2. Cuerpo con secciones: `## Objetivo`, `## Fase(s)`, `## Pasos realizados`, `## Payload usado` (parametrizado), `## Qué generalizo`, `## Enlace academy`.
3. Enlaza a su cheat sheet `[[CS-<Abrev>]]`.
4. Añade una fila en `03-Labs/<Tema>/_Tracker-<Tema>.md`.

## Antes de guardar
- Verifica que los wikilinks resuelven y los tags tienen prefijo válido.
- Muestra el resultado y confirma.
