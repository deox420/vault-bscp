---
tipo: vulnerabilidad
vuln: race-conditions
tags: [bscp, tipo/vulnerabilidad, vuln/race-conditions]
niveles: [practitioner]
cheatsheet: "[[CS-Race-Conditions]]"
academy: https://portswigger.net/web-security/race-conditions
estado: pendiente
---

# Race Conditions

## Qué es
Race Conditions: explotar la ventana entre comprobación y acción con peticiones paralelas.

## Cómo detectar
Busca comprobaciones previas a una acción (saldo, límite, cupón) con ventana temporal.

## Flujo de explotación
Identificar la ventana → enviar en paralelo (single-packet attack) → confirmar duplicado.

## Escalada a impacto
Duplicar saldo/cupón o saltar límites para lograr una ventaja hacia el objetivo.

## Gotchas de examen
Usa 'Send group in parallel' (single-packet) o Turbo Intruder para volumen.

## Cheat sheet
[[CS-Race-Conditions]]

## Labs
[[_Tracker-Race-Conditions]]

## Enlaces
- https://portswigger.net/web-security/race-conditions
