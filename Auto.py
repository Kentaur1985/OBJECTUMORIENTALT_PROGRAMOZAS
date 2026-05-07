# Absztrakt alaposztály az autókhoz

from abc import ABC, abstractmethod

class Auto(ABC):
    def __init__(self, id, tipus, rendszam, napidij):
        self._id = id
        self._tipus = tipus
        self._rendszam = rendszam
        self._napidij = napidij
        self._kiberelt = False

    @property
    def id(self):
        return self._id

    @property
    def tipus(self):
        return self._tipus

    @property
    def rendszam(self):
        return self._rendszam

    @property
    def napidij(self):
        return self._napidij

    @property
    def kiberelt(self):
        return self._kiberelt

    @abstractmethod
    def auto_berles(self):
        pass

    @abstractmethod
    def auto_lemondas(self):
        pass
