# Predicción de accidente cerebrovascular — Grupo X

El accidente cerebrovascular es la segunda causa de muerte a nivel mundial y una fracción relevante de los casos ocurre en pacientes con factores de riesgo registrados con anterioridad. El problema es de clasificación binaria: estimar, a partir de variables demográficas, clínicas y de hábitos, la probabilidad de que un paciente presente el evento.

## Integrantes
- Nombre Apellido (@usuario-github)
- Nombre Apellido (@usuario-github)
- Nombre Apellido (@usuario-github)

## Datos
- Fuente: Stroke Prediction Dataset (fedesoriano, Kaggle)
- Enlace: https://www.kaggle.com/datasets/fedesoriano/stroke-prediction-dataset
- Estructura: 5110 filas x 12 columnas
- Ubicación esperada: `data/raw/`

## Estructura del repositorio
```
data/raw/        datos originales, sin modificar
data/processed/  datos procesados (F2) y entregables para la Fase 4 (F3)
docs/            diccionario, fichas y metadatos
src/             módulos reutilizables: carga, transformadores, pipeline y medición (F3), comunicación (F4)
F1/ F2/ F3/ F4/  cuadernos e informes de cada fase; F4/figuras/ guarda las figuras del informe
```

## Requisitos y ejecución
Python 3.13

    python -m venv .venv
    source .venv/Scripts/activate    # Windows, Git Bash
    # source .venv/bin/activate      # macOS y Linux
    python -m pip install -r requirements.txt

Ejecutar los cuadernos en orden: F1, F2, F3 y F4. Cada cuaderno localiza la raíz del
proyecto aunque Jupyter lo abra en su propia carpeta. El cuaderno de F4 parte de los
artefactos que F3 deja en `data/processed/` y se detiene si no los encuentra.

### Dependencias declaradas
- ipykernel
- jupyterlab
- notebook
- numpy==2.5.4
- pandas==3.1.0
- matplotlib==3.11.2

## Convención de commits
Prefijos usados: docs, data, feat, fix.

## Decisiones técnicas
- Los datos son comunes a todas las fases (`data/`); los cuadernos se separan por fase.
- Semilla aleatoria fijada en 42 para asegurar reproducibilidad.
- Registro breve de las decisiones relevantes y su motivo, actualizado al cerrar cada fase.
