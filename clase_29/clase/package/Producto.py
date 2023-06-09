

class Producto:
    # el atributo de clase
    status = True

    # def __init__(self, nombre, codigo, stock ):
    #     self.nombre = nombre
    #     self.codigo = codigo
    #     self.stock = stock

    def __init__(self,**kwargs):
        self.nombre:str = kwargs["nombre"]
        self.codigo:int = kwargs["codigo"]
        self.stock:int = kwargs["stock"]

    def __str__(self):
        return f"""

        El producto es: {self.nombre}
        {'*'*50}
        """
    def cantidad_stock(self):
        return f"Producto {self.nombre}:\n\t Stock:{self.stock}"
    
    def modificar_stock(self, cantidad_modificar):
        self.stock += cantidad_modificar
    
    def estado_producto(self):
        # if self.status:
        #     return f"Tenemos disponible"
        # else:
        #     return f"No disponible"

        return  f"{self.nombre}::Tenemos disponible" if self.status else f"{self.nombre}::No disponible"