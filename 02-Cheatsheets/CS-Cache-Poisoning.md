---
tipo: cheatsheet
vuln: cache-poisoning
tags: [bscp, tipo/cheatsheet, vuln/cache-poisoning]
relacionada: "[[Cache-Poisoning]]"
---

# CS · Cache Poisoning

## Flujo repetible
1. Busca entradas no incluidas en la clave (headers).
2. Consigue que se reflejen con payload.
3. Fuerza el guardado en caché (usa cache buster al probar).

## Detección
```
Añade un header no incluido en la clave y observa si se refleja en la respuesta de {{BASE}}.
Usa un cache buster (?cb={{N}}) para no envenenar entradas reales mientras pruebas.
```

## Plantillas de payload
```
X-Forwarded-Host: {{EXPLOIT}}      (si acaba en <script src>)
X-Host / X-Forwarded-Scheme
```

## Escalada al objetivo
Servir XSS/redirect cacheado a todas las víctimas (incluido {{VICTIM}}).

## Checklist
- [ ] Identifiqué input no incluido en la clave
- [ ] Reflejé y caché el payload
- [ ] Verifiqué con cache buster

## Referencias
- https://portswigger.net/web-security/web-cache-poisoning
