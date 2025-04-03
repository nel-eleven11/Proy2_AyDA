MOD = 10**9 + 7
MAX_L = 200
MAX_H = 200

# Inicializamos la matriz DP
dp = [[[0] * (MAX_H + 1) for _ in range(MAX_H + 1)] for _ in range(2 * MAX_L + 1)]
dp[0][0][0] = 1  # Caso base: 1 forma de tener 0 tramos y estar en la altura 0 con altura máxima 0

# Calculamos la DP bottom-up
for t in range(1, 2 * MAX_L + 1):
    for ch in range(MAX_H + 1):  # Iteramos sobre todas las posibles alturas
        for mh in range(MAX_H + 1):  # Iteramos sobre todas las posibles alturas máximas alcanzables
            # Si estamos en la altura 0, el último tramo debe ser descendente
            if ch == 0:
                dp[t][ch][mh] = dp[t-1][1][mh]  # Solo puede ser ascendente el tramo anterior
            # Si estamos en una altura intermedia (0 < ch < mh), el tramo anterior puede ser ascendente o descendente
            elif 0 < ch < mh:
                dp[t][ch][mh] = (dp[t-1][ch-1][mh] + dp[t-1][ch+1][mh]) % MOD
            # Si estamos en la altura máxima (ch == mh), solo puede ser ascendente el tramo anterior
            elif ch == mh:
                dp[t][ch][mh] = (dp[t-1][mh-1][mh] + dp[t-1][mh-1][mh-1]) % MOD

# Función para responder las consultas
def responder_consultas(queries):
    resultados = []
    for (L, H) in queries:
        # La respuesta es dp[2*L][0][H], que es el número de montañas rusas de longitud L y altura máxima H
        resultados.append(dp[2*L][0][H])
    return resultados

# Ejemplo de uso con consultas (L, H)
queries = [(2, 1), (3, 2), (4, 3)]
resultados = responder_consultas(queries)

# Imprimimos los resultados
for resultado in resultados:
    print(resultado)

