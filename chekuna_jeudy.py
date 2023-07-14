# -*- coding: utf-8 -*-
"""chekuna jeudy.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/10XntUVDHm-iKa3MOovdF31FZrvjRgnkU
"""

import datetime

# Precios de los departamentos a vender
precios_venta = {
    'A': 3800,
    'B': 3000,
    'C': 2800,
    'D': 3500
}

# Estado de los departamentos
estado_departamentos = [['D'] * 4 for _ in range(10)]  # 'D' representa disponible

# Compradores
compradores = []

# Función para validar el RUN
def validar_run(run):
    try:
        run = run.replace('.', '').replace('-', '').upper()
        run_digits = run[:-1]
        return run_digits.isdigit()
    except ValueError:
        return False


# Función para mostrar el estado actual de los departamentos
def mostrar_estado_departamentos():
    for piso, departamentos in enumerate(estado_departamentos, start=1):
        print(f'Piso {piso}:', end=' ')
        for estado in departamentos:
            if estado == 'V':
                print('X', end=' ')
            else:
                print('D', end=' ')
        print()


# Función para comprar un departamento
def comprar_departamento():
    piso = input('Ingrese el número de piso (1-10): ')
    tipo_departamento = input('Ingrese el tipo de departamento (A-D): ')

    if tipo_departamento.upper() not in precios_venta or int(piso) not in range(1, 11):
        print('Error: Departamento inválido.')
        return

    if estado_departamentos[int(piso) - 1][ord(tipo_departamento.upper()) - 65] != 'D':
        print('Error: Departamento no está disponible.')
        return

    estado_departamentos[int(piso) - 1][ord(tipo_departamento.upper()) - 65] = 'V'
    precio = precios_venta[tipo_departamento.upper()]

    run = input('Ingrese el RUN del comprador (sin guiones ni puntos): ')
    if not validar_run(run):
        print('Error: RUN inválido.')
        return

    departamento = tipo_departamento.upper() + piso
    compradores.append((run, departamento))

    print('Operación de compra realizada correctamente.')
    print(f'El departamento {departamento} con RUN {run} ha sido registrado.')


# Función para mostrar el listado de compradores
def mostrar_listado_compradores():
    compradores_ordenados = sorted(compradores, key=lambda x: int(''.join(filter(str.isdigit, x[0]))))
    print('Listado de compradores:')
    for comprador in compradores_ordenados:
        print(f'RUN: {comprador[0]}, Departamento: {comprador[1]}')


# Función para calcular las ganancias totales
def mostrar_ganancias_totales():
    ganancias_ventas = {tipo: 0 for tipo in precios_venta}
    cantidad_ventas = {tipo: 0 for tipo in precios_venta}

    for fila in estado_departamentos:
        for tipo in fila:
            if tipo == 'V':
                tipo_departamento = chr(65 + fila.index(tipo))
                ganancias_ventas[tipo_departamento] += precios_venta.get(tipo_departamento, 0)
                cantidad_ventas[tipo_departamento] += 1

    print('Ganancias totales por ventas:')
    for tipo, ganancia in ganancias_ventas.items():
        print(f'Tipo de departamento {tipo}: {ganancia} UF (Vendidos: {cantidad_ventas[tipo]})')

    total_ventas = sum(ganancias_ventas.values())
    print('\nGanancia total por ventas:', total_ventas, 'UF')


# Función para mostrar información de salida del sistema
def mostrar_salida(nombre, apellido):
    fecha_actual = datetime.date.today().strftime('%d/%m/%Y')
    print(f'\nGracias por usar la aplicación, {nombre} {apellido}!')
    print(f'Salida del sistema: {fecha_actual}')


# Función principal del programa
def main():
    nombre = input('Ingrese su nombre: ')
    apellido = input('Ingrese su apellido: ')

    while True:
        print('\n===== MENÚ =====')
        print('1. Comprar departamento')
        print('2. Mostrar departamentos disponibles')
        print('3. Ver listado de compradores')
        print('4. Mostrar ganancias totales')
        print('5. Salir')
        opcion = input('Ingrese una opción: ')

        if opcion == '1':
            comprar_departamento()
        elif opcion == '2':
            mostrar_estado_departamentos()
        elif opcion == '3':
            mostrar_listado_compradores()
        elif opcion == '4':
            mostrar_ganancias_totales()
        elif opcion == '5':
            mostrar_salida(nombre, apellido)
            break
        else:
            print('Error: Opción inválida.')


# Ejecutar la función principal del programa
main()