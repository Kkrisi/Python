'''
1.	Írj programot, mely bekér a felahsználótól egy pozitív egész számot,
 és kiírja az egész számokat a képernyőre eddig a számig, 
 egymástól pontosvessszővel elválasztva! 
 Az utolsó szám után ne legyen pontosvessző! 
'''

def elso():
    a:int = int(input(f"Kérek egy pozitív egész számot: "))
    b:int = 0
    while b<a:
        if b==a-1:
            print(b, end="")
        else:
            print(b, end="; ")
        b+=1



'''2.	Írj programot, 
mely beolvas egy pozitív egész számot, 
és kiírja az osztóit, valamint az osztóinak az összegét! '''

def masodik():
    a:int = int(input(f"Kérek egy pozitív egész számot: "))
    b:int = 1
    osszeg=0
    while b<=a:
        if a % b==0:
            if b==a:
                print(b, end="")
                osszeg+=b
            else:
                print(b, end="; ")
                osszeg+=b
       
        b+=1
    print("\nOsztók összege:",b)







'''3.	Írj programot, 
amely kiírja két bekért szám között a páros számokat!'''

def harmadik():
    a:int = int(input(f"Kérek egy pozitív egész számot: "))
    b:int = int(input(f"Kérek egy másik pozitív egész számot: "))
    if a<b:
        while a<b:
            if a % 2 == 0:
                print(a)
            a += 1
    else:
        while b<a:
            if b % 2 == 0:
                print(b)
            b += 1
        


import math

'''4.	Írj programot, amely kiírja az első 20  négyzetszámot!'''
def negyedik():
    i = 1
    while i < 20:
        negyezt = math.pow(i,2)
        print(negyezt,end=" ")
        i+=1








