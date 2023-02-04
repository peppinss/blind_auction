from logo import logo





def playagain():
    while True:
        variabile1 = input("Vuoi continuare con il prossimo oggetto? Y N").lower
        if variabile1 == "y" or variabile1 == "yes":
            return True
        elif variabile1 == "n" or variabile1 == "no":
            return False
        else:
            print("Il valore inserito non sembra correto, prova di nuovo")



def checkwinner(database):
    check2 = 0
    for x in database:
        check1 = database[x]
        if check1 > check2:
            highestvalue = check1
            nameofthewinner = x
    print(f"Congratulazioni {nameofthewinner} ha vinto puntando {highestvalue}$")


def bid():
    while True:
        try:
            bid1 = int(input("inserisci la tua puntata $\n"))
            if bid1 > 0:
                return bid1
            else:
                print("Il valore inserito e' troppo basso")
        except:
            print("il valore inserito non sembra correto, riprova")



def name(database, firstrun):
    while True:
        name = input("Inserisci il tuo nome:\n").lower()
        if firstrun == 1:
            for x in database:
                if name in x:
                    print("Il nome inserito e' gia' stato preso")
                elif len(name) > 2:
                    return name
                else:
                    print("il nome scelto non rispetta i criteri minimi")
        elif len(name) > 2:
            return name
        else:
            print("il nome scelto non rispetta i criteri minimi")



def main():
    database = {}
    check = True
    firstrun = 0
    while check:
        name1 = name(database, firstrun)
        if firstrun == 0:
            firstrun = 1
        bid1 = bid()
        database[name1] = bid1
        while True:
            again = input("Ci sono altre persone che voglio puntare? Y N\n").lower()
            if again == "y":
                break
            elif again == "n":
                check = False
                break
            else:
                print("Il valore inserito non sembra corretto riprova")
    checkwinner(database)




if __name__ == "__main__":
    print("Benvenuto")
    tryagain = True
    while tryagain:
        print(logo)
        main()
        tryagain = playagain()