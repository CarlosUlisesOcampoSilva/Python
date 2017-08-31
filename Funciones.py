#Calculo de areas
F=3.141516
#Área del cuadrado
def acuadrado():
    
    lado=input("Cual es el valor del lado")
    x=lado**2
    print("\nEl area del cuadrado es",x,"Unidades cuadradas")
    
#Area del Triangulo
def atriangulo():
    
    base=input("Cual es el valor de la base?")
    altura=input("Cual es el valor de la altura?")
    y=(base * altura)/2
    print("\nEl área del triangulo es:",y,"unidades cuadradas")

#Area del Circulo
def acirculo():
    
    radio=input("Cual es el valor del radio?")
    z=(F*radio)**2
    print("\nEl area del circulo es",z,"unidades cudadras")
    
i=True
while i==True:
    area=input("\nElije la figura geometrica para calcular su area \nCuadrado=1\nTriangulo=2\nCirculo=3\n")
    
    if area===1:
        acuadrado()
    if area==2:
        atriangulo()
    if area==3:
        acirculo()
        
    else:
        print ("ingresa una opcion valida")
    
i=input("\nQuieres calcular el area de otra figura?\nsi=True\nNo=False\n")