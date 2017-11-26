def wypisz_osobe(imie, nazwisko):
    print("{0} {1}".format(imie, nazwisko))

def czy_obowiazek_szkolny(wiek):
    MAX = 18
    if wiek < MAX:
        return True
    else:
        return False

if __name__ == "__main__":
    imie = "Magda"
    nazwisko = "Pele"
    wiek = 19
    wypisz_osobe(imie, nazwisko)
    czy_obowiazek = czy_obowiazek_szkolny(wiek)
    if czy_obowiazek == True:
        print("TAK!")
    else:
        print("NIE")
