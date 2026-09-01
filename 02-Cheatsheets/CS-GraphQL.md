---
tipo: cheatsheet
vuln: graphql
tags: [bscp, tipo/cheatsheet, vuln/graphql]
relacionada: "[[GraphQL]]"
---

# CS · GraphQL

## Flujo repetible
1. Localiza el endpoint (/graphql, /api).
2. Introspección para mapear el esquema.
3. Abusa aliasing/batching e IDOR.

## Detección
```graphql
{__typename}                              # confirma endpoint GraphQL en {{BASE}}
```

## Plantillas de payload
```graphql
{__schema{types{name fields{name}}}}     # introspección
```
```
Aliasing/batching -> saltar rate-limit (fuerza bruta)
IDOR consultando IDs ajenos
Herramientas: InQL / visor GraphQL de Burp
```

## Escalada al objetivo
IDOR/aliasing para leer datos de {{TARGET_USER}} o forzar credenciales → acceso admin.

## Checklist
- [ ] Encontré el endpoint
- [ ] Corrí introspección
- [ ] Probé aliasing/batching e IDOR

## Referencias
- https://portswigger.net/web-security/graphql
