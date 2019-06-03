import threading
import time
import random

class Test(threading.Thread):
    def __init__(self, nombre):
        super().__init__()
        self.nombre = nombre
    
    def run(self):
        time.sleep(random.randint(0,3))
        print("Termino", self.nombre)

hilos = []
for n in range(10):
    tmp = Test(n)
    tmp.start()
    hilos.append(tmp)


for hilo in hilos:
    hilo.join()

print("termine?")