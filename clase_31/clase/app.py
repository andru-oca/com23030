def division(a,b):
    try:
        b=int(b)
        return a/b
    except ValueError as e:
        print(e)
        
    except ZeroDivisionError as e:
        print(e)
        print("zapallo, como me vas a dividir por cero?")


division(1,"0.")

print("SIGO FUNCIONANDO!")