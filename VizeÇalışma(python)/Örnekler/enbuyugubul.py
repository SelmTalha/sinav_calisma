a=int(input("Bir sayi giriniz:"))
b=int(input("Bir sayi giriniz:"))
c=int(input("Bir sayi giriniz:"))

d=a
if(a<b):
    d=b
elif(b<c):
    d=c
else:
    d=a
print(d)