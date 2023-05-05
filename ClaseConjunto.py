class Conjunto():
	
	def __init__(self, conjunto):
		self.__conjunto = conjunto
		
		self.__eliminarRepetidos()
		
	def __eliminarRepetidos(self):
		unicos = [ ]
		for elem in self.__conjunto:
			if not elem in unicos:
				unicos.append(elem)
		unicos.sort()
		self.__conjunto.clear()
		self.__conjunto = unicos
		
	def __str__(self):
		return str(self.__conjunto)
				
	def __add__(self, otro):
		union = None
		if type(self) == type(otro):
			union = list(self.__conjunto)
			for elem in otro.__conjunto:
				if not elem in union:
					union.append(elem)
		return union
		
	def __sub__(self, otro):
		diferencia = None
		if type(self) == type(otro):
			diferencia = list(self.__conjunto)
			for eliminar in otro.__conjunto:
				if eliminar in diferencia:
					diferencia.pop(diferencia.index(eliminar))
		return diferencia
		
	def __eq__(self, otro):
		igualdad = None
		if type(self) == type(otro):
			return self.__conjunto == otro.__conjunto