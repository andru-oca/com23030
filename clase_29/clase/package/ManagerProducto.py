from package.Producto import Producto

class ManagerProducto:
    db_productos = []

    def __init__(self ,**kwargs):
        self.path = kwargs.get("path", "")
        self.nombre = kwargs.get("nombre", "carrefour")

    def crear_producto_alamacenado(self,producto:Producto):
        self.db_productos.append(producto)
        print(f"el producto: {producto.nombre} ha sido agreado a la base de datos!")

    def read_batabase(self):
        for producto in self.db_productos:
            print(producto.cantidad_stock())

    def update_producto(self, **kwargs):
        codigo = kwargs["codigo"]
        productos_cant = kwargs["productos_cant"]

        for producto in self.db_productos:
            if producto.codigo == codigo:
                producto.modificar_stock(productos_cant)

    def soft_delete(self,nombre_producto):
        for index,producto in enumerate(self.db_productos):
            if producto.nombre == nombre_producto:
                producto.status = False


    def delete_producto(self, nombre_producto):
        # self.db_productos = [
        #     productos for productos in self.db_productos if productos.nombre !=  nombre_producto
        # ]

        for index,producto in enumerate(self.db_productos):
            if producto.nombre == nombre_producto:
                self.db_productos.pop(index)
