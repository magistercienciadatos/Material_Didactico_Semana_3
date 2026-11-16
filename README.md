# MCDI500 · Material didáctico de la Semana 3

Programación para la Ciencia de Datos · Magíster en Ciencia de Datos e Inteligencia Artificial · Universidad Andrés Bello

La Semana 3 cubre la Fase 4 del proyecto: visualización y comunicación de resultados, e integración de las cuatro fases. Se evalúa con la Sumativa de la Fase 4 (informe de hasta 10 páginas, notebooks, repositorio y video de 5 a 8 minutos, 150 puntos, 30% de la nota) y la autoevaluación y coevaluación (10%).

## Contenido

| Carpeta | Qué contiene | Cuándo usarla |
| --- | --- | --- |
| `1_Presentación_Semana3` | Presentación de la semana, en PDF y PowerPoint | Antes de la sesión sincrónica |
| `2_Parte_Práctica` | Cuaderno práctico, de la pregunta a la figura, con los datos del caso | Durante la semana, en orden |
| `3_Guías_de_Apoyo` | Guía de la Sumativa de la Fase 4, apunte teórico y cuaderno guía `f4_s03_guia_visualizacion.ipynb` | Antes de empezar la entrega |
| `proyecto-grupoX-mcdi500` | Proyecto modelo con el caso docente (Stroke Prediction Dataset), completo de F1 a F4 | Como referencia para el repositorio del grupo |

## El proyecto modelo en la Fase 4

Es el mismo proyecto de las Semanas 1 y 2, con la misma estructura, y agrega la carpeta `F4`. El cuaderno `F4/S3_F4_Visualizacion_Comunicacion.ipynb` **no vuelve a limpiar ni a transformar**: lee los cuatro artefactos que la Fase 3 dejó en `data/processed/` (`entrenamiento_f3.csv`, `prueba_f3.csv`, `diccionario_f3.csv` y `parametros_f3.csv`), verifica que cumplen el contrato y construye una copia con las unidades originales para graficar.

Las funciones nuevas de la fase están en `src/comunicacion.py`, junto a los módulos de la Fase 3, y el cuaderno las importa igual que la Fase 3 importa `src/pipeline.py`. La copia interpretable se verifica contra el archivo original de `data/raw`, no contra el mismo código que la produjo.

Los cuadernos se ejecutan en orden: F1, F2, F3 y F4. Si faltan los artefactos de la Fase 3, el cuaderno de F4 se detiene con un mensaje que indica qué ejecutar; no genera datos de reemplazo.

Al final, el cuaderno deja:

- seis figuras en `F4/figuras/`, a 200 ppp, una por pregunta u objetivo;
- la tabla `docs/hallazgos_f4.csv`, con la cifra que respalda cada hallazgo;
- los metadatos de la ejecución en `docs/metadatos_f4.json`.

## Cómo usar el cuaderno guía

`3_Guías_de_Apoyo/f4_s03_guia_visualizacion.ipynb` es un esqueleto con marcas `TODO`. Cópienlo en la carpeta `F4/` de su repositorio, junto con `src/comunicacion.py` en su carpeta `src/`, y complétenlo con su propio conjunto.

## Dependencias

El proyecto modelo usa NumPy, pandas y matplotlib, declarados en `proyecto-grupoX-mcdi500/requirements.txt`. La parte práctica usa además seaborn en la sección 5.6:

    python -m pip install seaborn
