#Random if else Çalışması
#Toplama İşlemi
import random
a=random.randint(1,50)
b=random.randint(1,50)
gs=a+b
print(a)
print(b)
c=int(input("Sonucu Giriniz:"))
if (c == gs):
    print("Doğru Buldunuz!")
else:
    print("Yanlış Buldunuz!")