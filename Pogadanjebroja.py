import random
from pogadanjebrojaError import pogadanjebrojaError

class Pogadanje:
    def __init__(self):
        self.computer_choice = 0
        self.player_input = 0
        self.broj_pokusaja = 0


    def display_title_bar(self):
        print("\t~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print("\t~~~ Igra pogađanja broja ~~~")
        print("\t~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

    def get_user_choice(self):
        print("\t[1] Igraj pogađanje broja.")
        print("\t[x] Izlaz.")

        return input("Odaberite što želite napraviti? ")

    def start_game(self):

        self.broj_pokusaja = 0

        if self.player_input > 100 and self.player_input < 0:
            raise pogadanjebrojaError (101)

        self.computer_choice = random.randrange (0,100)
        self.player_input = int(input("Odaberite broj između 1 i 100:  "))

        while self.broj_pokusaja <= 10:
            self.broj_pokusaja += 1
            if self.player_input < self.computer_choice:
                print("Vaš broj je manji od traženog! Pokušajte ponovno!")
                self.player_input = int(input("Odaberite broj između 1 i 100:  "))
            elif self.player_input > self.computer_choice:
                print("Vaš broj je veći od traženog! Pokušajte ponovno!")
                self.player_input = int(input("Odaberite broj između 1 i 100:  "))
            elif self.player_input == self.computer_choice:
                print("Pogodak!")
                break

            if self.broj_pokusaja >= 10:
                print("Potrošili ste sve pokušaje! Vaš traženi broj je {}".format(self.computer_choice))
                break

    def play(self):
        choice = ''
        self.display_title_bar()
        while choice != 'x':
            choice = self.get_user_choice()
            self.display_title_bar()
            if choice == '1':
                self.start_game()
            elif choice == 'x':
                print("Hvala što ste igrali. Vidimo se opet!!! :)")
            else:
                raise pogadanjebrojaError (000)


if __name__ == '__main__':
    game = Pogadanje()
    game.play()