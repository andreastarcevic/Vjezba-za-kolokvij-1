import random
from kartaskaigraError import kartaskaigraError

class Kartaska_igra:
    def __init__(self):
        self.ranks = ["Kec", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Decko", "Dama", "Kralj"] * 4
        self.deck = []
        self.broj_rundi = 0

        value = 1
        for rank in self.ranks:
            self.deck.append([rank, value])
        value = value + 1

        random.shuffle(self.deck)
        self.player_score = 0
        self.computer_score = 0
        self.player_choice = 0
        self.computer_choice = 0

    def display_title_bar(self):
        print("\t~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print("\t~~~~ Dobrodošli u kartašku igru ~~~~")
        print("\t~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

    def get_user_choice(self):
        print("\n[1] Igraj kartašku igru.")
        print("[x] Izlaz.")

        return input("Odaberite što želite napraviti?  ")

    def vrijednosti_computer(self):
        if self.computer_choice == '2':
            self.vrijednosti_computer = 2
        if self.computer_choice == '3':
            self.vrijednosti_computer = 3
        if self.computer_choice == '4':
            self.vrijednosti_computer = 4
        if self.computer_choice == '5':
            self.vrijednosti_computer = 5
        if self.computer_choice == '6':
            self.vrijednosti_computer = 6
        if self.computer_choice == '7':
            self.vrijednosti_computer = 7
        if self.computer_choice == '8':
            self.vrijednosti_computer = 8
        if self.computer_choice == '9':
            self.vrijednosti_computer = 9
        if self.computer_choice == '10':
            self.vrijednosti_computer = 10
        if self.computer_choice == 'decko':
            self.vrijednosti_computer = 11
        if self.computer_choice == 'dama':
            self.vrijednosti_computer = 12
        if self.computer_choice == 'kralj':
            self.vrijednosti_computer = 13
        else:
            raise kartaskaigraError (000)

    def vrijednosti_player(self):
        if self.player_choice == '2':
            self.vrijednosti_player = 2
        if self.player_choice == '3':
            self.vrijednosti_player = 3
        if self.player_choice == '4':
            self.vrijednosti_player = 4
        if self.player_choice == '5':
            self.vrijednosti_player = 5
        if self.player_choice == '6':
            self.vrijednosti_player = 6
        if self.player_choice == '7':
            self.vrijednosti_player = 7
        if self.player_choice == '8':
            self.vrijednosti_player = 8
        if self.player_choice == '9':
            self.vrijednosti_player = 9
        if self.player_choice == '10':
            self.vrijednosti_player = 10
        if self.player_choice == 'decko':
            self.vrijednosti_player = 11
        if self.player_choice == 'dama':
            self.vrijednosti_player = 12
        if self.player_choice == 'kralj':
            self.vrijednosti_player = 13
        else:
            raise kartaskaigraError (000)


    def start_game(self):

        self.broj_rundi = 0

        while self.broj_rundi <= 3:
            self.broj_rundi += 1

            print("\nVaš trenutni rezultat je {}".format(self.player_score))
            print("Računalov trenutni rezultat je {}".format(self.computer_score))

            self.player_choice = random.choice(self.ranks)
            self.computer_choice = random.choice(self.ranks)

            if self.player_choice > self.computer_choice:
                print("Ovu rundu ste dobili Vi!")
                self.player_score += 1
            elif self.player_choice < self.computer_choice:
                print("Ovu rundu je dobilo računalo!")
                self.computer_score += 1
            elif self.player_choice == self.computer_choice:
                print("Izjednačeno!")
            else:
                raise kartaskaigraError (000)

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
                raise kartaskaigraError (000)

if __name__ == '__main__':
    game = Kartaska_igra()
    game.play()