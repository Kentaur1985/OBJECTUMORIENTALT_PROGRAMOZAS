from Berles import Berles #beimportálom a bérlést

class Autokolcsonzo: # itt hozom létre a kölcsönzőt
    def __init__(self, name):
        self._name = name
        self._autok = [] #Ezekbe kerülnek majd a járműpark adatai
        self._berlesek = [] #Ebbe a listába a bérlések adatai

    @property
    def name(self):
        return self._name

    @property
    def autok(self):
        for auto in self._autok:
            berlesek = [b for b in self._berlesek if b.auto_id == auto.id] #A bérlések metódusa
            if berlesek:
                foglalt_datumok = ", ".join([b.datum for b in berlesek])
                status = f"Foglalt ekkor: {foglalt_datumok}"
            else:
                status = "Szabad"
            extrak = ", ".join(auto.extra)
            if hasattr(auto, "meret"): #Ez egy beépített algoritmus
                print(f"Azonosító: \033[93m {auto.id}, \033[0m Típus: {auto.tipus}, Rendszám: {auto.rendszam}, Ár: \033[93m {auto.napidij} Ft \033[0m, Teherbírás: \033[93m {auto.meret} kg \033[0m, Extrák: {extrak}, Állapot: {status}")
            else:
                print(f"Azonosító: \033[93m {auto.id}, \033[0m Típus: {auto.tipus}, Rendszám: {auto.rendszam}, Ár: \033[93m {auto.napidij} Ft \033[0m, Extrák: {extrak}, Állapot: {status}")

    @autok.setter
    def autok(self, new_auto):
        self._autok.append(new_auto)

    def autoberles_azonositoval(self, auto_id, berlo_neve, datum):
        for auto in self._autok:
            if auto.id == auto_id:
                berles = next((b for b in self._berlesek if b.auto_id == auto_id and b.datum == datum), None)
                if berles:
                    print(f"\033[31m Ez az autó ezen a napon már foglalt: {datum} \033[0m")
                else:
                    self._berlesek.append(Berles(berlo_neve, auto_id, datum))
                    print("\033[93m Sikeres bérlés! \033[0m")
                    print(f"A bérlés ára: \033[93m {auto.napidij} Ft / nap \033[0m")
                return

        print("\n \033[93m Nincs ilyen azonosítójú autó! \033[0m")
    def auto_lemondas_azonositoval(self, auto_id):
        self._berlesek = [berles for berles in self._berlesek if berles.auto_id != auto_id] #Nem egyenlő
        for auto in self._autok:
            if auto.id == auto_id:
                auto.auto_lemondas()
                print(f"Ha már átutaldad a bérleti díjat, a lemondás miatt visszajár:\033[93m {auto.napidij} Ft \033[0m")
                return

        print("\n \033[93m Nincs ilyen azonosítójú autó! \033[0m")

    def foglalt_autok_listazasa(self):
        if not self._berlesek:
            print("\n \033[93m Sajnos nincs lefoglalt autónk. \033[0m")
            return

        for berles in self._berlesek:
            for auto in self._autok:
                if auto.id == berles.auto_id:
                    if hasattr(auto, "meret"):
                        print(f"Azonosító: \033[93m {auto.id} \033[0m, Típus: {auto.tipus}, Rendszám: {auto.rendszam}, Ár: \033[93m {auto.napidij} Ft \033[0m, Teherbírás: \033[93m {auto.meret} kg \033[0m, Extrák: {', '.join(auto.extra)}, Bérlő: {berles.berlo_neve}, Foglalt nap: {berles.datum}")
                    else:
                        print(f"Azonosító: \033[93m {auto.id} \033[0m, Típus: {auto.tipus}, Rendszám: {auto.rendszam}, Ár: \033[93m {auto.napidij} Ft \033[0m, Extrák: {', '.join(auto.extra)}, Bérlő: {berles.berlo_neve}, Foglalt nap: {berles.datum}")