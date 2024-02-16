# 
#################################################
### EJERCICIOS PROPUESTOS
#################################################
# 01 Escribir un programa que pregunte por consola el precio de un producto 
# en soles con cuatro decimales y muestre por pantalla el número de soles y 
# el número de céntimos del precio introducido en dos decimales.

# precio = input("Introduce el precio de un producto con 4 decimales: ")
# deci = round(float(precio), 2)
# cadena = str(deci).split(".")
# # print(f"{cadena[0]} soles y {cadena[1]} centimos")
# print(f"{str(deci)[0:str(deci).find('.')]} soles y {str(deci)[str(deci).find('.')+1:]} centimos")


#02 Escribir un programa que pregunte el nombre de un producto, 
# su precio y un número de unidades y muestre por pantalla una cadena con el 
# nombre del producto seguido de su precio unitario con 6 dígitos enteros 
# y 2 decimales, el número de unidades con tres dígitos y el coste total 
# con 8 dígitos enteros y 2 decimales.

# producto = input("Introduce el nombre del producto: ")
# precio = float(input("Precio unitario: "))
# unidades = int(input("Ingrese unidades: "))
# cadena_precio = str(precio).split('.')
# precio_entero = len(cadena_precio[0])
# precio_decimal = len(cadena_precio[1])
# precio_final = str(cadena_precio[0]).zfill(6) + '.' + cadena_precio[1]
# print(cadena_precio)
# print(str(cadena_precio[0]).zfill(6))
# print(f"{precio_final}")
#1213.345
#['1213', '345']
# print(f"{producto}: Precio unitario S/. {str(round(precio, 2)).zfill(8)} soles, {unidades} unidades, Total: S/. {round(unidades * precio, 2)} soles.")

# if precio_entero == 6 and precio_decimal == 2:
# 	#posición
# 	print(f"{producto}: Precio unitario S/. {round(precio, 2)} soles, {unidades} unidades, Total: S/. {round(unidades * precio, 2)} soles.")
# 	# print(f"{producto}: Precio unitario S/. {round(precio, 2)} soles, {unidades} unidades, Total: S/. {round(unidades * precio, 2)} soles.")
# else:
# 	print("El precio ingresado no es el correcto.")


#################################################
### Funciones
#################################################
# Es un bloque de codigo que te permite reutilizar las veces que quieras
# la ejecución del codigo

# Función normal
from re import A


def saludo():
	print("Hola, este es una función.")


# Función con variable
def saludo_nombre(nombre):
	print(f"Hola, mi nombre es {nombre}.")


# Función que retorna una cadena string
def saludo_string(nombre, apellido):
	cadena = f"Hola, mi nombre es {nombre} y mi apellido es {apellido}."
	return cadena


# Función que retorna una operación matemática
def sumar_numeros(num01, num02):
	operacion = num01 + num02
	return operacion


#saludo()
# saludo_nombre("Eduardo")

# variable = saludo_string("Eduardo", "Tolentino")
# print(variable)

# suma = sumar_numeros(5.5, 6)
# print(suma)

# saludo()


def operacion(num01, num02):
	resultado = num01 * num02
	print("EL resultado de los números ingresados es: ", resultado)


# sumando1 = input("ingrese el primer número a sumar:   ")
# sumando2 = input("ingrese el segundo número a sumar:   ")
# operacion(int(sumando1), int(sumando2))

#################################################
# Carrito de compras
#################################################
def total(cantidad, precio_unitario):
	operacion = cantidad * precio_unitario
	return operacion


def mostrar_producto(nom_prod, total):
	print(f"El total del prodcto {nom_prod} es S/. {total}")


# nombre_producto = input("Ingrese nombre producto: ")
# cantidad_producto = int(input("Ingrese cantidad del producto: "))
# precio_producto = float(input("Ingrese precio del producto: "))

# var_total = total(cantidad_producto, precio_producto)
# mostrar_producto(nombre_producto, var_total)



#################################################
### CONDICIONALES
#################################################

# if condición:
# 	#logica de programación
# 	#
# 	#
# if condición:
# 	#logica de programación
# 	# 
# 	#
# elif condición:
# 	#logica de programación
# 	# Respuesta
# 	#
# else:
# 	#logica de programación
# 	#
# 	#
# Otra sintaxys de operación

# Operador lógico
# < menor
# > mayor
# == igual
# <= menor o igual
# >= mayor o igual
# and -> un valor verdad dentro de un parametro
# or -> un valor verdad en uno o más parametros
# != diferente


#01 Escribir un programa que pregunte al usuario su edad y muestre por pantalla si es mayor de edad o no.

#usuario ingresa 15 -> es menor de edad
#usuario ingresa 18 -> es mayor de edad

def edad_persona(nombre, edad):
	if edad >= 18:
		print(f"{nombre}, usted es mayor de edad.")
	elif 11 <= edad and edad <= 17:
		print(f"{nombre}, usted es adolescente.")
	else:
		print(f"{nombre}, usted es menor de edad.")


# nombre = input("Ingrese tu Nombre: ")
# edad = int(input("Ingrese tu Edad: "))
# edad_persona(nombre, edad)

