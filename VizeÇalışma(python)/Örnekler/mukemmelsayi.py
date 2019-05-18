a=int(input("Sayi giriniz:"))
sonuc=0
i=1
while(i<a):
    if(a%i==0):
        sonuc+=i
    i+=1
if(sonuc==a):
    print(a,"Mukemmel sayidir.")
else:
    print(a,"Mukemmel sayi değildir.")