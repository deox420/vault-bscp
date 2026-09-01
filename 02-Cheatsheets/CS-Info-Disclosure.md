---
tipo: cheatsheet
vuln: info-disclosure
tags: [bscp, tipo/cheatsheet, vuln/info-disclosure]
relacionada: "[[Information-Disclosure]]"
---

# CS · Information Disclosure

## Flujo repetible
1. Provoca y lee mensajes de error, y revisa recursos expuestos.
2. Recolecta rutas, versiones, comentarios, backups y ficheros de control.
3. Usa lo filtrado como entrada para otra vulnerabilidad (rutas, credenciales, tokens).

## Detección
```
/robots.txt   /sitemap.xml   (rutas ocultas anunciadas)
Envía tipos/valores inesperados en {{PARAM}} para forzar un stack trace verboso.
```

## Plantillas de payload
```
# Recursos y control expuestos
{{BASE}}/robots.txt
{{BASE}}/.git/HEAD                      (repositorio expuesto)
{{BASE}}/backup.zip   {{BASE}}/index.php.bak
{{BASE}}/main.js.map                    (source map -> código fuente)
```
```
# Forzar fugas por error / debug
TRACE {{BASE}}/                         (reflejo de headers)
{{PARAM}}=[]    {{PARAM}}='            (tipos inesperados -> stack trace)
Cabeceras reveladoras: Server, X-Powered-By, X-Debug
```

## Escalada al objetivo
Usar rutas/credenciales/tokens filtrados → login/admin → leer {{SECRET_PATH}}.

## Checklist
- [ ] Revisé robots.txt / sitemap / .git / backups
- [ ] Forcé errores verbosos en {{PARAM}}
- [ ] Revisé source maps y cabeceras reveladoras
- [ ] Reutilicé lo filtrado para escalar

## Referencias
- https://portswigger.net/web-security/information-disclosure
