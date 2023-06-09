
"""
GENERAR ABM 
CRUD => 
    CREATE
    RETRIEVE - READ
    UPDATE
    DELETE

MANAGER_PRODUCTOS

SOY CARREFOUR/COMPETENCIA Y QUIERO UN SISTEMA QUE ME MANEJE PRODUCTOS
"""

from package.Producto import Producto
from package.ManagerProducto import ManagerProducto

fideo = Producto(
    stock = 100,
    codigo = 987897,
    nombre = "fideos"
)

print(fideo.cantidad_stock())
fideo.modificar_stock(-200)
print(fideo.cantidad_stock())
fideo.status = True
print(fideo.estado_producto())

arroz = Producto(
    stock = -10,
    codigo = 767862,
    nombre = "arroz"
)

pizza = Producto(
    stock = 10_000,
    codigo = 9_999_666,
    nombre = "pizza"
)

manager_productos = ManagerProducto(
    nombre = "Coto"
)


print("CREATE", "#"*50)

manager_productos.crear_producto_alamacenado(fideo)
manager_productos.crear_producto_alamacenado(pizza)
manager_productos.crear_producto_alamacenado(arroz)

print("READ", "#"*50)
manager_productos.read_batabase()

print("UPDATE", "#"*50)
manager_productos.update_producto(
    codigo=9_999_666,
    productos_cant = -100000
)
manager_productos.read_batabase()

print("DELETE", "#"*50)
manager_productos.delete_producto("arroz")
manager_productos.read_batabase()

manager_productos.soft_delete("pizza")

for producto in manager_productos.db_productos:
    
    print(producto.estado_producto())