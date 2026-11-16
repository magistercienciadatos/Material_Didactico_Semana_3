"""Comunicación de resultados: del conjunto procesado a la figura que responde.

Módulo del proyecto modelo MCDI500 (Fase 4). El cuaderno
F4/S3_F4_Visualizacion_Comunicacion.ipynb lo importa y verifica que sus resultados
coinciden con un cálculo independiente sobre el archivo original.

La Fase 4 no vuelve a limpiar ni a transformar: lee los cuatro artefactos de la
Fase 3 y construye una copia interpretable, con las unidades originales, para
poder graficar y comunicar.
"""

import ast
import math
import os

import pandas as pd


ARTEFACTOS_F3 = {
    "entrenamiento": "entrenamiento_f3.csv",
    "prueba": "prueba_f3.csv",
    "diccionario": "diccionario_f3.csv",
    "parametros": "parametros_f3.csv",
}


def cargar_artefactos(carpeta):
    """Lee los cuatro artefactos que entrega la Fase 3.

    Si falta alguno, se detiene con un mensaje que dice qué hacer: la Fase 4 no
    debe inventar datos para poder seguir.
    """
    faltantes = [archivo for archivo in ARTEFACTOS_F3.values()
                 if not os.path.exists(os.path.join(carpeta, archivo))]
    if faltantes:
        raise FileNotFoundError(
            f"Faltan artefactos de la Fase 3 en {carpeta}: {faltantes}. "
            "Ejecuten primero el cuaderno de F3, que los escribe en data/processed."
        )
    return {nombre: pd.read_csv(os.path.join(carpeta, archivo))
            for nombre, archivo in ARTEFACTOS_F3.items()}


def leer_parametros(tabla_parametros):
    """Convierte la tabla de parámetros de la Fase 3 en un diccionario por paso.

    La Fase 3 guardó cada diccionario como texto. ast.literal_eval lo convierte
    de vuelta sin ejecutar código, a diferencia de eval, que sí lo haría.
    """
    parametros = {}
    for _, fila in tabla_parametros.iterrows():
        try:
            parametros[fila["paso"]] = ast.literal_eval(fila["parametros"])
        except (ValueError, SyntaxError) as error:
            raise ValueError(
                f"Parámetros ilegibles en el paso {fila['paso']}: {fila['parametros']!r}"
            ) from error
    return parametros


def _etiqueta(categoria):
    """Repite la limpieza de nombres que aplicó el CodificadorNominal de F3."""
    return str(categoria).strip().replace(" ", "_").replace("-", "_")


def revertir_escalamiento(df, parametros):
    """Devuelve una copia con las continuas en sus unidades originales.

    Aplica la inversa exacta del EscaladorEstandar: x = z * desviacion + media,
    con la media y la desviación que aprendió la Fase 3 del entrenamiento.
    """
    resultado = df.copy()
    for paso, valores in parametros.items():
        if paso.startswith("EscaladorEstandar("):
            columna = paso[len("EscaladorEstandar("):-1]
            resultado[columna] = resultado[columna] * valores["desviacion"] + valores["media"]
    return resultado


def reconstruir_categorias(df, parametros):
    """Vuelve a juntar las columnas 0/1 en una sola columna con la categoría.

    Usa el vocabulario que aprendió la Fase 3, no las columnas que encuentre, para
    que una categoría inesperada se detecte en vez de pasar inadvertida.
    """
    resultado = df.copy()
    for paso, valores in parametros.items():
        if not paso.startswith("CodificadorNominal("):
            continue
        columna = paso[len("CodificadorNominal("):-1]
        indicadoras = {f"{columna}_{_etiqueta(c)}": c for c in valores["categorias"]}
        faltan = [c for c in indicadoras if c not in resultado.columns]
        if faltan:
            raise KeyError(f"Faltan columnas indicadoras de {columna}: {faltan}")
        bloque = resultado[list(indicadoras)]
        if not (bloque.sum(axis=1) == 1).all():
            raise ValueError(f"{columna}: hay filas sin exactamente una categoría activa.")
        resultado[columna] = bloque.idxmax(axis=1).map(indicadoras)
        resultado = resultado.drop(columns=list(indicadoras))
    return resultado


def copia_interpretable(df, parametros):
    """Encadena las dos operaciones: unidades originales y categorías legibles."""
    return reconstruir_categorias(revertir_escalamiento(df, parametros), parametros)


def intervalo_wilson(exitos, total, z=1.96):
    """Intervalo de confianza de Wilson para una proporción.

    Se prefiere al intervalo normal porque no da límites negativos cuando la
    proporción es pequeña, que es justamente el caso de la clase positiva.
    """
    if total == 0:
        raise ValueError("No se puede estimar una proporción sin observaciones.")
    p = exitos / total
    denominador = 1 + z ** 2 / total
    centro = (p + z ** 2 / (2 * total)) / denominador
    margen = z * math.sqrt(p * (1 - p) / total + z ** 2 / (4 * total ** 2)) / denominador
    # Con 0 casos o con todos, el límite es exacto: se fija para que el redondeo
    # de punto flotante no deje un 1e-17 donde debe haber un cero
    inferior = 0.0 if exitos == 0 else max(0.0, centro - margen)
    superior = 1.0 if exitos == total else min(1.0, centro + margen)
    return inferior, superior


def tasa_por_grupo(df, grupo, objetivo):
    """Tasa del evento por grupo, con tamaño e intervalo de confianza al 95 %."""
    filas = []
    for valor, sub in df.groupby(grupo, observed=True):
        n = len(sub)
        casos = int(sub[objetivo].sum())
        inferior, superior = intervalo_wilson(casos, n)
        filas.append({grupo: valor, "n": n, "casos": casos, "tasa": casos / n,
                      "ic_inferior": inferior, "ic_superior": superior})
    return pd.DataFrame(filas)


def guardar_figura(figura, carpeta, nombre, dpi=200):
    """Guarda la figura en PNG con resolución de impresión y devuelve la ruta."""
    os.makedirs(carpeta, exist_ok=True)
    ruta = os.path.join(carpeta, f"{nombre}.png")
    figura.savefig(ruta, dpi=dpi, bbox_inches="tight")
    return ruta
