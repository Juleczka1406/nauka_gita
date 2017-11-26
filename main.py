def wypisz_osobe(imie, nazwisko):
    print("{0} {1}".format(imie, nazwisko))

def czy_emeryt(wiek):
    MAX = 68
    if wiek < MAX:
        return False
    else:
        return True

if __name__=="__main__":
    imie = 'Justyna'
    nazwisko = 'Fil'
    wiek = 70
    print("{1} {0} {2} lat".format(imie, nazwisko, wiek))

wypisz_osobe(imie, nazwisko)
if wiek < 63:
    print('Nie emeryt')
else:
    print("Wiek produkcyjny")
    wypisz_osobe(imie, nazwisko)
    if wiek < 63:
        print('Nie emeryt')
    else:
        print("Wiek produkcyjny")
