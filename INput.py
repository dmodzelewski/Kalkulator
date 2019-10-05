def Input(dzialanie):
    a = input("Podaj a")
    b = input("Podaj b")
    dzialanie()
    return dzialanie

def dzialanie(wybor):
    pass

if "__main__" == __name__:
    print("Podaj działanie dowykonania\n1.Dodawanie\n2.Odejmowanie\n3.Dzielenie\n4.Mnożenie")
    wybor = int(input("\n"))
    if wybor == 1:
        dzialanie()
    elif wybor == 2:
        dzialanie()
    elif wybor == 3:
        dzialanie()
    elif wybor == 4:
        dzialanie()
    else:
        print("Coś nie działa")