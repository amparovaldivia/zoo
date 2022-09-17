from zoo import Zoo
class Gallina(Zoo):
    def __init__(self,nombre,edad,nivel_salud,nivel_felicidad,color):
        super().__init__(nombre,edad,nivel_salud,nivel_felicidad,color)
        self.color=color