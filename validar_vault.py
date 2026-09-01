# -*- coding: utf-8 -*-
"""Validador del vault BSCP (TDD). Sale con codigo != 0 si algo falla.

Comprueba los 9 criterios de la SPEC (seccion 4). Ejecutar desde la raiz del vault:
    python validar_vault.py
"""
import os, re, sys, time

try:
    sys.stdout.reconfigure(encoding="utf-8")
except Exception:
    pass

ROOT = os.path.dirname(os.path.abspath(__file__))
errores = []
def fail(msg): errores.append(msg)

# --- Utilidades -----------------------------------------------------------
EXCLUDE_DIRS = {".obsidian", "copilot", ".trash", "node_modules", ".git"}
# Ficheros de instrucciones que generan los plugins/agentes (no son notas del vault)
EXCLUDE_FILES = {"CLAUDE.md", "GEMINI.md", "GEMINÍ.md"}
def md_files():
    for dp, dns, fns in os.walk(ROOT):
        dns[:] = [d for d in dns if d not in EXCLUDE_DIRS and not d.startswith(".")]  # no entrar en carpetas de plugins/sistema
        for fn in fns:
            if fn.endswith(".md") and fn not in EXCLUDE_FILES:
                yield os.path.join(dp, fn)

def is_template(path):
    return os.path.normpath("00-Index/_Plantillas") in os.path.normpath(path)

def parse_frontmatter(text):
    """Devuelve (dict, cuerpo) o (None, text) si no hay frontmatter parseable."""
    if not text.startswith("---"):
        return None, text
    m = re.match(r"^---\n(.*?)\n---\n?(.*)$", text, re.S)
    if not m:
        return None, text
    raw, body = m.group(1), m.group(2)
    d = {}
    for line in raw.splitlines():
        if not line.strip() or line.strip().startswith("#"):
            continue
        mm = re.match(r"^([A-Za-z0-9_-]+):\s?(.*)$", line)
        if not mm:
            return None, text  # linea de YAML no parseable
        k, v = mm.group(1), mm.group(2).strip()
        if v.startswith("[") and v.endswith("]"):
            inner = v[1:-1].strip()
            d[k] = [x.strip() for x in inner.split(",") if x.strip()] if inner else []
        else:
            d[k] = v
    return d, body

def read(path):
    for intento in range(5):
        try:
            with open(path, "r", encoding="utf-8") as f:
                return f.read()
        except OSError:
            if intento == 4:
                raise
            time.sleep(0.2)

REQUIRED = {
    "vulnerabilidad": ["tipo","vuln","tags","niveles","cheatsheet","academy","estado"],
    "cheatsheet":     ["tipo","vuln","tags","relacionada"],
    "lab":            ["tipo","vuln","nivel","tags","fase","url","estado"],
}
TAG_PREFIXES = ("tipo/","vuln/","nivel/","fase/","estado/")
CS_SECTIONS = ["## Flujo repetible","## Detección","## Plantillas de payload",
               "## Escalada al objetivo","## Checklist","## Referencias"]

# --- 1. Carpetas obligatorias (1.1) --------------------------------------
REQ_DIRS = [
    "00-Index","00-Index/_Plantillas","01-Vulnerabilidades","02-Cheatsheets",
    "03-Labs","04-Recon-y-Herramientas","99-Recursos",
]
for d in REQ_DIRS:
    if not os.path.isdir(os.path.join(ROOT, d)):
        fail(f"[1] Falta la carpeta obligatoria: {d}")

# Recolecta indice de notas (basename sin extension) para wikilinks
note_index = set()
for p in md_files():
    note_index.add(os.path.splitext(os.path.basename(p))[0])

