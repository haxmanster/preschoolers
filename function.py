import pickle
import os.path


def dodaj_przedszkolaka(option):
    listen = []

    if os.path.isfile("parrot.pkl") is False:
        with open('parrot.pkl', 'wb') as f:
            pickle.dump(listen, f)

    if option == "show":
        with open('parrot.pkl', 'rb') as f:
            listen = pickle.load(f)
            for show in listen:
                print("Przedszkolaki znajdujace sie na liscie:", show)

    if option == "add":
        ile = input("Ilu przedszkolaków chcesz dodac do listy ? ")
        with open('parrot.pkl', 'rb') as f:
            listen = pickle.load(f)
        for imie in range(int(ile)):
            listen.append(input("Imie Przedszkolaka "))
            with open('parrot.pkl', 'wb') as f:
                pickle.dump(listen, f)
        print(listen)

    if option == "remove":
        with open('parrot.pkl', 'rb') as f:
            listen = pickle.load(f)
        ile = input("Ilu przedszkolaków chcesz usunac z  listy ? ")
        print(listen)
        for usun in range(int(ile)):
            listen.remove(input("imie przedszkolaka "))
            with open('parrot.pkl', 'wb') as f:
                pickle.dump(listen, f)
            print(listen)
    return


def oceny_maluszkow(option):

    oceny = {}

    if os.path.isfile('oceny.pkl') is False:
        with open('oceny.pkl', 'wb') as f:
            pickle.dump(oceny, f)

    if option == "add":

        with open('oceny.pkl', 'rb') as f:
            oceny = pickle.load(f)
        ile = input("Ilu przedszkolaków chcesz ocenic?  ")

        for dodaj in range(int(ile)):
            dziecko = input("Wpisz przedszkolaka ktorego chcesz ocenic: ")
            wynik = int(input("Podaj ocene 0d 1 do 6: "))
            oceny[dziecko] = wynik
        with open('oceny.pkl', 'wb') as f:
            pickle.dump(oceny, f)
        

    if option == "show":
        with open('oceny.pkl', 'rb') as f:
            oceny = pickle.load(f)
        print(oceny)
    return
