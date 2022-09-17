class Zoo:
    def __init__(self,nombre,edad,nivel_salud,nivel_felicidad):
        self.nombre=nombre
        self.edad=edad
        self.nivel_salud=nivel_salud
        self.nivel_felicidad=nivel_felicidad

    def mostrar_info(self):
        print(self.__dict__)
        return self
        
    def alimentacion (self):
        self.nivel_salud+=10
        self.nivel_felicidad+=10
        return self
        

