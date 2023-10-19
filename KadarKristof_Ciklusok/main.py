
'''
Kérj be 2 számot a felhasznalotol (main.py)
    Irj eljarast
        szamok néven, (ciiklusok.py)
        melynek parametere a felhasznalo által megadott két szám
        és
        az eljarast kiirja a szamokat ezen két paraméter között
'''

import ciklusok

a:int = int(input("a: "))
b:int = int(input("b: "))
ciklusok.szamok(a,b)
" A felhasználó csak olyan b-t tudjon megadni, am inagyobb, mint az a"

while (a>b):
    print("B-nek nagyobnake kell lennie A-nál")
    b:int = int(input(f"Adj az {a}-nal nagyobbat!"))




ciklusok.szamok(a,b)



