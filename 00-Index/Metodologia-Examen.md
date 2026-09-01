---
tipo: moc
tags: [bscp, tipo/moc]
---

# Metodología de Examen (BSCP)

El examen tiene 2 aplicaciones; en cada una hay que llegar de un usuario sin privilegios a leer el secreto/borrar al usuario objetivo. Trabaja siempre en 3 fases.

## Fase 1 — Acceso (#fase/1-acceso)
1. Recon completo de la app (ver [[Metodologia-Discovery]]).
2. Encuentra una vía para autenticarte o robar una sesión de bajo privilegio.
3. Lanza [[Burp-Scanner]] en paralelo mientras exploras a mano.

## Fase 2 — Admin (#fase/2-admin)
1. Desde el acceso inicial, busca escalar a `{{TARGET_USER}}` (normalmente `administrator`).
2. Encadena vulnerabilidades: robo de sesión de `{{VICTIM}}`, IDOR, JWT/OAuth, etc.

## Fase 3 — Secret (#fase/3-secret)
1. Con acceso admin, ejecuta la acción final: leer `{{SECRET_PATH}}` o borrar al usuario objetivo.

## Reglas de oro
- Corre Burp Scanner sobre TODO desde el minuto uno.
- Anota cada endpoint y parámetro; parametriza con el glosario.
- Cada hallazgo reutilizable vuelve a su cheat sheet (`## Qué generalizo`).

## Enlaces
- [[MOC-BSCP]]
