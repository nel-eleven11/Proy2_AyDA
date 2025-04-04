#main.py

import time
import sol_dac
import sol_dp
import random

#Se genera el conjunto de datos de prueba
import random

def generar_pares(opcion):
    pares = []
    lista = []

    if opcion == 1:
        # Pares pequeños (L entre 10 y 50)
        for i in range(2, 32):
            L = random.randint(10, 50)
            H = random.randint(10, L)
            lista.append([L, H])

    elif opcion == 2:
        # Pares grandes (L entre 100 y 200)
        for i in range(2, 32):
            L = random.randint(100, 200)
            H = random.randint(100, L)
            lista.append([L, H])

    for i in range(1, len(lista) + 1):
        pares.append(lista[:i])

    return pares


def menu():
    while True:
        print("\nMenu:")
        print("1. Probar con pares 'pequeños' (L entre 10 y 50)")
        print("2. Probar con pares 'grandes' (L entre 100 y 200)")
        print("3. Par pesonalizado")
        print("4. Salir")

        choice = input("Elige una opción: ")

        if choice == '1' or choice == '2':
            # Generar pares según la opción seleccionada
            pares_prueba = generar_pares(int(choice))
            print(f"Generando 30 listas de prueba con {len(pares_prueba)} listas de pares...")

            # Elegir solución a usar
            while True:
                print("\nElige una solución para procesar los pares:")
                print("1. Divide and Conquer")
                print("2. Programación Dinámica Bottom-Up")
                print("3. Salir")

                solucion_choice = input("Elige una opción: ")

                if solucion_choice == '1':
                    # Probar las listas una por una con Divide and Conquer
                    for idx, lista in enumerate(pares_prueba, 1):
                        print(f"\nProcesando lista {idx} con {len(lista)} pares:")

                        dicc = {}

                        total_start_time = time.time()

                        for (L, H) in lista:
                            resultado = sol_dac.calc_montanias([(L, H)])
                            print(f"Par ({L}, {H}) -> Resultado: {resultado}")

                        total_end_time = time.time()
                        total_execution_time = total_end_time - total_start_time

                        print(f"Tiempo total de ejecución para la lista {idx}: {total_execution_time:.6f} segundos")

                elif solucion_choice == '2':
                    # Probar las listas una por una con Programación Dinámica Bottom-Up
                    for idx, lista in enumerate(pares_prueba, 1):
                        print(f"\nProcesando lista {idx} con {len(lista)} pares:")

                        total_start_time = time.time()

                        for (L, H) in lista:
                            resultado = sol_dp.resultado_montanias([(L, H)])[0]

                            print(f"Par ({L}, {H}) -> Resultado: {resultado}")

                        total_end_time = time.time()
                        total_execution_time = total_end_time - total_start_time

                        print(f"Tiempo total de ejecución para la lista {idx}: {total_execution_time:.6f} segundos")

                elif solucion_choice == '3':
                    break  # Salir a la opción anterior

                else:
                    print("Opción no válida. Intenta de nuevo.")

        elif choice == '3':

            L = int(input("Escriba la longitud de la montania rusa: "))
            H = int(input("Escriba la altura maxima para la montania rusa: "))
            print("\n")

            print("Solución con DaC: ")

            dicc = {}

            total_start_time = time.time()

            resultado = sol_dac.calc_montanias([(L, H)])
            print(f"Par ({L}, {H}) -> Resultado: {resultado}")

            total_end_time = time.time()
            total_execution_time = total_end_time - total_start_time

            print(f"Tiempo total de ejecución: {total_execution_time:.6f} segundos")

            print("\n")

            print("Solución con DP: ")

            total_start_time = time.time()

            resultado = sol_dp.resultado_montanias([(L, H)])[0]

            print(f"Par ({L}, {H}) -> Resultado: {resultado}")

            total_end_time = time.time()
            total_execution_time = total_end_time - total_start_time

            print(f"Tiempo total de ejecución: {total_execution_time:.6f} segundos")



        elif choice == '4':
            print("Saliendo del programa...")
            break  # Salir del programa

        else:
            print("Opción no válida. Intenta de nuevo.")

menu()
