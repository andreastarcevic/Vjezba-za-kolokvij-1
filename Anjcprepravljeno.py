#Filip Vidović- prvi kolokvij
import random
from AnjcError import AnjcError
class Anjc:
    def __init__(self):
        self.player_karte=None
        self.komp_karte=None
        self.karta_odabir=(["2","3","4","5","6","7","8","9","0","Decko","Dama","Kralj","As"])*4
        self.bodovi_igrac=0
        self.komp_bodovi=0
        self.izvucene_karte=0
        
        
    def unos_broja_igraca(self):
        self.unos_broja_igraca=int(input("unesite broj između 1 i 200:"))
        print("Igrač je odabrao broj {}".format(self.unos_broja_igraca))

    def kompjuter_odabir(self):
        self.kompjuter_odabir=random.choice(range(1,200))
        print("Komp je odabrao broj {}".format(self.kompjuter_odabir))

    def get_user_choice(self):
        print("[1]Igraj kartašku igru:")
        print("[x] izlaz")

        return input ("što želite napravit:")

    def kartePlayer(self):
        if self.player_karte=="2":
           self.karta_vrijednost=2
        elif self.player_karte=="3":
            self.karta_vrijednost=3
        elif self.player_karte=="4":
            self.karta_vrijednost=4
        elif self.player_karte=="5":
            self.karta_vrijednost=5
        elif self.player_karte=="6":
            self.karta_vrijednost=6
        elif self.player_karte=="7":
            self.karta_vrijednost=7
        elif self.player_karte=="8":
            self.karta_vrijednost=8
        elif self.player_karte=="9":
            self.karta_vrijednost=9
        elif self.player_karte=="0":
            self.karta_vrijednost=10
        elif self.player_karte=="Decko":
            self.karta_vrijednost=10
        elif self.player_karte=="Dama":
            self.karta_vrijednost=10
        elif self.player_karte=="Kralj":
            self.karta_vrijednost=10
        elif self.player_karte=="As":
            self.karta_vrijednost=1
        else:
            raise AnjcError(000)
        
    def karteRacunalo(self):
        if self.komp_karte=="2":
           self.karta_vrijednost=2
        elif self.komp_karte=="3":
            self.karta_vrijednost=3
        elif self.komp_karte=="4":
            self.karta_vrijednost=4
        elif self.komp_karte=="5":
            self.karta_vrijednost=5
        elif self.komp_karte=="6":
            self.karta_vrijednost=6
        elif self.komp_karte=="7":
            self.karta_vrijednost=7
        elif self.komp_karte=="8":
            self.karta_vrijednost=8
        elif self.komp_karte=="9":
            self.karta_vrijednost=9
        elif self.komp_karte=="0":
            self.karta_vrijednost=10
        elif self.komp_karte=="Decko":
            self.karta_vrijednost=10
        elif self.komp_karte=="Dama":
            self.karta_vrijednost=10
        elif self.komp_karte=="Kralj":
            self.karta_vrijednost=10
        elif self.komp_karte=="As":
            self.karta_vrijednost=1
        else:
            raise AnjcError(000)
        

    def igra(self):
        self.player_karte=random.choice(self.karta_odabir)
        self.komp_karte=random.choice(self.karta_odabir)
        self.player_input=input("unesite vuci ili stop:").lower()
        
        if self.player_input=="vuci":
            print("Igrac je dobio {}:".format(self.player_karte))
            print("komp je dobio {}:".format(self.komp_karte))
            self.izvucene_karte=self.izvucene_karte+2
            print("Do sada je izvučeno {} karata".format(self.izvucene_karte))
            self.kartePlayer()
            self.bodovi_igrac+= self.karta_vrijednost
            self.karteRacunalo()
            self.komp_bodovi+= self.karta_vrijednost
            print("Igrač ima osvojenih {}".format(self.bodovi_igrac))
            print("Računalo ima osvojenih {}".format(self.komp_bodovi))
           
            if self.bodovi_igrac==21 :
                print("Čestitamo, pobijedili ste")
                return self.get_user_choice()
            elif self.komp_bodovi==21:
                print("Računalo je pobijedilo")
                return self.get_user_choice()
            elif self.bodovi_igrac>21:
                print("izgubili ste, prekoračili ste broj")
                return self.get_user_choice()
            elif self.komp_bodovi>21:
                print("pobijedili ste, komp prekoračio broj")
                return self.get_user_choice()
            
            
        elif self.player_input=="stop":
            print("Hvala na igri, konačni bodovi su:")
            print(self.bodovi_igrac)
            print(self.komp_bodovi)
            if self.bodovi_igrac>self.komp_bodovi:
                print("Čestitamo pobijedili ste")
                return self.get_user_choice()
            elif self.komp_bodovi>self.bodovi_igrac:
                print("Računalo pobjeđuje")
                return self.get_user_choice()
            else :
                print("Nerijšeno je")
                return self.get_user_choice()
        else:
            raise AnjcError(101)
        

    def play(self):
        choice=''
        while choice!="x":
            choice=self.get_user_choice()
            broj_igrac=self.unos_broja_igraca()
            broj_komp=self.kompjuter_odabir()
            while self.bodovi_igrac<=200 or self.komp_bodovi<=200:
                if choice=="1":
                    self.igra()
                elif choice=="x":
                    print("Hvala na igri")
                else:
                    raise AnjcError(101)
               
                    

if __name__=="__main__":
    game=Anjc()
    game.play()


        







