from Auto import Auto

class Szemelyauto(Auto):
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
            print("\033[31m Ezt az autót már kibérelték! \033[0m")

    def auto_lemondas(self):
        if self._kiberelt:
            self._kiberelt = False
            print("\n \033[93m Sikeres lemondás! \033[0m")
        else:
            print("\n \033[93m Az autó nincs kibérelve! \033[0m")
