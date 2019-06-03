import random

class Usuario:
    def __init__(self, identificador):
        self.__id = identificador 

    def dameId(self):
        return self.__id

class Servidor:

    def __init__(self, identificador):
        self.__id = identificador

    def run(self, usuario):
        print(id(self), usuario.dameId())

class LB:

    def __init__(self, identificador):
        self.__id = identificador
        self.ultimoLlamado = 0
        self.servidores = []

    def dispatch(self, usuario):
        self.servidores[self.ultimoLlamado].run(usuario)
        self.ultimoLlamado += 1
        if self.ultimoLlamado >= len(self.servidores):
            self.ultimoLlamado = 0


    def agregarServidor(self, servidor):
        self.servidores.append(servidor)

user = Usuario(10)
usuarios = []
usuarios.append(Usuario(10))

for n in range(10):
    usuarios.append(Usuario(n))


lb = LB(1)
lb.agregarServidor(Servidor("servidor 1"))
lb.agregarServidor(Servidor("servidor 2"))
lb.agregarServidor(Servidor("servidor 3"))
lb.agregarServidor(Servidor("servidor 4"))
lb.agregarServidor(Servidor("servidor 5"))
lb.agregarServidor(Servidor("servidor 6"))
lb.agregarServidor(Servidor("servidor 7"))


llamadas = []
for n in range(1000):
    llamadas.append( usuarios[random.randint(0,9)] )

for usuario in llamadas:
    lb.dispatch(usuario)

# print(lb.servidores)