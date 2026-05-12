from abc import ABC, abstractmethod

class Berles: #A bérlés metódusa
    def __init__(self, berlo_neve, auto_id, datum):
        self._berlo_neve = berlo_neve
        self._auto_id = auto_id
        self._datum = datum

    @property
    def berlo_neve(self):
        return self._berlo_neve

    @property
    def auto_id(self):
        return self._auto_id

    @property
    def datum(self):
        return self._datum