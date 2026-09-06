---
tipo: recurso
tags: [bscp, tipo/recurso]
---

# 🧩 Extensiones de Burp para el BSCP

> **Regla de oro:** instálalas, configúralas y **pruébalas ANTES** del examen. **No añadas nada nuevo durante** la prueba (una extensión puede modificar tus peticiones y romperte el examen).
> Instalar: **Extensions → BApp Store → Install**. Muchas necesitan **Burp Suite Professional** y Jython (Python) configurado.

Elige la extensión según lo que detectes en [[Triage-Deteccion]].

---

## HTTP Request Smuggler → [[CS-Smuggling]]
- **Qué hace:** detecta y explota desincronización HTTP (CL.TE / TE.CL / TE.TE / CL.0).
- **Cuándo:** siempre que haya front-end + back-end.
- **Cómo:** clic derecho en una petición → *Extensions → HTTP Request Smuggler → Smuggle probe* (detección automática); luego usa las plantillas que genera para explotar.

## Param Miner → [[CS-Cache-Poisoning]]
- **Qué hace:** descubre **headers y parámetros ocultos** por fuerza bruta con wordlists.
- **Cuándo:** cache poisoning, parámetros no documentados, mass assignment.
- **Cómo:** clic derecho → *Extensions → Param Miner → Guess headers / Guess params* → revisa la pestaña **Issues**.

## JWT Editor → [[CS-JWT]]
- **Qué hace:** decodifica, edita y **firma** tokens JWT.
- **Cuándo:** veas un token de 3 bloques base64url.
- **Cómo:** pestaña *JWT Editor Keys* (genera/importa claves) y, en Repeater, pestaña *JSON Web Token* para editar claims (rol → admin) y probar `alg:none`, secreto débil y confusión de algoritmo.

## Turbo Intruder → [[CS-Race-Conditions]]
- **Qué hace:** envío **masivo/paralelo** de peticiones con scripts Python.
- **Cuándo:** race conditions y fuerza bruta a volumen.
- **Cómo:** clic derecho → *Extensions → Turbo Intruder* → elige un script (p. ej. `race-single-packet-attack.py`) → marca las posiciones → *Attack*.

## InQL → [[CS-GraphQL]]
- **Qué hace:** **introspección** y explorador de esquemas GraphQL.
- **Cuándo:** endpoint `/graphql` o similar.
- **Cómo:** envía la petición GraphQL a InQL → genera el esquema y las queries → edítalas y lánzalas en Repeater.

## Autorize → [[CS-Access-Control]]
- **Qué hace:** prueba **control de acceso** repitiendo cada petición con el token de otro usuario (IDOR / escalada).
- **Cuándo:** verificar autorización en cada endpoint.
- **Cómo:** mete en Autorize la cookie/token de un usuario de **bajo privilegio** → navega como **admin** → Autorize marca cada petición como *Bypassed!* (vulnerable) o *Enforced!* (seguro).

## Hackvertor → [[CS-SQLi]] · [[CS-XSS]]
- **Qué hace:** codifica/transforma payloads con etiquetas dentro de la petición (`<@base64>…</@base64>`, `<@urlencode>…`).
- **Cuándo:** saltar filtros/WAF y codificar payloads sin salir de Repeater.
- **Cómo:** en Repeater, envuelve tu payload con las etiquetas y se convierte automáticamente al enviar.

---

## Específicas de SQL Injection → [[CS-SQLi]]
> Úsalas **solo como acelerador** cuando ya entiendas la inyección a mano. En el examen (cronometrado) **manual + Scanner** suele ir mejor.

### SQLiPy Sqlmap Integration
- **Qué hace:** lanza **sqlmap** contra una petición desde Burp.
- **Cómo:** arranca el API de sqlmap → clic derecho en la petición → *SQLiPy Scan* → configura y revisa resultados. ⚠️ Ruidoso y lento en labs de examen.

### CO2 (SQLMapper)
- **Qué hace:** te ayuda a **construir el comando de sqlmap** a partir de la petición.
- **Cómo:** pestaña *CO2 → SQLMapper* → pega los parámetros → copia el comando generado.

---

## Built-in esenciales (ya vienen, no son extensiones)
- **Scanner** → detección automática (SQLi, XSS, access control…). **Córrelo desde el minuto 1.** Ver [[Burp-Scanner]].
- **DOM Invader** (navegador de Burp) → DOM XSS y prototype pollution → [[CS-DOM]] · [[CS-Prototype-Pollution]].
- **Collaborator** → OAST para vulnerabilidades **ciegas** (SSRF, XXE, SQLi ciega, CMDi) → usa `{{COLLAB}}`.
- **Repeater → "Send group in parallel"** (single-packet) → race conditions.

## Flujo en el examen
1. **Scanner** corriendo sobre todo el objetivo `{{BASE}}`.
2. Confirmas cada issue a mano en **Repeater**.
3. Según el [[Triage-Deteccion]], abres la **extensión** que toque.
4. Las **ciegas/OOB** se confirman con **Collaborator** (`{{COLLAB}}`).

## Checklist pre-examen (instalada + probada)
- [ ] HTTP Request Smuggler
- [ ] Param Miner
- [ ] JWT Editor
- [ ] Turbo Intruder
- [ ] InQL
- [ ] Autorize
- [ ] Hackvertor
- [ ] SQLiPy / CO2 (opcionales)

## Enlaces
- [[Burp-Scanner]] · [[Triage-Deteccion]] · [[MOC-BSCP]]
- https://portswigger.net/bappstore
