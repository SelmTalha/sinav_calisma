#Kullanicidan istenilen 3 sayinin en buyugunu ekrana bastirma
a=int(input("1.sayıyı giriniz:"))
b=int(input("2.sayıyı giriniz:"))
c=int(input("3.sayıyı giriniz:"))
if (a>=b) and (a>=c):
    buyuk=a
elif(b>=a) and (b>=c):
    buyuk=b
else:
    buyuk=c
print (buyuk)