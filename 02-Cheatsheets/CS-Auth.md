---
tipo: cheatsheet
vuln: auth
tags: [bscp, tipo/cheatsheet, vuln/auth]
relacionada: "[[Authentication]]"
---

# CS · Authentication

## Flujo repetible
1. Enumera usuarios (mensajes/timing).
2. Fuerza bruta con Intruder.
3. Ataca 2FA, reset y persistencia de sesión.

## Detección
```
Enumeración: diferencias de respuesta o de tiempo al probar {{PARAM}}=usuario
```

## Plantillas de payload
```
Enumeración: diferencias de respuesta o de tiempo
Fuerza bruta: Burp Intruder (cluster bomb / pitchfork)
2FA: saltar al endpoint post-2FA · fuerza bruta del código · manipular respuesta success:true
Reset: token predecible/reutilizable · fuga de token · poisoning con Host header del enlace
Cookie remember-me predecible · sesión válida tras cambio de contraseña
```

## Escalada al objetivo
Comprometer la cuenta de {{TARGET_USER}} → acceso admin → objetivo del examen.

## Checklist
- [ ] Enumeré usuarios
- [ ] Probé fuerza bruta controlada
- [ ] Probé bypass de 2FA y flujo de reset

## Referencias
- https://portswigger.net/web-security/authentication
