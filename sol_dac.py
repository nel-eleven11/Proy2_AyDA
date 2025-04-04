import time

MOD = 10**9 + 7

# Función recursiva para calcular el número de montañas rusas
def contar_montanias(L, H, resultados):
    # Caso base: Si no hay tramos, solo hay una forma de estar a nivel 0 y con altura máxima 0
    if L == 0:
        return 1 if H == 0 else 0

    # Verificar si ya hemos calculado este subproblema
    if (L, H) in resultados:
        return resultados[(L, H)]

    # Caso en que la montaña finaliza en altura 0 (el último tramo es descendente)
    res = contar_montanias(L - 1, H, resultados)

    # Caso en que la montaña finaliza en una altura máxima mayor a 0
    if H > 0:
        res = (res + contar_montanias(L - 1, H - 1, resultados)) % MOD
        res = (res + contar_montanias(L - 1, H, resultados)) % MOD

    # Guardamos el resultado para evitar recalcularlo
    resultados[(L, H)] = res
    return res

# Función para procesar varias consultas
def calc_montanias(mon):
    resultados = {}
    for (L, H) in mon:
        print(contar_montanias(L, H, resultados))

# Ejemplo de uso con consultas (L, H)
montanias = [(2, 1), (3, 2), (4, 3)]

# Medición de tiempo
start_time = time.time()  # Tiempo de inicio

calc_montanias(montanias)

end_time = time.time()  # Tiempo de finalización
execution_time = end_time - start_time  # Calculamos el tiempo de ejecución

# Imprimimos el tiempo de ejecución
print(f"Tiempo de ejecución (Divide and Conquer): {execution_time:.6f} segundos")
