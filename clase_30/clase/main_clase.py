class _Vehiculo_:

    def on(self):
        pass

    def off(self):
        pass



#HERENCIA


class Remolque:
    def aguanta(self):
        print("si sr, aguanto")


class PropiedasCoche(_Vehiculo_):
    status = False

    def on(self):
        print(f"el motor {self.motor} prendido")
        self.status = True

    def off(self):
        print(f"el motor {self.motor} esta apagado")
        self.status = False

    def  remolcar(self, remolque:Remolque):
        remolque.aguanta()


class PropiedasCocheIngles(_Vehiculo_):
    status = True

    def __init__(self,idioma = "ingles"):
        self.idioma = idioma

    def on(self):
        print(f"IS ON MADAF")
        self.status = True

    def off(self):
        print(f"SARAKATUNGA")
        self.status = False



class PremiumCar(PropiedasCocheIngles):
    def __init__(self, calidad="Premium",idioma= "ingles"):
        PropiedasCocheIngles.__init__(self, idioma )
        self.idioma = idioma

porsche = PremiumCar()
porsche.on()
porsche.off()

# ENCAPSULAMIENTO
class Auto(PropiedasCoche):


    def __init__(self,motor:str, cant_ruedas:int):
        self.motor = motor
        self.cant_ruedas = cant_ruedas
        self.__kms = 100

    def kilometraje(self,medida):
        if medida == "km":
            print(f"{self.__kms} kms andados")
        elif medida == "millas":
            print(f"{self.__kms/1.61} millas")
        else:
            print("ni idea macho")

    def set_kms(self,kms):
        self.__kms += kms
    

volvo = Auto("v8", 4)
volvo.kilometraje("km")
volvo.set_kms(2000)
volvo.kilometraje("km")
print(volvo._Auto__kms)


volvo.on()
volvo.off()
print("****"*10)
remo = Remolque()
volvo.remolcar(remo)


# def deco_zero(fn):

#     def validador(a,b):
#         if b==0:
#             print("zappallo,como vas a dividir por zero???, a marzo")
#             return
#         else:
#             return fn(a,b)

#     return validador

# @deco_zero
# def division(a,b):
#     return a/b

# print(division(20,2))