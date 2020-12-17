from ciberpolicia import Ciberpolicia
from coordinadorpatrulla import CoordinadorPatrulla

class Patrulla():

    def __init__(self, npatrulla, cpatrulla, cpolicias):

        if len(cpolicias) < 4:
            raise ValueError("El número de policías debe >= 4")
        self.coordinadorpatrulla = cpatrulla
        self.ciberpolicias = cpolicias
        self.npatrulla = npatrulla

    @property
    def coordinadorPatrulla(self):
        return self.__coordinadorpatrulla

    @property
    def ciberpolicias(self):
        return self.__ciberpolicias

    @property
    def npatrulla(self):
        return self.__npatrulla

    @coordinadorPatrulla.setter
    def coordinadorPatrulla(self, cpatrulla):
        self.__coordinadorpatrulla = cpatrulla

    @ciberpolicias.setter
    def ciberpolicias(self, cpolicias):
        self.__ciberpolicias = cpolicias

    @npatrulla.setter
    def npatrulla(self, npatrulla):
        self.__npatrulla = npatrulla

    def addCiberpolicia(self, cpolicia):
        self.__ciberpolicias.append(cpolicia)