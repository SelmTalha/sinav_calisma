#Notlar 0 ile 100 arasında değere sahip olabilir.Yoksa hata mesajı verir.
#50'den yüksek notlar geçer,50 dahil
#50'den düşük notlar kalır.

while True:
    a=int(input("Vize Notunuzu Giriniz:"))
    b=int(input("Final Notunuzu Giriniz:"))
    if(a<=100 and a>=0 and b<=100 and b>=0):
        break
    else:
        raise Exception("Hatali Giris!")

ort=a*0.4+b*0.6

def islem_kontrol():
    if(ort>=50):
        print("Geçtiniz!")
    elif(ort<50):
        print("Kaldınız!")
    else:
        pass

islem_kontrol()