class Autokolcsonzo:
    def __init__(self, name):
        self._name = name
        self._autok = []

    @property
    def name(self):
        return self._name

    @property
    def autok(self):
        for auto in self._autok:
            status = "Foglalt" if auto.kiberelt else "Szabad"
            extrak = ", ".join(auto.extra)
            print(f"Azonosító: \033[93m {auto.id}, \033[0m Típus: {auto.tipus}, Rendszám: {auto.rendszam}, Ár: \033[93m {auto.napidij} Ft \033[0m, Extrák: {extrak}, Állapot: {status}")

    @autok.setter
    def autok(self, new_auto):
        self._autok.append(new_auto)

    def autoberles_azonositoval(self, auto_id):
        for auto in self._autok:
            if auto.id == auto_id:
                auto.auto_berles()
                print(f"A bérlés ára: \033[93m {auto.napidij} Ft / nap \033[0m")
                return

        print("\n \033[93m Nincs ilyen azonosítójú autó! \033[0m")

    def auto_lemondas_azonositoval(self, auto_id):
        for auto in self._autok:
            if auto.id == auto_id:
                auto.auto_lemondas()
                print(f"Ha már átutaldad a bérleti díjat, a lemondás miatt visszajár:\033[93m {auto.napidij} Ft \033[0m")
                return

        print("\n \033[93m Nincs ilyen azonosítójú autó! \033[0m")

    def foglalt_autok_listazasa(self):
        van_foglalt = False

        for auto in self._autok:
            if auto.kiberelt:
                van_foglalt = True
                print(f"Azonosító: \033[93m {auto.id} \033[0m, Típus: {auto.tipus}, Rendszám: {auto.rendszam}, Ár: \033[93m {auto.napidij} Ft \033[0m, Extrák: {', '.join(auto.extra)}")

        if not van_foglalt:
            print("\n \033[93m Sajnos nincs kibérelt autónk. \033[0m")