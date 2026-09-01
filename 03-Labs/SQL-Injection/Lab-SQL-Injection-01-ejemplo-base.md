---
tipo: lab
vuln: sqli
nivel: practitioner
tags: [bscp, tipo/lab, vuln/sqli, nivel/practitioner, estado/pendiente]
fase: [1-acceso]
url: 
estado: pendiente
---

# SQL Injection · Lab 01 — Ejemplo base

## Objetivo
Reproducir el flujo genérico de SQL Injection contra `{{BASE}}` hasta cumplir el objetivo del examen.

## Fase(s)
- 1-acceso (adaptar a 2-admin / 3-secret según el lab concreto)

## Pasos realizados
1. Detectar el punto de inyección en `{{PARAM}}` siguiendo [[CS-SQLi]].
2. Confirmar la vulnerabilidad con la sonda mínima.
3. Explotar con la plantilla parametrizada correspondiente.

## Payload usado
Ver plantillas parametrizadas en [[CS-SQLi]] (placeholders `{{BASE}}`, `{{PARAM}}`, `{{COLLAB}}`).

## Qué generalizo
La lección reutilizable que devuelvo a la cheat sheet tras resolver el lab.

## Enlace academy
- https://portswigger.net/web-security/sql-injection
