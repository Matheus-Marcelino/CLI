"""Calculo de tempo"""
from datetime import datetime


def Calculate_time(func):
    """Calcula o tempo da função"""
    def wrapper(*args, **kwgs):
        time_inicial = datetime.now()

        resultado = func(*args, **kwgs)

        time_final = datetime.now()

        time_total = time_final - time_inicial
        return resultado, time_total
    return wrapper
