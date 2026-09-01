---
tipo: moc
tags: [bscp, tipo/moc]
---

# 🔎 Triage de detección · señal → sospecha

> **Regla del examen: identifica primero, explota después.** Esta nota es para el "identifica".
> Cuando no sepas qué tienes delante, busca la **señal observable** aquí y salta a su cheat sheet.
> Corre **[[Burp-Scanner]]** en paralelo desde el minuto uno.

## A) Según qué acepta el parámetro `{{PARAM}}`
| Señal observable | Sospecha | Cheat sheet |
|---|---|---|
| Texto que acaba en una consulta a BD; una comilla rompe/cambia la respuesta | SQL Injection | [[CS-SQLi]] |
| Login/consulta con backend Mongo; operadores `$ne`/`$regex` cambian la respuesta | NoSQL Injection | [[CS-NoSQLi]] |
| Tu texto se **refleja** en la página (HTML/atributo/JS/URL) | XSS | [[CS-XSS]] |
| Tu texto llega a un **sink** del cliente (`location.hash` → `innerHTML`/`eval`) | DOM-based | [[CS-DOM]] |
| Acepta una **URL o host** | SSRF | [[CS-SSRF]] |
| Acepta **ruta o nombre de fichero** | Path Traversal | [[CS-Path-Traversal]] |
| Alimenta un **comando del sistema** | Command Injection | [[CS-CMDi]] |
| Una **expresión** se evalúa (`{{7*7}}` → 49) | SSTI | [[CS-SSTI]] |
| Cuerpo/entrada en **XML** (body, SOAP, SVG, DOCX) | XXE | [[CS-XXE]] |
| **JSON** con objetos anidados / propiedades tipo `__proto__` | Prototype Pollution | [[CS-Prototype-Pollution]] |

## B) Según el artefacto/formato que ves
| Señal observable | Sospecha | Cheat sheet |
|---|---|---|
| Cookie/token de **3 bloques base64url** separados por puntos | JWT | [[CS-JWT]] |
| Cookie/param **serializado** (`O:4:"..."`, base64 `rO0AB`, bytes `ac ed 00 05`) | Deserialización | [[CS-Deserializacion]] |
| Endpoint **`/graphql`** o consultas con `query { }` | GraphQL | [[CS-GraphQL]] |
| Endpoints **REST `/api/...`**, métodos y JSON | API testing | [[CS-API]] |
| Conexión **`ws://` / `wss://`** (WebSocket) | WebSockets | [[CS-WebSockets]] |

## C) Según la respuesta / cabeceras
| Señal observable | Sospecha | Cheat sheet |
|---|---|---|
| Refleja tu **`Origin`** con `Access-Control-Allow-Credentials: true` | CORS | [[CS-CORS]] |
| Un **header no incluido en la clave** se refleja y se **cachea** | Cache Poisoning | [[CS-Cache-Poisoning]] |
| Enlaces construidos con el **`Host`** (p. ej. el de reset de contraseña) | Host Header | [[CS-Host-Header]] |
| La página se puede **enmarcar** (sin `X-Frame-Options`/`frame-ancestors`) | Clickjacking | [[CS-Clickjacking]] |
| **Errores verbosos**, `/.git`, `.bak`, `.map`, cabeceras reveladoras | Information Disclosure | [[CS-Info-Disclosure]] |
| Front-end + back-end con **desincronización** por timing | Request Smuggling | [[CS-Smuggling]] |

## D) Según la funcionalidad / lógica
| Señal observable | Sospecha | Cheat sheet |
|---|---|---|
| Login, registro, **2FA**, reset de contraseña | Authentication | [[CS-Auth]] |
| Login social / "Sign in with…" (`redirect_uri`, `state`) | OAuth | [[CS-OAuth]] |
| Acción que **cambia estado** sin token anti-CSRF | CSRF | [[CS-CSRF]] |
| **`/admin`**, IDs de otros usuarios, cambiar rol | Access Control / IDOR | [[CS-Access-Control]] |
| Compra, descuentos, cantidades, pasos de un flujo | Business Logic | [[CS-Business-Logic]] |
| Canjear cupón/saldo, límites, doble uso simultáneo | Race Conditions | [[CS-Race-Conditions]] |
| Subida de ficheros | File Upload | [[CS-File-Upload]] |

## Sonda de 10 segundos (para confirmar rápido)
- Comilla `'` → ¿error/cambio? → **SQLi**
- Marcador único (`<svg onload=alert(1)>`) → ¿se ejecuta/refleja? → **XSS**
- `{{7*7}}` → ¿sale `49`? → **SSTI**
- `../../../etc/passwd` → ¿contenido del fichero? → **Path Traversal**
- Cambiar un `id` por el de otro → ¿ves datos ajenos? → **IDOR**
- `Origin: https://{{COLLAB}}` → ¿se refleja con credenciales? → **CORS**

## Enlaces
- [[MOC-BSCP]] · [[Metodologia-Discovery]] · [[Metodologia-Examen]] · [[Dashboard]]
