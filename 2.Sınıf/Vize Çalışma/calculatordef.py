#Calculator(Hesap Makinası)
a=int(input("1.Sayıyı Giriniz:"))
b=int(input("2.Sayıyı Giriniz:"))
c=int(input("3.Sayıyı Giriniz:"))
print("a.Toplama İşlemi")
print("b.Çıkarma İşlemi")
print("c.Çarpma İşlemi")
print("d.Bölme İşlemi")
d=input("Seçim yapınız:")

def toplama (a,b,c):
    print(a+b+c)
def cikarma (a,b,c):
    print(a-b-c)
def carpma (a,b,c):
    print(a*b*c)
def bolme (a,b,c):
    print(float(a)/float(b)/float(c))

if(d=='a'):
    toplama(a,b,c)
elif(d=='b'):
    cikarma(a,b,c)
elif(d=='c'):
    carpma(a,b,c)
elif(d=='d'):
    bolme(a,b,c)
else:
    print("Yanlış Değer girdiniz:")