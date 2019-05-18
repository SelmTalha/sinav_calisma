a=int(input("a giriniz :"))
def uclecarp(a):
    print("1.Fonksiyon Çalıştı !")
    return a*3

def ikiyletopla(a):
    print("2.Fonksiyon Çalıştı !")
    return a+2

def dördeböl(a):
    print("3.Fonksiyon Çalıştı !")
    return a/4

print(dördeböl(ikiyletopla(uclecarp(a))))