

texto_bienvenida = "hola mundo"

texto_bienvenida_con_hint:str = "hola mundo"

print(
    texto_bienvenida ,
    "\n",
    texto_bienvenida_con_hint
)

# ------------------------
# edad = input("ingresa la edad ==> tomado desde la consola \n")
# print( edad + 1 )
# ------------------------
"""
condicionales
if( condicion ){
    bloque de codigo
}
"""

# if edad > 50 :
#     print("el usuario es mayor de 50")
# elif edad > 18 :
#     print("es mayor de edad")
# else :
#     print("no es mayor de edad")


# ------------------------

# text_ext = """

#     El filósofo griego explica que la motivación y el esfuerzo son dos elementos clave para conseguir todos los objetivos que uno se proponga.
#     Y que, además,cuando se pone empeño en algo que al final se consigue, el logro es mucho más satisfactorio para esa persona. 

# """

# cont = 0

# for chars in text_ext:

#     if chars == "ó":
#         cont += 1
#         print("te encontré!", cont)


# for num in range(100,10,-2):
#     print(num)


# flag = True


# while flag:
#     edad = input("ingresar edad: \n")
#     edad = int(edad)

#     if edad > 18 :
#         print("sos mayor de edad, ahora podes tomarte una guinness")
#         flag = False
    
#     print("no sos mayor de edad, intentalo de nuevo")
# else:
#     print("ya te tomaste la guinness, ahora podes pasar")


# while True:

#     edad = input("ingresar edad: \n")
#     edad = int(edad)

#     if edad > 18 :
#         print("sos mayor de edad, ahora podes tomarte una guinness")
#         break
#     else:
#         print("no sos mayor de edad, intentalo de nuevo")


from alvaro_constantes.credenciales import PASS_AWS


print(PASS_AWS)





