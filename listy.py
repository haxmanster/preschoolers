from function import dodaj_przedszkolaka

wybor = "t"
t = str(wybor)
while wybor == t:

    print("""
    Wpisz opcje które chciałbyś wykonać w naszym programie:
        
        add - dodaje uczniów do listy
        remove - usuwa uczniow do listy
        show - pokaz uczniow na liscie 
        create - Utworz Baze przedszkolakow
""")


    dodaj_przedszkolaka(input("C:\> "))
    wybor = str(input("Kontynuowac ? T / N "))
