"""
Generowanie listy liczb
"""
def generowanie(a, b):
    n = 0.5
    tab =[]
    for x in range(0, int((b - a)/n)+1):
        tab.append(a+ (x * n))

    return tab

a = 2.0
b = 5.5
print(generowanie(a, b))