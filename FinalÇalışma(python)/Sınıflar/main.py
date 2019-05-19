from sinif import Sınıf

s_isim=input("İsminizi giriniz:")
s_soyad=input("Soyadınızı giriniz:")
s_yas=int(input("Yaşınızı giriniz:"))
s_cinsiyet=input("Cinsiyeti (E/K)")
s_kilo=int(input("Kilonuzu giriniz:"))
s_tcno=int(input("Tc Numarasını giriniz :"))
a=int(input("1.Notu giriniz:"))
b=int(input("2.Notu giriniz:"))
cocuk=Sınıf(s_isim,s_soyad,s_yas,s_cinsiyet,s_kilo,s_tcno)

print("""
    Sınıf İçeriği:

    İsim: {}

    Soyad: {}

    Yaş: {}

    Cinsiyet: {}

    Kilo: {}

    TC No: {}

    Not Ortalaması: {}
""".format(cocuk.isim,cocuk.soyad,cocuk.yas
,cocuk.cinsiyet,cocuk.kilo,cocuk.tcno,cocuk.toplama(a,b)))




