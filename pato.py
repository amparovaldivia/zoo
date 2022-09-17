from zoo import Zoo

class Pato(Zoo):
    def __init__(self,nombre,edad,nivel_salud,nivel_felicidad,tamano):
        super().__init__(nombre,edad,nivel_salud,nivel_felicidad)
        self.tamano=tamano
