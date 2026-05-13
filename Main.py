from Autokolcsonzo import Autokolcsonzo
from Szemelyauto import Szemelyauto
from Teherauto import Teherauto
from Berles import Berles

class BerlesRendszer:
    def __init__(self):
        self._kolcsonzo = Autokolcsonzo("S.O.S Kell egy Kocsi BT") #A cég neve
        self._init_data()

    def _init_data(self): #A gépjárműpark
        self._kolcsonzo.autok = Szemelyauto(1, "Suzuki Swift", "AA-BER-012",30000, ["Klíma", "Tempomat", "GPS"])
        self._kolcsonzo.autok = Szemelyauto(2, "Suzuki - Swift", "AE-FER-345", 30000, ["Klíma", "Tempomat", "GPS"])
        self._kolcsonzo.autok = Szemelyauto(3, "Suzuki - Vitara", "AE-KOT-023", 35000, ["Klíma", "Tempomat", "GPS", "Vonóhorog"])
        self._kolcsonzo.autok = Szemelyauto(4, "Suzuki - Vitara", "BB-FDC-034", 35000, ["Klíma", "Tempomat", "GPS", "Vonóhorog"])
        self._kolcsonzo.autok = Teherauto(101, "Ford - Transporter", "AA-ZHT-245", 50000, ["Klíma", "Tempomat", "Vonóhorog"], 1500)
        self._kolcsonzo.autok = Teherauto(102, "Ford - Transporter", "AA-HGG-534", 50000, ["Klíma", "Tempomat", "Vonóhorog"],1500)
        self._kolcsonzo.autok = Teherauto(103, "Mercedes - Sprinter", "AA-POL-768", 55000, ["Klíma", "Tempomat", "GPS", "Vonóhorog"], 2500)
        self._kolcsonzo.autok = Teherauto(104, "Mercedes - Sprinter", "AA-KGD-733", 55000, ["Klíma", "Tempomat", "GPS", "Vonóhorog"], 2500)

# 4 autót alapból kikölcsönöztek, de ez nem lenne része a programomnak.
        self._kolcsonzo._berlesek.append(Berles("Kiss Béla", 1, "2026-09-01"))
        self._kolcsonzo._berlesek.append(Berles("Nagy Béla", 2, "2026-10-01"))
        self._kolcsonzo._berlesek.append(Berles("Hosszú Csaba", 101, "2026-11-01"))
        self._kolcsonzo._berlesek.append(Berles("Szabó Dóra", 103, "2026-12-01"))

    def user_interact(self):# A fontos dolgokat sárgával a hiba üziket pirossal íratom ki, a végén mindig visszaváltok fehérre
        print(f"\n\033[93m Üdvözöl a {self._kolcsonzo.name} autókölcsönző! \033[0m \n") #Köszöntő szöveg
        print("Ha szükséged van egy autóra, vagy egy teherautóra egy napra, akkor jó helyen jársz!")
        while True: #A főmenü
            print("\n1. Az összes autónk listája")
            print("2. Autó bérlése")
            print("3. Bérlés lemondása")
            print("4. Kibérelt autók listázása")
            print("5. Kilépés")

            try: #try, mert kell kivételt kezelni
                menu = int(input("\n\033[93m Válassz mit szeretnél: \033[0m"))
                if menu == 1:
                    self._kolcsonzo.autok # listázás
                elif menu == 2: #bérlés
                    try:
                        auto_id = int(input(" \n\033[93m Add meg az autó azonosítóját: (pl. 1, 2, 101, 102): \n\033[0m "))
                        berlo_neve = input("\033[93m Add meg a bérlő nevét: \033[0m")
                        datum = input("\033[93m Add meg a bérlés dátumát: pl. 2026-09-01 \033[0m")
                        self._kolcsonzo.autoberles_azonositoval(auto_id, berlo_neve, datum)
                    except ValueError:
                        print("\n\033[93m Hiba! Csak számot adhatsz meg az azonosítóhoz! \033[0m") #hibakezelés
                elif menu == 3:
                    try:
                        auto_id = int(input("\n\033[93m Add meg az autó azonosítóját: (pl. 1, 2, 101, 102): \n\033[0m"))
                        berlo_neve = input("\033[93m Add meg a bérlő nevét: \033[0m")
                        datum = input("\033[93m Add meg a bérlés dátumát: pl. 2026-09-01 \033[0m")
                        self._kolcsonzo.auto_lemondas_azonositoval(auto_id, berlo_neve, datum)
                    except ValueError:
                        print("\n\033[31m Hiba! Csak számot adhatsz meg az azonosítóhoz! \033[0m")
                        print("\n\033[31m Hiba! Csak számot adhatsz meg az azonosítóhoz! \033[0m")
                elif menu == 4:# A foglalt autók listázása
                    print("\n Ezek az autóink foglaltak")
                    self._kolcsonzo.foglalt_autok_listazasa()
                elif menu == 5:#kilépés a programból
                    print("Viszont látásra!")
                    break
                else:# hibakezelések
                    print("\n\033[31m Nincs ilyen menüpontunk!\033[0m")
            except ValueError:
                print("\n \033[31m Hiba! A menüpont csak szám lehet! (1-5)\033[0m")
            except Exception as e:
                print(f"\n \033[31m Valami hibát észleltünk, lépj be újra: {e} \033[0m")

berles_rendszer = BerlesRendszer()
berles_rendszer.user_interact()
