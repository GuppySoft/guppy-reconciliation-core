# guppy-reconciliation-core
# 🦊 GuppySoft: Fintech Reconciliation Engine (Core Demo)

![Python](https://img.shields.io/badge/Python-3.9+-blue.svg)
![Flask](https://img.shields.io/badge/Framework-Flask-lightgrey.svg)
![License](https://img.shields.io/badge/License-MIT-green.svg)

### "El software debe ser un puente de integridad financiera, nunca un acto de fe."

Este repositorio contiene módulos core extraídos de la plataforma **GuppySoft**. Es una demostración técnica de cómo procesar, auditar y conciliar liquidaciones masivas de pasarelas de pago (Mercado Pago, Clover) y entidades bancarias de forma automática.

## 🚀 El Problema: La "Caja Negra" de las Liquidaciones
Muchos negocios operan bajo el riesgo de errores en las liquidaciones de tarjetas: comisiones mal aplicadas, retenciones impositivas (IVA/IIBB) no declaradas o cobros que simplemente nunca llegan al banco. La conciliación manual en Excel es propensa a errores y consume cientos de horas hombre.

## 🛠️ Soluciones Técnicas Implementadas

Este motor resuelve estos desafíos mediante tres pilares de arquitectura:

### 1. Gestión de Concurrencia y Resiliencia de Datos
El sistema utiliza **SQLAlchemy** con una lógica avanzada de `flush` y `rollback` para manejar la creación de entidades en entornos de alta concurrencia, evitando duplicados y garantizando la integridad de la base de datos incluso si dos procesos intentan registrar la misma sucursal simultáneamente.

### 2. In-Memory Data Processing (Zero Footprint)
Para optimizar el rendimiento y la seguridad del servidor, el motor procesa archivos PDF y genera reportes Excel (.xlsx) directamente en memoria utilizando `io.BytesIO`. Esto elimina la necesidad de archivos temporales en disco y acelera la respuesta del sistema.

### 3. Auditoría y Prevención de Pérdidas
- **Cálculo Dinámico de Liquidación:** Algoritmos que predicen la fecha exacta de cobro según la marca de la tarjeta y la plataforma (Macro/MP).
- **Extracción de Tablas en PDFs:** Lógica de filtrado y normalización de datos desestructurados extraídos de liquidaciones bancarias.
- **Detección de Retrasos:** Sistema de alertas automáticas para transacciones que superan el tiempo esperado de acreditación.

## 🏗️ Arquitectura del Motor



## 💻 Stack Tecnológico
- **Lenguaje:** Python 3.9+
- **Procesamiento de Datos:** Pandas, NumPy
- **ORMs:** SQLAlchemy (PostgreSQL/MySQL)
- **Integraciones:** Mercado Pago API, WooCommerce REST API
- **Reporting:** Openpyxl (Excel Engine)

---
**Nota:** Este código es una versión de demostración técnica. El sistema completo incluye módulos de IA (XGBoost) para predicción de stock y una interfaz administrativa completa diseñada bajo la marca **GuppySoft**.

## ⚖️ Licencia
Este fragmento de código está bajo la licencia MIT. Ver el archivo `LICENSE` para más detalles.
