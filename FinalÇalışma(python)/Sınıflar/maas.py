class Yazılımcı():
    def __init__(self,isim,soyisim,numara,maaş,diller):
        self.isim = isim
        self.soyisim = soyisim
        self.numara = numara 
        self.maaş = maaş
        self.diller = diller
    def bilgilerigöster(self):
        print("""
        Çalışan Bilgisi:

        İsim : {}

        Soyisim : {}

        Şirket Numarası: {}

        Maaş : {}

        Diller: {}
        """.format(self.isim,self.soyisim,self.numara,self.maaş,self.diller))

    def dil_ekle(self,yeni_dil):
        print("Dil ekleniyor.")
        self.diller.append(yeni_dil)

    def maas_yukselt(self,zam_miktarı):
        print("Maaş yükseliyor...")
        self.maaş += zam_miktarı

yazilimci1 = Yazılımcı("Selim","Çağlar",542,3000,['Java','PHP'])
#yazilimci1.bilgilerigöster()
yazilimci1.dil_ekle("Python")
yazilimci1.bilgilerigöster()
yazilimci1.maas_yukselt(500)
yazilimci1.bilgilerigöster()