import random


class Repositorio:
    def __init__(self):
        pass

    def falta_palabra(self):
        palabras = ['labial', 'collar', 'medico', 'gorila', 'tomate', ]
        tipos = ['Maquillaje', 'Accesorios', 'Profesion', 'Animal', 'Verdura']

        indice = random.randrange(0, 4)

        return {'palabra': palabras[indice], 'tipo_palabra': tipos[indice]}
