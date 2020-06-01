import random 
from ajncError import ajncError

class ajnc(self):
    def __init__(self):
        self.bodovi_korisnik = ''
        self.bodovi_racunalo = ''
        

    def display_title_bar(self):
		print("~Ajnc~")
		
    def get_user_choice(self):
        print("\n[1] Igraj Ajnc.")
        print("[x] Izlaz.")
         
        return input ("Birajte [1] za ulazak u igru ili [x] za Izlaz. ")
   
    def vuci_stop(self):
        print("\n[1] Vuci.")
        print("[2] Stop.")

    def play(self):
        while (self.get_user_choice != 'x'):
			self.bodovi_korisnik = 0
			self.bodovi_racunalo = 0
            
        if self.vuci_stop == 1:
                self.korisnik = random.choice(0,2,3,4,5,6,7,8,9,'kec','decko','dama','kralj')
                self.bodovi_korisnik += random.randint
                self.racunalo = random.choice(0,2,3,4,5,6,7,8,9,'kec','decko','dama','kralj')
                self.bodovi_racunalo += random.randint

                if self.bodovi_korisnik == 21:
                    print("Pobjednik igre je Korisnik!")
                elif self.bodovi_racunalo == 21:
                    print("Pobjednik igre je Računalo!")
	 
                print("Korisnik ima {} bod/ova".format(self.bodovi_korisnik.title()))
                print("Računalo {} bod/ova".format(self.bodovi_racunalo.title()))

                self.display_title_bar()

                print("Hvala na poštenoj igri! Pozdrav!")
        
if __name__ == "__main__":
    game = ajnc()
    game.play()

