import random

def generar_lista_de_atletas():
	"""
	Esta función genera aleatoriamente los datos de 20 atletas que participaron de una maratón.
	Devuelve una lista de atletas donde cada atleta es un diccionario con los campos:
		- nombre: el nombre del atleta
		- numero: el número con el que participó en la maratón
		- tiempo_llegada: la cantidad de segundos que tardó en llegar
	"""
	lista_atletas = []
	nombres = ('Daniel', 'Alejandro', 'Pablo', 'Hugo', 'Álvaro', 'Adrián', 'David', 'Sergio', 'Diego')
	apellidos = ('García', 'Rodríguez', 'González', 'Fernández', 'López', 'Martínez', 'Sanchez', 'Pérez')	
	for i in range(1, 21):
		atleta = {
			"nombre": random.choice(nombres)+" "+random.choice(apellidos),
			"numero": i,
			"tiempo_llegada": random.random()*120
		}
		lista_atletas.append(atleta)
	return lista_atletas

listaAtletas = generar_lista_de_atletas()

print(listaAtletas)

def mostrarAtletas(listaAtletas):
	for numAtleta in listaAtletas:
		print(f"{numAtleta['numero']} {numAtleta['nombre']} -: ({numAtleta['tiempo_llegada']} segundos) ")
		
mostrarAtletas(listaAtletas)

def atletaGanador(listaAtletas):
	menorTiempo = 150
	numeroGanador = 0
	for elem in listaAtletas:
		if elem['tiempo_llegada'] < menorTiempo:
			menorTiempo = elem['tiempo_llegada']
			numeroGanador = elem['numero']
	return numeroGanador

print(f"El atleta ganador es el numero: {atletaGanador(listaAtletas)}")

def datosAtleta(listaAtletas, numeroAtleta):
	for  i in listaAtletas:
		if i['numero'] == numeroAtleta:
			return print(f"{i['nombre']} :- Número: {i['numero']} -: Tiempo de llegada:  {i['tiempo_llegada']} segundos")
		
datosAtleta(listaAtletas, 14)
	