#02 Escribir un programa que almacene la cadena de caracteres 
# contraseña en una variable, pregunte al usuario por la contraseña e 
# imprima por pantalla si la contraseña introducida por el usuario 
# coincide con la guardada en la variable sin tener en cuenta 
# mayúsculas y minúsculas.

# contra = "claveusuario"
# usuario_contra = input("Escriba la contraseña: ")

# if contra == usuario_contra.lower():
# 	print("La contraseña es correcta")
# else:
# 	print("La contraseña es incorrecta")

def inicio_sesion(pass_usuario, pass_db):
	if pass_db == pass_usuario:
		print("La contraseña es correcta")
	elif pass_db != pass_usuario: # <> otros lenguajes de programacion
		print("La contraseña es incorrecta")


# pass_usuario = input("Escriba la contraseña: ")
# db_contra = "holacomoestas"
# inicio_sesion(pass_usuario, db_contra)

#03 Escribir un programa que pida al usuario dos números y muestre por pantalla su división. Si el divisor es cero el programa debe mostrar un error.

#04 Escribir un programa que pida al usuario un número entero y muestre por pantalla si es par o impar.

#05 Para tributar un determinado impuesto se debe ser mayor de 16 años y tener unos ingresos iguales o superiores a S/. 1000 mensuales. Escribir un programa que pregunte al usuario su edad y sus ingresos mensuales y muestre por pantalla si el usuario tiene que tributar o no.

#06 Los alumnos de un curso se han dividido en dos grupos A y B de acuerdo al sexo y el nombre. El grupo A esta formado por las mujeres con un nombre anterior a la M y los hombres con un nombre posterior a la N y el grupo B por el resto. Escribir un programa que pregunte al usuario su nombre y sexo, y muestre por pantalla el grupo que le corresponde.

#07 Escribir un programa para una empresa que tiene salas de juegos para 
# todas las edades y quiere calcular de forma automática el precio que debe 
# cobrar a sus clientes por entrar. El programa debe preguntar al usuario la 
# edad del cliente y mostrar el precio de la entrada. Si el cliente es menor 
# de 14 años puede entrar gratis, si tiene entre 14 y 18 años debe pagar S/. 5 y 
# si es mayor de 18 años, S/. 10.

def validar_edad_entrada(edad):
	if edad < 14:
		# Ejecute lo siguiente
		precio = 0
	else:
		if edad <= 18 and edad >= 14:
			precio = 5
		elif edad > 18:
			precio = 10
	return f"El precio de ingreso es S/. {precio}"


edad_cliente = int(input("Ingrese su edad: "))
print(validar_edad_entrada(edad_cliente))


#08 La pizzería Bella Napoli ofrece pizzas vegetarianas y no vegetarianas a sus clientes. Los ingredientes para cada tipo de pizza aparecen a continuación.
	# Ingredientes vegetarianos: Pimiento y tofu.
	# Ingredientes no vegetarianos: Peperoni, Jamón y Salmón.

	# Escribir un programa que pregunte al usuario si quiere una pizza 
	# vegetariana o no, y en función de su respuesta le muestre un menú con los 
	# ingredientes disponibles para que elija. Solo se puede eligir un ingrediente 
	# además de la mozzarella y el tomate que están en todas la pizzas. Al final se debe 
	# mostrar por pantalla si la pizza elegida es vegetariana o no y todos los 
	# ingredientes que lleva.

#################################################
### BUCLES
#################################################
#01 Escribir un programa que pida al usuario una palabra y la muestre por pantalla 10 veces.
#02 Escribir un programa que pregunte al usuario su edad y muestre por pantalla todos los años que ha cumplido (desde 1 hasta su edad).
#03 Escribir un programa que pida al usuario un número entero positivo y muestre por pantalla todos los números impares desde 1 hasta ese número separados por comas.
#04 Escribir un programa que pida al usuario un número entero positivo y muestre por pantalla la cuenta atrás desde ese número hasta cero separados por comas.
#05 Escribir un programa que pregunte al usuario una cantidad a invertir, el interés anual y el número de años, y muestre por pantalla el capital obtenido en la inversión cada año que dura la inversión.
#06 Escribir un programa que pida al usuario un número entero y muestre por pantalla un triángulo rectángulo como el de más abajo, de altura el número introducido.
# *
# **
# ***
# ****
# *****
#07 Escribir un programa que muestre por pantalla la tabla de multiplicar del 1 al 10.
#08 Escribir un programa que pida al usuario un número entero y muestre por pantalla un triángulo rectángulo como el de más abajo.
# 1
# 3 1
# 5 3 1
# 7 5 3 1
# 9 7 5 3 1
#09 Escribir un programa que almacene la cadena de caracteres contraseña en una variable, pregunte al usuario por la contraseña hasta que introduzca la contraseña correcta.
#10 Escribir un programa que pida al usuario un número entero y muestre por pantalla si es un número primo o no.
#11 Escribir un programa que pida al usuario una palabra y luego muestre por pantalla una a una las letras de la palabra introducida empezando por la última.
#12 Escribir un programa en el que se pregunte al usuario por una frase y una letra, y muestre por pantalla el número de veces que aparece la letra en la frase.
#13 Escribir un programa que muestre el eco de todo lo que el usuario introduzca hasta que el usuario escriba “salir” que terminará.