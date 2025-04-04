#sol_dac.py

MOD = 10**9 + 7
MAX_L = 200
MAX_H = 200

montanias = [[[-1 for _ in range(MAX_H + 1)] for __ in range(MAX_H + 1)] for ___ in range(2 * MAX_L + 1)]

# Función recursiva para calcular el número de montañas rusas
def contar_montanias(t, ch, mh):
    # Caso base: Si no hay tramos, solo hay una forma de estar a nivel 0 y con altura máxima 0
    if t == 0:
        return 1 if (ch == 0 and mh == 0) else 0

    # Verificar límites
    if ch < 0 or ch > MAX_H or mh < 0 or mh > MAX_H:
        return 0

    # Verificar si ya hemos calculado este estado
    if montanias[t][ch][mh] != -1:
        return montanias[t][ch][mh]

    result = 0

    # Caso 1: estamos al nivel del suelo (c = 0)
    if ch == 0:
        # El tramo anterior solo puede ser descendente (viniendo de altura 1)
        result = contar_montanias(t-1, 1, mh)

    # Caso 2: estamos en la altura máxima
    elif ch == mh:
        # El tramo anterior debe ser ascendente (viniendo de mh-1)
        # Dos subcasos:
        # 1. La altura máxima ya se había alcanzado antes
        # 2. Este es el primer punto donde se alcanza la altura máxima
        if mh > 0:
            case1 = contar_montanias(t-1, mh-1, mh)
            case2 = contar_montanias(t-1, mh-1, mh-1)
            result = (case1 + case2) % MOD

    # Caso 3: estamos en una altura intermedia (0 < ch < mh)
    else:
        # El tramo anterior puede ser ascendente o descendente
        if ch > 0 and mh > 0:
            ascend = contar_montanias(t-1, ch-1, mh)
            descend = contar_montanias(t-1, ch+1, mh)
            result = (ascend + descend) % MOD

    # Almacenar el resultado en la tabla de memoization
    montanias[t][ch][mh] = result
    return result

def calc_montanias(consultas):
    for (L, H) in consultas:
        res = contar_montanias(2*L, 0, H)
        return res


