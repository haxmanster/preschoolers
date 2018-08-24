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
