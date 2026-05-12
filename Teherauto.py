from Auto import Auto #ezzel hívjuk meg a szülő osztályt

class Teherauto(Auto):
    def __init__(self, id, tipus, rendszam, napidij, extra, meret):
        super().__init__(id, tipus, rendszam, napidij)#Superrel a szülő osztályból hivatkozok
        self._extra = extra
        self._meret = meret #Csak a teherautónál van ez a paraméter

    @property
    def extra(self):
        return self._extra

    @property
    def meret(self):
        return self._meret

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
            print("\n \033[31mAz autó nincs kibérelve! \033[0m")
