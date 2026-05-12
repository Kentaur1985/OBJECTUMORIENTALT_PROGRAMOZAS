# Absztrakt alaposztály az autókhoz

from abc import ABC, abstractmethod

class Auto(ABC):
    def __init__(self, id: int, tipus: str, rendszam: str, napidij: int):#Az autók közös szülő változói
        self._id = id
        self._tipus = tipus
        self._rendszam = rendszam
        self._napidij = napidij
        self._kiberelt = False

    @property #az azonosítót ezzel hívjuk meg
    def id(self):
        return self._id

    @property #a típust ezzel hívjuk meg
    def tipus(self):
        return self._tipus

    @property
    def rendszam(self):
        return self._rendszam

    @property
    def napidij(self):
        return self._napidij

    @property# a státuszát ezzel hívjuk meg
    def kiberelt(self):
        return self._kiberelt

    @abstractmethod #ezek üresek itt, csak deklaráltam
    def auto_berles(self):
        pass

    @abstractmethod #ezek üresek itt, csak deklaráltam
    def auto_lemondas(self):
        pass
