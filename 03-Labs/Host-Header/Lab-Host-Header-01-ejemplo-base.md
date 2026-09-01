---
tipo: lab
vuln: host-header
nivel: practitioner
tags: [bscp, tipo/lab, vuln/host-header, nivel/practitioner, estado/pendiente]
fase: [1-acceso]
url: 
estado: pendiente
---

# Host Header · Lab 01 — Ejemplo base

## Objetivo
Reproducir el flujo genérico de Host Header contra `{{BASE}}` hasta cumplir el objetivo del examen.

## Fase(s)
- 1-acceso (adaptar a 2-admin / 3-secret según el lab concreto)

## Pasos realizados
1. Detectar el punto de inyección en `{{PARAM}}` siguiendo [[CS-Host-Header]].
2. Confirmar la vulnerabilidad con la sonda mínima.
3. Explotar con la plantilla parametrizada correspondiente.

## Payload usado
Ver plantillas parametrizadas en [[CS-Host-Header]] (placeholders `{{BASE}}`, `{{PARAM}}`, `{{COLLAB}}`).

## Qué generalizo
La lección reutilizable que devuelvo a la cheat sheet tras resolver el lab.

## Enlace academy
- https://portswigger.net/web-security/host-header
