#Choice ve sample Kullanımı:

import random

sayi=random.random()
sayi=random.uniform(1,20)
sayi=random.randint(1,20)

print(sayi)

#Choice = Liste içinden rastgele eleman seçiyo her defasında değiştiriyor.Kura çekilişi mantığı !
isimler= ["elif","gözde","yasemin","selim"]
cekilis=random.choice(isimler)
eslestirme=random.sample(isimler,2) #Sample: Rastgele çekilişe değer girerek adedi artırıyor.2 yazarsak 2 isim gözükür gibi.
print(cekilis) 
print(eslestirme)