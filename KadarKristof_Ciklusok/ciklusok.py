'''
import math

def szamok(a:int, b:int):

    while(a<b-1):
        a+=1
        print(math.ceil(a), end=" ")
    print("\n-----------")

'''









import math
def szamok(a:float,b:float):
    if a>b:
        csere:float = a
        a = b
        b = csere

    i:int = math.ceil(a)

    while i<b:
        if (i==b-1):
            print(i)
        else:
            print(i,end=", ")
        i+=1







