from os import system


def seleccionar_por_arranque():
    #funcion que selecciona tanque por tiempo de arranque de compresor
    #asume los parámetros que no son ingresados en el array de especs
    pass

def seleccionar_por_vaciado():
    #funciona que selecciona tanque por tiempo de vaciado
    #asume los parámetros que no son ingresados en el array de especs
    pass

def seleccionar_por_llenado():
    #funciona que selecciona tanque por tiempo de llenado
    #asume los parámetros que no son ingresados en el array de especs
    pass

def seleccionar_tanque(especificaciones, criterio):
    #funcion que gestiona la selección según un diccionario de especificaciones y un criterio
    #se debe deifnir un orden del array (puede ser según cuaderno)
    pass

if __name__== '__main__':

    #Total de especficaciones posibles; inicializador
    especificaciones_totales = {
        'Caída de presión máxima permitida (psig)': 0,
        'Presión atmosférica (psig)': 14.7,
        'Volumen tanque (Gal)': 0,
        'Tiempo de arranque (s)': 0,
        'Tiempo de llenado (s)': 0,
        'Tiempo de vaciado (s)': 0,
        'Presión inicial (psig)': 0,
        'Presión final (psig)': 0,
        'Caudal (CFM)': 0,
    }

    #Escoger las especificaciones según lo que el usuario tenga
    especificaciones = {}
    for spec, valor in especificaciones_totales.items():
        try:
            input_usuario = float(input(f'Por favor ingresar {spec}: '))
            #En el fututo incluir el conversor de unidades
        except: #Si el usuario no ingresa nada
            print(f'No has ingresado ningún valor para {spec}.')
            continue

        valor = input_usuario
        especificaciones.update({spec: valor})
        print(f'Has ingresado el valor {valor} a {spec}.')

    system('cls')
    print('Harás una selección con las siguientes especificaciones:')
    for spec, valor in especificaciones.items():
        print(f'{spec}: {valor}')

    # criterio = int(input('¿Bajo qué criterio seleccionarás el tanque? A, B o C'))

    # seleccionar_tanque(especificaciones, criterio)