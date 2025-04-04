import time

MOD = 10**9 + 7
MAX_L = 200
MAX_H = 200

# Inicializamos la matriz DP
res_montanias = [[[0] * (MAX_H + 1) for _ in range(MAX_H + 1)] for _ in range(2 * MAX_L + 1)]
# Caso base:
res_montanias[0][0][0] = 1

# Calculamos la DP bottom-up
for t in range(1, 2 * MAX_L + 1):
    for ch in range(MAX_H + 1):
        for mh in range(MAX_H + 1):
            # Si estamos en la altura 0, el último tramo debe ser descendente
            if ch == 0:
                res_montanias[t][ch][mh] = res_montanias[t-1][1][mh]  # Solo puede ser ascendente el tramo anterior
            # Si estamos en una altura intermedia (0 < ch < mh), el tramo anterior puede ser ascendente o descendente
            elif 0 < ch < mh:
                res_montanias[t][ch][mh] = (res_montanias[t-1][ch-1][mh] + res_montanias[t-1][ch+1][mh]) % MOD
            # Si estamos en la altura máxima (ch == mh), solo puede ser ascendente el tramo anterior
            elif ch == mh:
                res_montanias[t][ch][mh] = (res_montanias[t-1][mh-1][mh] + res_montanias[t-1][mh-1][mh-1]) % MOD

# Obtener las montañas
def resultado_montanias(mon):
    resultados = []
    for (L, H) in mon:
        resultados.append(res_montanias[2*L][0][H])
    return resultados


montanias = [(2, 1), (3, 2), (4, 3)]

# Medición de tiempo
start_time = time.time()

resultados = resultado_montanias(montanias)

end_time = time.time()
execution_time = end_time - start_time

# Imprimimos los resultados y el tiempo de ejecución
for resultado in resultados:
    print(resultado)

print(f"Tiempo de ejecución (Programación Dinámica Bottom-Up): {execution_time:.6f} segundos")
