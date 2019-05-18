sayi=int(input("Bir sayi giriniz :"))
basamak=str(sayi)
toplam =0
for x in basamak:
    rakam=int(x)**len(basamak)
    toplam+=rakam
if sayi==toplam:
    print("Armstrong sayısıdır.")
else:
    print("değil!")