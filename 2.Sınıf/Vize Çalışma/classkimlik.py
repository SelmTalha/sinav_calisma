#Classın içinde kimlik oluşturma 
# self=içinde demek
class gozde():
    def __init__(self,boy,kilo,yas):
        self.boy=boy
        self.kilo=kilo
        self.yas=yas
    def kimlik(self):
        print("""
            Boy={}
            Kilo={}
            Yaş={}
        """.format(self.boy,self.kilo,self.yas))
        # print("Boy={}".format(self.boy))
        # print("Kilo={}".format(self.kilo))
        # print("Yas={}".format(self.yas))

selim=gozde(1.90,85,21)
elif1=gozde(1.50,54,7)
selim.kimlik()
print(selim.boy,selim.kilo,selim.yas)