#main.py

import cProfile
import pstats
import io
import sol_dac
import sol_dp
import random

def generar_pares(opcion):
    pares = []
    lista = []

    if opcion == 1:
        for i in range(2, 32):
            L = random.randint(10, 50)
            H = random.randint(10, L)
            lista.append([L, H])
    elif opcion == 2:
        for i in range(2, 32):
            L = random.randint(100, 200)
            H = random.randint(100, L)
            lista.append([L, H])

    for i in range(1, len(lista) + 1):
        pares.append(lista[:i])

    return pares

def profile_function(func, *args):
    pr = cProfile.Profile()
    pr.enable()
    result = func(*args)
    pr.disable()

    stats_stream = io.StringIO()
    ps = pstats.Stats(pr, stream=stats_stream).sort_stats("cumulative")
    stats = ps.stats

    print("\nFuncion | Llamadas | Tiempo Total | Tiempo por Llamada | Tiempo Acumulado | Tiempo por Llamada Acumulado")
    print("-" * 110)

    for func_stat, (cc, nc, tt, ct, callers) in sorted(stats.items(), key=lambda x: x[1][3], reverse=True)[:10]:
        filename, lineno, funcname = func_stat
        print(f"{funcname:<30} {nc:>9} {tt:>14.6f} {tt/nc if nc else 0:>22.6f} {ct:>19.6f} {ct/nc if nc else 0:>32.6f}")

    return result

def procesar_con_dac(lista):
    resultados = []
    for (L, H) in lista:
        resultado = sol_dac.calc_montanias([(L, H)])
        print(f"Par ({L}, {H}) -> Resultado: {resultado}")
        resultados.append(resultado)
    return resultados

def procesar_con_dp(lista):
    resultados = []
    for (L, H) in lista:
        resultado = sol_dp.resultado_montanias([(L, H)])[0]
        print(f"Par ({L}, {H}) -> Resultado: {resultado}")
        resultados.append(resultado)
    return resultados

def menu():
    while True:
        print("\nMenu:")
        print("1. Probar con pares 'pequeños' (L entre 10 y 50)")
        print("2. Probar con pares 'grandes' (L entre 100 y 200)")
        print("3. Par pesonalizado")
        print("4. Salir")

        choice = input("Elige una opción: ")

        if choice == '1' or choice == '2':
            pares_prueba = generar_pares(int(choice))
            print(f"Generando 30 listas de prueba con {len(pares_prueba)} listas de pares...")

            resultados_dac = []
            resultados_dp = []

            while True:
                print("\nElige una solución para procesar los pares:")
                print("1. Divide and Conquer")
                print("2. Programación Dinámica Bottom-Up")
                print("3. Comparar Resultados")
                print("4. Salir")

                solucion_choice = input("Elige una opción: ")

                if solucion_choice == '1':
                    resultados_dac.clear()
                    for idx, lista in enumerate(pares_prueba, 1):
                        print(f"\nProcesando lista {idx} con {len(lista)} pares:")
                        res = profile_function(procesar_con_dac, lista)
                        resultados_dac.append(res)

                elif solucion_choice == '2':
                    resultados_dp.clear()
                    for idx, lista in enumerate(pares_prueba, 1):
                        print(f"\nProcesando lista {idx} con {len(lista)} pares:")
                        res = profile_function(procesar_con_dp, lista)
                        resultados_dp.append(res)

                elif solucion_choice == '3':
                    if not resultados_dac or not resultados_dp:
                        print("Primero debes ejecutar ambas soluciones (DaC y DP) para poder comparar.")
                    else:
                        print("\nComparando resultados:")
                        for idx, (r1, r2) in enumerate(zip(resultados_dac, resultados_dp), 1):
                            iguales = r1 == r2
                            estado = "IGUALES" if iguales else "DIFERENTES"
                            print(f"Lista {idx}: {estado}")

                elif solucion_choice == '4':
                    break

                else:
                    print("Opción no válida. Intenta de nuevo.")

        elif choice == '3':
            L = int(input("Escriba la longitud de la montania rusa: "))
            H = int(input("Escriba la altura maxima para la montania rusa: "))
            print("\nSolución con DaC:")
            profile_function(procesar_con_dac, [(L, H)])

            print("\nSolución con DP:")
            profile_function(procesar_con_dp, [(L, H)])

        elif choice == '4':
            print("Saliendo del programa...")
            break

        else:
            print("Opción no válida. Intenta de nuevo.")

menu()
