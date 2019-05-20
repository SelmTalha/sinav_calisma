class dnm:
    def __init__(self):
        print("init fonksiyonu çağrıldı")
        self.sayfa_sayisi=524
    def __str__(self):
        return "İsim : Selim Talha Çağlar"
    def __len__(self):
        return self.sayfa_sayisi
    def __del__(self):
        print("dnm class siliniyor ...")

kitap1=dnm()
print(len(kitap1))
del kitap1
#len(kitap1)