# Imamo karte od keca do kralja s 4 boje
# Računalo izvlači jednu kartu i izvukli ste kartu br. 5 i(1) vi sada kažete viša ili manja,
# (2) računalo izvlači sljedeću kartu, (3) radi se usporedba karata te ako ste vi recimo
# rekli viša i računalo je izvuklo kartu 6 dobijete poruku točno, a ako ste rekli niža,
# a računalo je izvuklo 6, dobijete poruku netočno i zaustavlja se igra

import random
class Karte:
    def __init__(self):
        self.ranks = ["Kec", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Decko", "Dama", "Kralj"] # [0, 1, 2, ....]
        self.suits = ["Tref", "Srce", "Karo", "Pik"]
        self.deck = []
        value = 1
        for rank in self.ranks:
            for suit in self.suits:
                self.deck.append([rank +  " iz "  + suit +  " boje " , value])
            value = value + 1

        random.shuffle(self.deck)
        self.score = 0
        self.card1 = self.deck.pop(0)

    def display_title_bar(self):
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print("~~~~~~~~~~~~~~~~~~~~~~~ Kartaška igra - izvlačenje ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

    def get_user_choice(self):
        print("\n[1] Pokreni kartašku igru")
        print("[x] Izlaz")
        return input ("Što želite napraviti?  ")

    def start_game(self):
        while True:
            print("Vaš trenutni rezultat je {}".format(self.score))
            print("\nVaša trenutna karta je {}".format(self.card1[0]))
            while True:
                choice = input("Viša (v) ili Niža (n) karta?  ")
                if choice[0].lower() in ["v", "n"]: # ako je prvo slovo v ili n izlazi iz ove while petlje i nastavlja
                    break
            self.card2 = self.deck.pop(0)
            print("Sljedeća odabrana karta je {}".format(self.card2))
            # vi sad trebate vidjeti je li korisnik upisao v ili n
            # te ovisno o upisu v ili n usporediti karte i ispisati pogodak te nastaviti,
            # ako je pogodak, igra se nastavlja i rezultat pogođenih karata se povećava u var score,
            # a ako nije pogodak, izaći iz petlje i završiti igru
        
            if choice[0].lower() == "v" and self.card2[1] > self.card1[1]:
                print("Točno")
                self.score = self.score +1 # self.score += 1
            elif choice[0].lower() == "v" and self.card2[1] < self.card1[1]:
                print("Netočno, vaš završni rezultat je {}".format(self.score))
                break

            elif choice[0].lower() == "n" and self.card2[1] < self.card1[1]:
                print("Točno")
                self.score = self.score + 1
            elif choice[0].lower() == "n" and self.card2[1] > self.card1[1]:
                print("Netočno, vaš završni rezultat je {}".format(self.score))
                break

            else: 
                print("Karte su jednake, nema povećanja rezultata. Vaš rezultat je {}".format(self.score))

            self.card1 = self.card2

    def play(self):
        choice = ''
        self.display_title_bar()
        while choice != 'x':
            choice = self.get_user_choice()
            self.display_title_bar()
            if choice == '1':
                self.start_game()
            elif choice == 'x':
                print("\n Hvala na igri, pozdrav!")
            else:
                print("Hvatanje izuzetaka")

if __name__ == '__main__':
    game = Karte()
    game.play()
