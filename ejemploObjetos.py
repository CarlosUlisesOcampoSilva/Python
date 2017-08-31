class Persona:
    
    def __init__(self):
        
        self.edad=18
        self.nombre="juan"
        print("Se ha creado a",self.nombre,"de",self.edad)
    #Metodo nuevo "hablar"
    def hablar(self, palabras):
       print(self.nombre,':',palabras)
        
juan=Persona()
juan.hablar("Hola, estoy hablando")
