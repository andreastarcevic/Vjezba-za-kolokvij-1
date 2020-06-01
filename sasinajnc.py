import random

class Anjc:
    def __init__(self):
        self.SPIL = {'2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, '0':10, 
        'Decko':10, 'Dama':10, 'Kralj':10, 'Kec':1}

    def display_title_bar(self):
        print("\t~~~~~~~~~~~~")
        print("\t~~~ Anjc ~~~")
        print("\t~~~~~~~~~~~~")

    def get_user_choice(self):
        print("\t[1] Igraj Ajnc")
        print("\t[x] Izlaz")
        return input("Odaberite što želite napraviti:  ")
    
    def player_input(self):
        # vraća TRUE za stop i FALSE za vuci
        # while petlja za Meni u kojem su vuci ili stop
            while True:
                # lower metoda je korištena kako bi uvijek spustio unos na mala slova radi lakše usporedbe
                vuci = input("Želite li odabrati vuci (V) ili stop (S)? ").lower()
                if vuci in ("vuci", "v"):
                    return False #to mi treba u metodi koja obrađuje logiku povlacenja karata iz liste
                elif vuci in ("stop", "s"):
                    return True #to mi treba u metodi koja obrađuje logiku povlacenja karata iz liste
                else: 
                    print ("HVATANJE IZUZETAKA!")

    def start_game(self):
        deck = (['2', '3', '4', '5', '6', '7', '8', '9', '0', 'Decko', 'Dama', 'Kralj', 'Kec'])*4 #*4 je zato što ima 4 boje u kutiji karata
        random.shuffle(deck)
        # igrac/racunalo dobivaju po jednu kartu
        player = [deck.pop() for _ in range(1)] # random.int(1 10)
        computer = [deck.pop() for _ in range(1)]

        while True:
            print("Igračeva (vaša) ruka: {}".format(player))
            stop = self.player_input()
            if not stop:
                player.append(deck.pop())
                computer.append(deck.pop())
            else:
                player_total = sum(self.SPIL[card] for card in player)
                computer_total = sum(self.SPIL[card] for card in computer)
                if player_total > computer_total:
                    print("Igrač pobjeđuje. Rezultat: Igrač {} vs. Računalo {}".format(player_total, computer_total))
                else:
                    print("Računalo pobjeđuje. Rezultat Računalo {} vs. Igrač {}".format(computer_total, player_total))
                
            total = sum(self.SPIL[card] for card in player)
            if total > 21:
                print("Premašili ste rezultat, vaša ruka {}".format(total))
                break
            elif total == 21:
                print("Pobjeđujete! Imate ajnc! Vaša ruka je {}".format(total))
                break
            elif stop:
                print("Stali ste s igrom. Završni rezultat je: Igrač {} vs. Računalo {}".format(total, sum(self.SPIL[card] for card in computer)))
                break

    def play(self):
        choice = ''
        self.display_title_bar()
        while choice != 'x':
            choice = self.get_user_choice()
            self.display_title_bar()
            if choice == '1': # u ovoj situaciji choice ima vrijednost '1' što je string, a vi ga uspoređujete s brojem
                self.start_game()
            elif choice == 'x':
                print("\nHvala na igranju! Pozdrav!")
            else: 
                print("HVATANJE IZUZETKA")

if __name__ == '__main__':
    game = Anjc()
    game.play()

