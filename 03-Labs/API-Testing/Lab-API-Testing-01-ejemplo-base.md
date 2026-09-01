---
tipo: lab
vuln: api
nivel: practitioner
tags: [bscp, tipo/lab, vuln/api, nivel/practitioner, estado/pendiente]
fase: [1-acceso]
url: 
estado: pendiente
---

# API Testing · Lab 01 — Ejemplo base

## Objetivo
Reproducir el flujo genérico de API Testing contra `{{BASE}}` hasta cumplir el objetivo del examen.

## Fase(s)
- 1-acceso (adaptar a 2-admin / 3-secret según el lab concreto)

## Pasos realizados
1. Detectar el punto de inyección en `{{PARAM}}` siguiendo [[CS-API]].
2. Confirmar la vulnerabilidad con la sonda mínima.
3. Explotar con la plantilla parametrizada correspondiente.

## Payload usado
Ver plantillas parametrizadas en [[CS-API]] (placeholders `{{BASE}}`, `{{PARAM}}`, `{{COLLAB}}`).

## Qué generalizo
La lección reutilizable que devuelvo a la cheat sheet tras resolver el lab.

## Enlace academy
- https://portswigger.net/web-security/api-testing
