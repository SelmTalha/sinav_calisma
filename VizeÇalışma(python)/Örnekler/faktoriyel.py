n=int(input("Sayi giriniz:"))
def fact(n):
    a=1
    sonuc=1
    while a<=n:
        sonuc = sonuc *a
        a+=1
    return sonuc
print(fact(n))