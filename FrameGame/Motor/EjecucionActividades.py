from Personaje_ import Personaje
from Plataforma_ import Plataforma
import time

def ejecutarAccionesColisionesDetectadas(personajes, tablaColisiones):
    #adyacencia(personajes, tablaColisiones)
    for personaje in personajes:
        lista_objetos = tablaColisiones[personaje.id]
        xGanancia = 0
        yGanancia = 0
        ladoAbajo = False
        ladoIzquierdo = False
        for objeto in lista_objetos:
            if isinstance(objeto[0], Personaje):
                pass
            if isinstance(objeto[0], Plataforma):#traspasando la ganancia en caso de la plataforma
                plataforma = objeto[0]
                lado = objeto[1]
                if lado == 0:
                    ladoAbajo = True
                    xGanancia+= plataforma.getGananciaXY()[0]
                    yGanancia+= plataforma.getGananciaXY()[1]

                if lado == 1:#izquierda
                    ladoIzquierdo = True
                    if plataforma.getGananciaXY()[0] > 0:
                        xGanancia += plataforma.getGananciaXY()[0]
                """
                if lado == 3:#derecha
                    if personaje.getCaminar() and personaje.getSentido():
                        personaje.setCaminar(False)

                    if plataforma.getGananciaXY()[0] < 0:
                        xGanancia += plataforma.getGananciaXY()[0]
                """

        if len(lista_objetos) > 0:
            personaje.setGananciaXY((xGanancia, yGanancia))

        if ladoAbajo == False:
            personaje.setCaminar(False)
            personaje.setCorrer(False)

        if ladoIzquierdo == True and ladoAbajo == False:
            personaje.setCaminar(False)
            personaje.setCorrer(False)
            angulo = round(personaje.status["angulo"])
            print "AF: ",angulo
            print "float: %.20f"%personaje.status["angulo"]
            print type(angulo)
            print " 90: ", angulo != 90
            print "-90: ", angulo != -90
            if angulo != 90 and  angulo != -90:
                print "AD: ", angulo
                personaje.setSalto(True)
                personaje.status["parabola"] = (60, 45)
                personaje.reseteo()


        if ladoIzquierdo == True and ladoAbajo == True:
            if personaje.getSentido() == False:
                personaje.setCaminar(False)
        
        """
        if ladoIzquierdo == True:
            if personaje.getSalto():
                print personaje.status["angulo"]
                #angulo = personaje.status["angulo"]
                #if (personaje.status["angulo"]>90 and personaje.status["angulo"]<270) or (personaje.status["angulo"]<-90 and personaje.status["angulo"]>-270):
                #    personaje.setSalto(False)
            if personaje.getCaminar() and personaje.getSentido() == False:
                personaje.setCaminar(False)

        if ladoAbajo == False and ladoIzquierdo == True:
            if personaje.getSalto() == True:
                angulo = personaje.status["angulo"]
                saltoIzquierda = (angulo>90 and angulo<270) or (angulo<-90 and angulo>-270)
                if saltoIzquierda == True:
                    veloy = personaje.status["velocidad y"]
                    if veloy > 0:
                        personaje.status["angulo"] = 90
                    else:
                        personaje.status["angulo"] = -90
        """



def adyacencia(personajes, tablaColisiones):
    for personaje in personajes:
        personaje.ady_down = recursion(personaje, tablaColisiones, 0)
        personaje.ady_left = recursion(personaje, tablaColisiones,1)
        personaje.ady_up = recursion(personaje, tablaColisiones,2)
        personaje.ady_right = recursion(personaje, tablaColisiones,3)


def recursion(personaje, tablaColisiones, lado):
    lista_objetos = tablaColisiones[personaje.id]
    for objeto in lista_objetos:
        if objeto[1] == lado:
            #print str(personaje.id)
            #print len(lista_objetos), " ============== ", objeto[1]
            if isinstance(objeto[0], Plataforma):
                return True
            else:
                return recursion(objeto[0], tablaColisiones, lado)
    return False

def ejecutarScripts(diccionarioScripts, diccionarioPersonajes, diccionarioPlataformas):
    for clave, funciones in diccionarioScripts.items():
        for funcion in funciones:
            if diccionarioPersonajes.has_key(clave):
                personaje = diccionarioPersonajes[clave]
                funcion(personaje)
            if diccionarioPlataformas.has_key(clave):
                plataforma = diccionarioPlataformas[clave]
                funcion(plataforma)

def ejecutarActividadesPlataformas(conjuntoPlataformas):
    for p in conjuntoPlataformas:
        p.estado()
        p.actualizacionRec()


def ejecutarActividadesPersonajes(conjuntoPersonajes):
    for p in conjuntoPersonajes:
        p.saltando()
        p.corriendo()
        p.caminando()
        p.runGanancia2()
        p.actualizacionRec()

def ejecutarSonidos(tablaSonidos):
    pass