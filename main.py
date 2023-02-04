from logo import logo





def playagain():
    while True:
        variabile1 = input("Vuoi giocare ancora? Y N")
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
            score1 = x
    print(f"Congratulazioni {score1} ha vinto puntando {check1}")


def bid():
    while True:
        try:
            bid1 = int(input("inserisci la tua puntata\n"))
            return bid1
        except:
            print("il valore inserito non sembra correto, riprova")



def name(database, firstrun):
    while True:
        name = input("Inserisci il tuo nome:\n").lower()
        if firstrun == 1:
            for x in database:
                if name in x:
                    print("Il nome inserito e' gia' stato preso")
                else:
                    return name
        else:
            return name



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
            again = input("Ci sono altre persone che voglio puntare Y N").lower()
            if again == "y":
                break
            elif again == "n":
                check = False
                break
            else:
                print("Il valore inserito non sembra corretto riprova")
    checkwinner(database)




if __name__ == "__main__":
    costanzo = True
    while costanzo:
        print(logo)
        main()
        costanzo =playagain()