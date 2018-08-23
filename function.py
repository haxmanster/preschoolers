import pickle


def dodaj_przedszkolaka(option):
    listen = []

    if option == "create":
        with open('parrot.pkl', 'wb') as f:
            pickle.dump(listen, f)
    if option == "show":
        with open('parrot.pkl', 'rb') as f:
            listen = pickle.load(f)
        print("Przedszkolaki znajdujace sie na liscie: ", listen)

    if option == "add":
        ile = input("Ilu przedszkolaków chcesz dodac do listy ? ")
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
            print(listen)
    return