# --- 2/3/7. Frontmatter, claves y tags -----------------------------------
frontmatters = {}
for p in md_files():
    text = read(p)
    fm, body = parse_frontmatter(text)
    if fm is None:
        fail(f"[2] Frontmatter YAML ausente o no parseable: {os.path.relpath(p, ROOT)}")
        continue
    frontmatters[p] = (fm, body)
    if "tipo" not in fm:
        fail(f"[3] Falta la clave 'tipo': {os.path.relpath(p, ROOT)}")
        continue
    if is_template(p):
        continue  # las plantillas no se validan por claves/wikilinks
    tipo = fm["tipo"]
    for k in REQUIRED.get(tipo, []):
        if k not in fm:
            fail(f"[3] {os.path.relpath(p, ROOT)} (tipo={tipo}) sin clave obligatoria: {k}")
    for tag in fm.get("tags", []):
        if tag != "bscp" and not tag.startswith(TAG_PREFIXES):
            fail(f"[7] Tag con prefijo invalido en {os.path.relpath(p, ROOT)}: {tag}")

# --- 4. 1 vuln + 1 cheatsheet por tema (28 de cada) ----------------------
vuln_dir = os.path.join(ROOT, "01-Vulnerabilidades")
cs_dir = os.path.join(ROOT, "02-Cheatsheets")
n_vuln = len([f for f in os.listdir(vuln_dir) if f.endswith(".md")]) if os.path.isdir(vuln_dir) else 0
n_cs = len([f for f in os.listdir(cs_dir) if f.endswith(".md")]) if os.path.isdir(cs_dir) else 0
if n_vuln != 28:
    fail(f"[4] Se esperaban 28 notas de vulnerabilidad, hay {n_vuln}")
if n_cs != 28:
    fail(f"[4] Se esperaban 28 cheat sheets, hay {n_cs}")

# --- 5. Cada vuln referencia una cheatsheet existente --------------------
for p, (fm, body) in frontmatters.items():
    if is_template(p) or fm.get("tipo") != "vulnerabilidad":
        continue
    ref = fm.get("cheatsheet", "")
    m = re.search(r"\[\[([^\]]+)\]\]", ref)
    if not m:
        fail(f"[5] {os.path.relpath(p, ROOT)}: frontmatter 'cheatsheet' sin wikilink")
        continue
    target = m.group(1).split("|")[0].split("#")[0].strip()
    if target not in note_index:
        fail(f"[5] {os.path.relpath(p, ROOT)}: cheatsheet inexistente -> {target}")

# --- 6. Todos los wikilinks resuelven ------------------------------------
for p, (fm, body) in frontmatters.items():
    if is_template(p):
        continue
    full = read(p)
    for m in re.finditer(r"\[\[([^\]]+)\]\]", full):
        target = m.group(1).split("|")[0].split("#")[0].strip()
        if target not in note_index:
            fail(f"[6] Wikilink roto en {os.path.relpath(p, ROOT)}: [[{target}]]")

# --- 8/9. Cheat sheets: 6 secciones, sin hosts de lab, con placeholder ---
if os.path.isdir(cs_dir):
    for f in os.listdir(cs_dir):
        if not f.endswith(".md"):
            continue
        p = os.path.join(cs_dir, f)
        text = read(p)
        for sec in CS_SECTIONS:
            if sec not in text:
                fail(f"[8] {f}: falta la seccion obligatoria '{sec}'")
        if "web-security-academy.net" in text:
            fail(f"[9] {f}: contiene host de laboratorio hardcodeado (web-security-academy.net)")
        if "{{" not in text:
            fail(f"[9] {f}: no usa ningun placeholder {{{{...}}}}")

# --- Resumen --------------------------------------------------------------
tipos = {}
for p, (fm, body) in frontmatters.items():
    if is_template(p):
        tipos["plantilla"] = tipos.get("plantilla", 0) + 1
    else:
        t = fm.get("tipo", "?")
        tipos[t] = tipos.get(t, 0) + 1

print("=" * 56)
print("RESUMEN DE VALIDACION DEL VAULT BSCP")
print("=" * 56)
for t in sorted(tipos):
    print(f"  notas tipo {t:16s}: {tipos[t]}")
print(f"  cheat sheets                : {n_cs}")
print(f"  notas de vulnerabilidad     : {n_vuln}")
print("-" * 56)
if errores:
    print(f"FALLOS: {len(errores)}\n")
    for e in errores:
        print("  ✗", e)
    print("\nExit code 1")
    sys.exit(1)
else:
    print("Todos los tests pasaron. ✓")
    print("Exit code 0")
    sys.exit(0)
