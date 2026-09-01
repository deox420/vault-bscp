---
tipo: cheatsheet
vuln: jwt
tags: [bscp, tipo/cheatsheet, vuln/jwt]
relacionada: "[[JWT]]"
---

# CS · JWT

## Flujo repetible
1. Identifica el token (3 bloques base64url).
2. Prueba alg:none, secreto débil y confusión de algoritmo.
3. Forja el token de {{TARGET_USER}}.

## Detección
```
Decodifica header y payload (base64url). Observa alg, kid, jwk/jku y el claim de rol.
```

## Plantillas de payload
```
alg:none        -> header {"alg":"none"}, firma vacía (deja el punto final)
HMAC débil      -> crackear (hashcat -m 16500 / jwt-tool)
kid injection   -> path traversal o SQLi en kid
jwk/jku         -> firmar con tu clave y alojar JWK en {{EXPLOIT}}
RS256 -> HS256  -> usar la clave pública como secreto HMAC
```

## Escalada al objetivo
Forjar token con rol admin (usuario {{TARGET_USER}}) → panel admin.

## Checklist
- [ ] Probé alg:none
- [ ] Probé secreto débil
- [ ] Probé confusión de algoritmo

## Referencias
- https://portswigger.net/web-security/jwt
