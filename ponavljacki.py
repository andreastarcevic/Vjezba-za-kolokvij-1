import random
from ponavljackiError import ponavljackiError

class Rulet:
    def __init__(self):
        self.computer_choice = 0
        self.computer_number = 0
        self.player_input = 0
        self.player_number = 0
        self.ulog = 100
        self.boja = ["crvena", "crna"]
    


    def display_title_bar(self):
        print("\t~~~~~~~~~~~~~~~~~~~~")
        print("\t~~~ Casino Rulet ~~~")
        print("\t~~~~~~~~~~~~~~~~~~~~")

    def get_user_choice(self):
        print("\t[1] Igraj Rulet.")
        print("\t[x] Izlaz.")

        return input("Odaberite što želite napraviti? ")
    
    def tip_kladenja(self):
        print("[1] pogađanje broja")
        print("[2] pogađanje boje")

        return input("Odaberite tip klađenja: ")
    

    def start_game(self):

        self.ulog = 100

        if self.player_input > 100 and self.player_input < 0:
            raise ponavljackiError (101)

        while self.player_input <= 1:
            self.player_input = int(input("Vaše trenutno stanje je {}. Odaberite iznos uloga:  ".format(self.ulog)))

            tip = self.tip_kladenja()
            
            while tip == '1':
                self.computer_choice = random.randrange (0,36)
                self.player_input = int(input("Odaberi broj između 1 i 36: "))

                if self.player_input == self.computer_choice:   
                    self.ulog += self.player_input * 20
                    print("Vaš ulog se povećao. Trenutno stanje je {}".format(self.ulog))
                elif self.player_input != self.computer_choice:
                    self.ulog -= self.player_input
                    print("Vaš ulog se smanjio. Trenutno stanje je {}".format(self.ulog))
                else:
                    raise ponavljackiError (101)
                
                return self.tip_kladenja()

            while tip == '2':

                while True:
                    
                    self.player_input = input("Želite li odabrati crvenu ili crnu? ".format(self.boja)).lower()
                    self.computer_choice = random.choice (self.boja)

                    if self.player_input == self.computer_choice:
                        self.ulog += self.player_input * 2
                        print("Pogodili ste boju! Vaš ulog se povećao na {}".format(self.ulog))    
                    elif self.computer_choice != self.player_input:
                        self.ulog -= self.player_input
                        print("Niste pogodili boju! Vaš ulog se smanjio na {}".format(self.ulog))
                    else: 
                        print ("HVATANJE IZUZETAKA!")
   
                return self.tip_kladenja()

            if self.ulog <= 0 and self.ulog >= 5000:
                print("Kraj igre! Došli ste do kraja limita!")
            break
            

    def play(self):
        choice = ''
        self.display_title_bar()
        while choice != 'x':
            choice = self.get_user_choice()
            self.display_title_bar()
            if choice == '1':
                self.start_game()
            elif choice == '2':
                self.start_game()
            elif choice == 'x':
                print("Hvala što ste igrali. Vidimo se opet!!! :)")
            else:
                raise ponavljackiError (000)


if __name__ == '__main__':
    game = Rulet ()
    game.play()

