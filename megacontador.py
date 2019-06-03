import threading
import random
import time

superLista = []
for n in range (1000):
    superLista.append(n)

print ("resultado deberia ser: ", (999*1000)/2)

class SuperContador(threading.Thread):
    def __init__(self, inicio, fin, lista):
        super().__init__()
        self.inicio = inicio
        self.fin = fin
        self.lista = lista
        self.total = 0
    
    def dameTotal(self):
        return self.total

    def run(self):
        for n in range(self.inicio, self.fin+1): 
            self.total += self.lista[n]
            time.sleep(1.0/100.0)


procesos = []
procesos.append( SuperContador(0,199, superLista))
procesos.append( SuperContador(200,399, superLista))
procesos.append( SuperContador(400,599, superLista))
procesos.append( SuperContador(600,799, superLista))
procesos.append( SuperContador(800,999, superLista))

for proceso in procesos:
    proceso.start()

resultado = 0
for proceso in procesos:
    proceso.join()
    resultado += proceso.dameTotal()

print ("el resultado es: " , resultado)