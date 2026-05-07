from Auto import Auto

class Teherauto(Auto):
    def __init__(self, id, tipus, rendszam, napidij, extra):
        super().__init__(id, tipus, rendszam, napidij)
        self._extra = extra

    @property
    def extra(self):
        return self._extra

    def auto_berles(self):
        if not self._kiberelt:
            self._kiberelt = True
            print("\033[93m Sikeres bérlés! \033[0m")
        else:
            print("Ezt az autót már kibérelték!")

    def auto_lemondas(self):
        if self._kiberelt:
            self._kiberelt = False
            print("Sikeres lemondás!")
        else:
            print("Az autó nincs kibérelve!")
