---
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
