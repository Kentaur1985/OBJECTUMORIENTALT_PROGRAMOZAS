from Autokolcsonzo import Autokolcsonzo
from Szemelyauto import Szemelyauto
from Teherauto import Teherauto

class BerlesRendszer:
    def __init__(self):
        self._kolcsonzo = Autokolcsonzo("S.O.S Kell egy Kocsi BT")
        self._init_data()

    def _init_data(self):
        self._kolcsonzo.autok = Szemelyauto(1, "Suzuki Swift", "AA-BER-012",30000, ["Klíma", "Tempomat", "GPS"])
        self._kolcsonzo.autok = Szemelyauto(2, "Suzuki - Swift", "AE-FER-345", 30000, ["Klíma", "Tempomat", "GPS"])
        self._kolcsonzo.autok = Szemelyauto(3, "Suzuki - Vitara", "AE-KOT-023", 35000, ["Klíma", "Tempomat", "GPS", "Vonóhorog"])
        self._kolcsonzo.autok = Szemelyauto(4, "Suzuki - Vitara", "BB-FDC-034", 35000, ["Klíma", "Tempomat", "GPS", "Vonóhorog"])
        self._kolcsonzo.autok = Teherauto(101, "Ford - Transporter", "AA-ZHT-245", 50000, ["Klíma", "Tempomat", "Vonóhorog"])
        self._kolcsonzo.autok = Teherauto(102, "Ford - Transporter", "AA-HGG-534", 50000, ["Klíma", "Tempomat", "Vonóhorog"])
        self._kolcsonzo.autok = Teherauto(103, "Mercedes - Sprinter", "AA-POL-768", 55000, ["Klíma", "Tempomat", "GPS", "Vonóhorog"])
        self._kolcsonzo.autok = Teherauto(104, "Mercedes - Sprinter", "AA-KGD-733", 55000, ["Klíma", "Tempomat", "GPS", "Vonóhorog"])

# A feladat alapján már 4 autót alapból kikölcsönöztek, de ez nem lenne része a programomnak.
        self._kolcsonzo._autok[0]._kiberelt = True
        self._kolcsonzo._autok[1]._kiberelt = True
        self._kolcsonzo._autok[4]._kiberelt = True
        self._kolcsonzo._autok[6]._kiberelt = True

    def user_interact(self):
        print(f"\nÜdvözöl a(z) {self._kolcsonzo.name} autókölcsönző!\n")
        print("Ha szükséged van egy autóra, vagy egy teherautóra egy napra, akkor jó helyen jársz!")
        while True:
            print("\n1. Az összes autónk listája")
            print("2. Autó bérlése")
            print("3. Bérlés lemondása")
            print("4. Kibérelt autók listázása")
            print("5. Kilépés")

            try:
                menu = int(input("Válassz mit szeretnél: "))

                if menu == 1:
                    self._kolcsonzo.autok

                elif menu == 2:
                    try:
                        auto_id = int(input("Add meg az autó azonosítóját: (pl. 1, 2, 101, 102): "))
                        self._kolcsonzo.autoberles_azonositoval(auto_id)
                    except ValueError:
                        print("Hiba! Csak számot adhatsz meg az azonosítóhoz! (pl. 1, 2, 101, 102)")

                elif menu == 3:
                    try:
                        auto_id = int(input("Add meg az autó azonosítóját: (pl. 1, 2, 101, 102): "))
                        self._kolcsonzo.auto_lemondas_azonositoval(auto_id)
                    except ValueError:
                        print("Hiba! Csak számot adhatsz meg az azonosítóhoz! (pl. 1, 2, 101, 102)")

                elif menu == 4:
                    print("\nEzek az autóink foglaltak mára")
                    self._kolcsonzo.foglalt_autok_listazasa()

                elif menu == 5:
                    print("Kilépés...")
                    break

                else:
                    print("Nincs ilyen menüpontunk!")

            except ValueError:
                print("Hiba! A menüpont csak szám lehet! (1-4)")

            except Exception as e:
                print(f"Valami hibát észleltünk, lépj be újra: {e}")




berles_rendszer = BerlesRendszer()
berles_rendszer.user_interact()
