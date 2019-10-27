#İnheritance (Kalıtım) Class Örnek Çalışma

class selim():
    def __init__(self):
        print("Selim class'ı oluşturuldu.")
        a=65
        b=46
        c=a+b
        print(c) 

    def yemek(self):
        print("Aç")

    
class elif1(selim):
    def __init__(self):
        print("Elif class'ı oluşturuldu")
    def yemek(self):
        print("Çok aç")

a=elif1()
a.yemek()