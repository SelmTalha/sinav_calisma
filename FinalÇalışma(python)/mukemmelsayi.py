
a=int(input("Sayiyi giriniz :"))
sonuc=0 
for i in range(1,a):
    if(a%i==0):
        sonuc+=i

if(a==sonuc):
    print("Mukemmel sayi")

else:
    print("değil")