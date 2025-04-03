MOD = 10**9 + 7

# Función recursiva para calcular el número de montañas rusas
def count_mountains(L, H, memo):
    # Caso base: Si no hay tramos, solo hay una forma de estar a nivel 0 y con altura máxima 0
    if L == 0:
        return 1 if H == 0 else 0
    
    # Verificar si ya hemos calculado este subproblema
    if (L, H) in memo:
        return memo[(L, H)]
    
    # Caso en que la montaña finaliza en altura 0 (el último tramo es descendente)
    result = count_mountains(L - 1, H, memo)
    
    # Caso en que la montaña finaliza en una altura máxima mayor a 0
    if H > 0:
        result = (result + count_mountains(L - 1, H - 1, memo)) % MOD
        result = (result + count_mountains(L - 1, H, memo)) % MOD
    
    # Guardamos el resultado para evitar recalcularlo
    memo[(L, H)] = result
    return result

# Función para procesar varias consultas
def process_queries(queries):
    memo = {}  # Diccionario para almacenar los resultados ya calculados
    for (L, H) in queries:
        print(count_mountains(L, H, memo))

# Ejemplo de uso con consultas (L, H)
queries = [(2, 1), (3, 2), (4, 3)]
process_queries(queries)

