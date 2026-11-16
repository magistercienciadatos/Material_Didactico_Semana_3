"""Medición de tiempo y memoria de una función.

Módulo del proyecto modelo MCDI500. El código es el mismo que se desarrolla paso a
paso en F3/S2_F3_NucleoAlgoritmico_Eficiencia_POO.ipynb; el cuaderno verifica que ambas
versiones producen el mismo resultado.
"""

import time
import tracemalloc


def medir(funcion, *args, **kwargs):
    """Ejecuta la función y devuelve resultado, segundos y memoria pico en MB.

    *args recoge los argumentos posicionales en una tupla y **kwargs los
    argumentos con nombre en un diccionario. El asterisco es lo que hace el
    trabajo; los nombres args y kwargs son solo convención.
    """
    tracemalloc.start()
    inicio = time.perf_counter()
    resultado = funcion(*args, **kwargs)
    transcurrido = time.perf_counter() - inicio
    _, pico = tracemalloc.get_traced_memory()
    tracemalloc.stop()
    return resultado, transcurrido, pico / 1024 / 1024
