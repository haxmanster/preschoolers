import pickle


def dodaj_przedszkolaka(option):
    with open('parrot.pkl', 'rb') as f:
        listen = pickle.load(f)

    if option == "show":
        print("Przedszkolaki znajdujace sie na liscie: ", listen)

    if option == "add":
        ile = input("Ilu przedszkolaków chcesz dodac do listy ? ")
        for imie in range(int(ile)):
            listen.append(input("Imie Przedszkolaka "))
            pickle.dump(listen, f)
        print(listen)

    if option == "remove":
        listen = pickle.load(f)
        ile = input("Ilu przedszkolaków chcesz usunac z  listy ? ")
        for usun in range(int(ile)):
            listen.remove(input("imie przedszkolaka "))
            print(listen)
    return


print("""
    Wpisz opcje ktore chciałbyś wykonać w naszym programie:
        
        add - dodaje uczniów do listy
        remove - usuwa uczniow do listy
        show - pokaz uczniow na liscie 
""")
dodaj_przedszkolaka(input())
