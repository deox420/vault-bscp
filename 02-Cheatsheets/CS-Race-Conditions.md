---
tipo: cheatsheet
vuln: race-conditions
tags: [bscp, tipo/cheatsheet, vuln/race-conditions]
relacionada: "[[Race-Conditions]]"
---

# CS · Race Conditions

## Flujo repetible
1. Localiza una comprobación con ventana temporal (límite, saldo, cupón).
2. Envía peticiones en paralelo (single-packet attack).

## Detección
```
Identifica en {{BASE}} un endpoint con comprobación previa a una acción (saldo, límite, cupón).
```

## Plantillas de payload
```
Burp Repeater -> "Send group in parallel" (single-packet attack)
Turbo Intruder para volumen
Casos: canjear cupón/tarjeta varias veces, saltar límites, 2FA
```

## Escalada al objetivo
Duplicar el efecto (saldo/cupón) o saltar límites → ventaja que lleva al objetivo.

## Checklist
- [ ] Identifiqué la ventana de carrera
- [ ] Envié en paralelo
- [ ] Confirmé el efecto duplicado

## Referencias
- https://portswigger.net/web-security/race-conditions
