#Division by zero hatası

while True:
    try:
        a=5
        b=0
        c=a/b
        print(c)

    except Exception as Selim:
        print(Selim)
        break
