# Arbol N-ario
# Autor: Javier Rivera
#


class Nodo:
	def __init__ (self, valor):
		self.info = valor
		self.hijos = []

class Arboln:
	def __init__(self):
		self.__raiz = None
				
	def __buscar (self, valor, hermanos = None, pos = 0):
		
		if (pos >= len(hermanos)):
			return None
		
		if (hermanos[pos].info == valor):
			return hermanos[pos]
			
		nodo = self.__buscar (valor, hermanos[pos].hijos)
		if (nodo != None):
			return nodo
		
		nodo = self.__buscar (valor, hermanos, pos + 1)
		if (nodo != None):
			return nodo
		
		return None
		
	def buscar (self, valor):
		
		if (self.__raiz == valor):
			return True
		
		if (self.__buscar(valor, self.__raiz.hijos) != None):
			return True
		return False
		
	def insertar (self, valor, val_padre = None, pos_hijo = 0):
		
		if (self.__raiz == None):
			self.__raiz = Nodo(valor)
			return True
				
		if (val_padre == self.__raiz.info):
			padre = self.__raiz
		else:
			padre = self.__buscar (val_padre, self.__raiz.hijos, 0)
		
		if (padre != None):
			padre.hijos.insert (pos_hijo,Nodo(valor))
			return True
		
		return False
	
	# Retorna la informacion del padre con mas hijos 
	def padre_mas_hijos (self, nodos = None, pos = 0):
		
		if (nodos == None):
			if (self.__raiz == None):
				return None
			nodos = [self.__raiz]
			self.__mayorpadre = self.__raiz
		
		if (pos >= len(nodos)):
			return 0
			
		if (len(nodos[pos].hijos) > len(self.__mayorpadre.hijos)):
			self.__mayorpadre = nodos[pos] 
		
		self.padre_mas_hijos(nodos[pos].hijos)
		self.padre_mas_hijos(nodos, pos + 1)
		
		return self.__mayorpadre.info
	
	# Retorna el nro de hijos unicos (sin hermanos) en el arbol 
	# La raiz siempre es hijo unico
	def hijos_unicos (self, nodos = None, pos = 0):
		if (nodos == None):
			if (self.__raiz == None):
				return 0
			nodos = [self.__raiz]
		
		if (pos >= len(nodos)):
			return 0
		
		h_unico = 0
		if (len(nodos) == 1):
			h_unico = 1
			
		h_unicos_hijos = self.hijos_unicos (nodos[pos].hijos)
		h_unicos_Hermanos = self.hijos_unicos (nodos, pos + 1)
	
		return h_unico + h_unicos_hijos + h_unicos_Hermanos
	
	# Retorna True si dos valores indicados son nodos hermanos en el arbol n-ario
	def son_hermanos (self, fulano, sutano, nodos = None, pos = 0):
		if (nodos == None):
			if (self.__raiz == None):
				return False
			nodos = [self.__raiz]
		
		if (pos >= len(nodos)):
			return False
		
		hermano = None
		if (fulano == nodos[pos].info): # Existe Fulano
			hermano = sutano
		elif (sutano == nodos[pos].info): # Existe Mengano
			hermano = fulano
			
		if (hermano != None): # Buscar el hermano si exite fulano o sutano
			for nodo in nodos:
				if (hermano == nodo.info): # Encuentra al hermano
					return True
			
		encontro = self.son_hermanos(fulano,sutano,nodos[pos].hijos)			
		if (encontro):
			return True
		
		return self.son_hermanos(fulano,sutano,nodos, pos + 1)		
	
	# Recorrido en Preorden 
	def preorden (self, nodos = None, pos = 0):
		
		if (nodos == None):
			if (self.__raiz == None):
				return
			nodos = [self.__raiz]
		
		if (pos >= len(nodos)):
			return 
		
		print nodos[pos].info, 
		self.preorden (nodos[pos].hijos)
		self.preorden (nodos, pos + 1)
