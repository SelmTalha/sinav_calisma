class Sınıf():
    def __init__(self,isim,soyad,yas,cinsiyet,kilo,tcno):
        print("init fonksiyonu çağrıldı.")
        self.isim=isim
        self.soyad=soyad
        self.yas=yas
        self.cinsiyet=cinsiyet
        self.kilo=kilo
        self.tcno=tcno
    def toplama(self,not1,not2):
        return (not1+not2)/2

#Class içerisindeki tüm metodlar class'ın ismi ile çağrılır
#Class Tanımlamasını sinif.py dosyasında yaptık.
#main.py dosyasında ise class içeriğini çağırarak değerleri girip isteyeceğiz.!