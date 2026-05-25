# TP Análisis de Ventas

## Universidad Tecnológica Nacional
Tecnicatura Universitaria en Programación (TUP) 
Materia: Organización Empresarial  
Trabajo Práctico N° 2  
Alumna: Marcela Livio  
---
## Descripción del Proyecto
Este proyecto consiste en la implementación de un flujo completo de gestión y desarrollo técnico aplicando herramientas de organización empresarial, control de versiones y automatización de análisis de datos.
Se desarrolló un script en Python para procesar un dataset de ventas, generar métricas descriptivas y producir artefactos de salida automatizados.

---
## Objetivos
- Aplicar gestión de tareas mediante Jira.
- Implementar trazabilidad entre planificación y desarrollo técnico.
- Utilizar Git y GitHub para control de versiones.
- Aplicar flujo de trabajo distribuido desde Google Colab.
- Automatizar procesamiento de datos con Python.
- Implementar buenas prácticas de seguridad y documentación.

---
## Estructura del Proyecto
```text
tp-analisis-ventas/
│
├── datos/
│   └── sales_sample_2024.csv
│
├── scripts/
│   └── analisis_ventas.py
│
├── resultados/
│   ├── resumen_ventas.csv
│   └── ventas_diarias.png
│
└── README.md

---
## Tecnologías Utilizadas

- Python
- pandas
- matplotlib
- Google Colab
- Git
- GitHub
- Jira

---
## Funcionalidades Implementadas
El script realiza:

- carga de dataset CSV
- conversión de fechas
- análisis descriptivo
- cálculo de ventas totales
- cálculo de promedio diario
- identificación del mejor y peor día
- generación automática de archivo resumen
- generación de gráfico de ventas

---
## Ejecución
Desde Google Colab: !python scripts/analisis_ventas.py

---
## Gestión del Proyecto
Se utilizó Jira para planificación y seguimiento de tareas mediante tablero Kanban.
Issues implementados:

- KAN-1: Configuración inicial del proyecto y repositorio
- KAN-2: Desarrollo del análisis automatizado
- KAN-3: Seguridad, documentación y entrega final

---
## Control de Versiones
Se aplicó trazabilidad entre Jira y Git mediante commits identificados con el ID del issue correspondiente.
Ejemplos:

KAN-1: Actualización de documentación inicial
KAN-2: Implementar análisis automatizado de ventas
KAN-3: Agregar configuración de seguridad con gitignore

---
## Repositorio

Repositorio GitHub:  
https://github.com/marcelalivio/tp-analisis-ventas
