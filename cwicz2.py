"""
Zwracanie brakujących elementow
"""
def brakujace_dane(tab, maks):
    wynik = []
    zmienna = False
    for x in range(1, int(maks)):
        for y in tab:
            if(x == y):
                zmienna = True
        if(zmienna == False):
            wynik.append(x)
        zmienna = False
    return(wynik)

tab = [3, 5, 9, 14, 20]
maks = 25
print(brakujace_dane(tab, maks))