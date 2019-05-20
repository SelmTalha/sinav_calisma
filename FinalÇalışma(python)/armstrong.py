sayi=int(input("Bir sayi giriniz :")) #342
basamak=str(sayi)
toplam =0
for x in basamak: #'3-4-2'
    rakam=int(x)**len(basamak)
    toplam+=rakam
if sayi==toplam:
    print("Armstrong sayısıdır.")
else:
    print("değil!")