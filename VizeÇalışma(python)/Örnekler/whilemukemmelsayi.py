sayi = int(input("Sayi:"))

i=1
toplam=0
while(i<sayi):
    if(sayi%i==0):
        toplam+=i
    i+=1
if (toplam==sayi):
    print("Mükemmel sayi")
else:
    print("Mükemmel sayi değil !")


# sayı 6          
# i 1         /2  /3  /4  /5  /6
#  toplam 0   /1  /3  /6

