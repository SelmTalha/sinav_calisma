#Fibonacci serisi yazdırın.
# 0 , 1 , 1 , 2 , 3 , 5 , 8 , 13 , 21 , ...
# a , b
#       , c
#     a , b

a=0
b=1
while a<100:
    print(a)
    c= a+b
    a=b
    b=c