from zoo import Zoo
class Elefante(Zoo):
    def __init__(self,nombre,edad,nivel_salud,nivel_felicidad,comida):
        super().__init__(nombre,edad,nivel_salud,nivel_felicidad,comida)
        self.comida=comida
