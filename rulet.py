import random


class Rulet:
    def __init__(self):
        self.money = 100
        self.limit = 5000

    def display_title_bar(self):
        print("\t~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print("\t~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ RULET ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print("\t~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")


    def get_user_choice(self):
        print("\n[1] Igraj Rulet")
        print("[x] Izlaz.")

        return input("Odaberite što želite napraviti?  ")


    def start_game(self):
        while self.money <= self.limit:
            print("Imate: {} kn.".format(self.money))
            if self.money <= 0:
                print("Završili ste s igrom")
                break
            bet_amount = int(input("Ulog: "))
            while bet_amount > self.money:
                print("Nemate dovoljno novaca za takav ulog.")
                bet_amount = int(input("Ulog: "))
            self.money = self.money - bet_amount
            bet = input("Na što želite uložiti?  [1] Broj ili [2] Boja. ")

            if bet == '1':
                final_bet = int(input("Odaberite na koji broj stavljate ulog (1-36):  "))
                if 1 <= final_bet <= 36:
                    print("Rulet se okreće ...")
                    k = random.randint (1, 37)
                    print("\nKuglica na ruletu je na broju: {}".format(k))
                    if k == final_bet:
                        print("Čestitamo! Vaš ulog se povećao za 20 puta!")
                        self.money = self.money + bet_amount*20 
                    else:
                        print("Izgubili ste! Više sreće drugi put!")
                else:
                    self.money = self.money + bet_amount
                    print("HVATANJE IZUZETAKA")

            elif bet == '2':
                final_bet = input("Na koju boju stavljate ulog? Upišite crna ili crvena:  ")
                if final_bet.lower() == "crna" or final_bet.lower() == "crvena":
                    print("Rulet se okreće ...")
                    k = random.choice(["crvena", "crna"])
                    print("\nKuglica na ruletu je na boji: {}".format(k))
                    if k == final_bet:
                        print("Čestitamo! Vaš ulog se povećao za 2 puta!")
                        self.money = self.money + bet_amount*2
                    else:
                        print("Izgubili ste! Više sreće drugi put!")
                else:
                    self.money = self.money + bet_amount
                    print("HVATANJE IZUZETAKA")

            else:
                self.money = self.money + bet_amount
                print("HVATANJE IZUZETAKA")

    
    def play(self):
        choice = ''
        while choice != 'x':
            self.display_title_bar()
            choice = self.get_user_choice()
            if choice == '1':
                self.start_game()
            elif choice == 'x':
                print("Hvala na igranju! Pozdrav!")
            else:
                print("HVATANJE IZUZETAKA")
    

if __name__ == '__main__':
    game = Rulet ()
    game.play ()