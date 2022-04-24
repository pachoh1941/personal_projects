
class Conversor():

    def __init__(self, magnitud, uns_entrada, uns_salida):
        self.magnitud = magnitud
        self.uns_entrada = uns_entrada #Unidades de entrada
        self.uns_salida = uns_salida #Unidades de salida
        self._unidades = {
            'bar_a_psi':14.5,
            'in_a_mm':1/25.4,
            'gal_a_L':3.78,
            'L_a_m3':0.001
        }

    def convertir(self):
        conversion_solicitada = f'{self.uns_entrada}_a_{self.uns_salida}'
        factor = _unidades.get(conversion_solicitada)

        return self.magnitud * factor


    def agregar_unidad(self, nueva_un_entrada, nueva_un_salida, factor): #permite al usuario agregar una nueva conversión de unidades
        pass