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
			
		nodo = self.__buscar (valor, hermanos[pos].hijos, 0)
		if (nodo != None):
			return nodo
		
		nodo = self.__buscar (valor, hermanos, pos + 1)
		if (nodo != None):
			return nodo
		
		return None
		
	def buscar (self, valor):
		
		if (self.__buscar(valor, self.__raiz.hijos, 0) != None):
			return True
		return False
		
	def insertar(self, valor, val_padre = None, pos_hijo = 0):
		
		if (self.__raiz == None):
			self.__raiz = Nodo(valor)
			return
				
		if (val_padre == self.__raiz.info):
			padre = self.__raiz
		else:
			padre = self.__buscar (val_padre, self.__raiz.hijos, 0)
		
		if (padre != None):
			padre.hijos.insert(pos_hijo,Nodo(valor))
			
	
	def preorden(self, nodos = None, pos = 0):
		
		if (nodos == None):
			nodos = [self.__raiz]
			if (nodos == None):
				return
		
		if (pos >= len(nodos)):
			return 
		
		print nodos[pos].info, 
		self.preorden(nodos[pos].hijos, 0)
		self.preorden(nodos, pos + 1)
		

# PRINCIPAL

a = Arboln()
a.insertar("A")
a.insertar("B","A")
a.insertar("C","A")
a.insertar("D","A",1)
a.insertar("E","C")
a.insertar("F","C")
a.insertar("G","B")

a.preorden()
