n=int(input("Sayi giriniz:"))
def fact(n):
    a=1
    sonuc=1
    for i in range(a,n+1):
        sonuc=sonuc*a
        a+=1
    return sonuc

print(fact(n))