class Ventana:
    #Atributos
    __titulo = ''
    __verSupIzqX = 0
    __verSupIzqY  =0
    __verInfDerX = 500
    __verInfDerY =500

    #Metodos
    def __init__(self,titulo='',vsix=0,vsiy=0,vidx=500,vidy=500):
        self.__titulo = titulo
        self.__verSupIzqX = vsix
        self.__verSupIzqY = vsiy
        self.__verInfDerX = vidx
        self.__verInfDerY = vidy
     
    def getTitulo(self):
         return self.__titulo
    def getPatente(self):
        return self.__patente
    def getConductor(self):
        return self.__nombreConductor

    def mostrar(self):
        print('Valor de las Coordenadas x=',self.__verSupIzqX,' e y=',self.__verSupIzqY,' del vértice superior izquierdo: son')
        print('Valor de las Coordenadas x e y del vértice inferior derecho:son',self.__verInfDerX,self.__verInfDerY)

    def alto(self):
        return  (self.__verSupIzqY + self.__verInfDerY)

    def ancho(self):
        return (self.__verSupIzqX + self.__verInfDerX)

    def moverDerecha(self,x):
        xau=self.__verInfDerX+x
        if xau < 500 :
            self.__verInfDerX=xau
            xau=self.__verSupIzqX+x
            self.__verSupIzqX=xau
        else:
            print('Imposible Mover')
            print('=== ++++++++++ ===')

    def subir(self,y):
        yau=self.__verSupIzqY-y
        if ((yau > 0)and(yau<500)) :
            self.__verSupIzqY=yau
            yau=self.__verInfDerY-y
            self.__verInfDerY=yau
        else:
            print('Imposible Mover')
            print('=== ++++++++++ ===')
        
        

