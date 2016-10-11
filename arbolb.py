# Arbol Binario
# Autor: Javier Rivera
# https://repl.it/Dkvj/6

class Nodo:
	def __init__ (self, valor):
		self.info = valor
		self.hizq = None
		self.hder = None

class Arbolb:
	def __init__(self):
		self.__raiz = None
	
	def insertar(self, valor, raiz = None):
	
		if (raiz == None):
			if (self.__raiz == None):
				self.__raiz = Nodo(valor)
				return
			raiz = self.__raiz
				
		if (valor < raiz.info):
			if(raiz.hizq == None):
				raiz.hizq = Nodo(valor)
			else:
				self.insertar (valor, raiz.hizq)
		else:
			if (raiz.hder == None):
				raiz.hder = Nodo(valor)
			else:
				self.insertar (valor, raiz.hder)
				
	# Retorna el hermano de un elemento del arbol, indica cual hermano es
	def hermano (self, valor, raiz = None):
		if (raiz == None):
			if (self.__raiz == None):
				return
			raiz = self.__raiz

		if (valor < raiz.info and raiz.hizq != None):
			if (raiz.hizq.info == valor):
				if (raiz.hder != None):
					return raiz.hder.info, "DER"
				return False, "DER"
			return self.hermano (valor, raiz.hizq)
			
		elif (valor > raiz.info and raiz.hder != None):
			if (raiz.hder.info == valor):
				if (raiz.hizq != None):
					return raiz.hizq.info, "IZQ"
				return False, "IZQ"
			return self.hermano (valor, raiz.hder)

		return None
	
	# Retorna el numero de hojas de un arbol
	def num_hojas (self, raiz = None):
		
		if (raiz == None):
			if (self.__raiz == None):
				return
			raiz = self.__raiz
			
		if (raiz.hizq == None and raiz.hder == None):
			return 1
		
		n_hizq, n_hder = 0,0
		if (raiz.hizq != None):
			n_hizq = self.num_hojas(raiz.hizq)
		
		if (raiz.hder != None):
			n_hder = self.num_hojas(raiz.hder)
			
		return n_hizq + n_hder
	
	# Retorna si los datos de un arbol son consecutivos (paso 1) recorrido inorden
	def esConsecutivo (self, raiz = None):
		if (raiz == None):
			if (self.__raiz == None):
				return
			raiz = self.__raiz

		self.__mayor = self.__menor = raiz.info
		
		if (raiz.hizq != None):
			M = self.__mayor
			cons = self.esConsecutivo (raiz.hizq)
			if (not(cons) and (self.__mayor + 1) != raiz.info):
				return False 
			self.__mayor = M
		
		if (raiz.hder != None):
			m = self.__menor 
			cons = self.esConsecutivo (raiz.hder)
			if (not(cons) and raiz.info != (self.__menor - 1)):
				return False
			self.__menor = m
			
		return True 
	
	# Retorna el tipo del nodo de un elemento
	# Raiz, Rama Derecha, Rama Izquierda, Hoja Derecho, Hoja Izquiedo, 
	def tipo_nodo (self, valor, raiz = None, dirn = None):
		
		if (raiz == None):
			if (self.__raiz == None):
				return
			elif (self.__raiz.info == valor):
				return "RAIZ"
			raiz = self.__raiz			
			
		if (valor == raiz.info):
			if (raiz.hizq == None and raiz.hder == None):
				return "HOJA " + dirn
			return "RAMA " + dirn
				
		if (valor < raiz.info and raiz.hizq != None):
			return self.tipo_nodo (valor, raiz.hizq, "IZQ")
			
		elif (raiz.hder != None):
			return self.tipo_nodo (valor, raiz.hder, "DER")
	
	# Elemento mayor del arbol
	def elem_mayor (self, raiz = None):
		if (raiz == None):
			if (self.__raiz == None):
				return
			raiz = self.__raiz
			
		if (raiz.hder != None): 
			return self.elem_mayor(raiz.hder)
			
		return raiz.info
	
	# TRES FORMAS DISTINTAS DE OBTENER EL NUMERO DE NODOS DE UN ARBOL BINARIO
	
	# FORMA 1: la funcion recursiva num_nodos() retorna el numeros de nodos del arbol izquierdo 
	# y del arbol derecho y los suma al nodo donde se encuentra  
	
	def num_nodos(self, raiz = None):
		if (raiz == None):
			if (self.__raiz == None):
				return 0
			raiz = self.__raiz
		
		num = 0	
		if (raiz.hizq != None):
			num = self.num_nodos(raiz.hizq)
					
		if (raiz.hder != None):
			num = num + self.num_nodos(raiz.hder)
		
		return 1 + num

	# FORMA 2: la funcion recursiva nro_nodos() envia por paranetro el numero de nodos encontrados el recorrido  
	# (iniciado por cero en la raiz) luego lo envia luego por parametro a sus ramas izquierda y derecha 
	# para que retroenen la sumen de sus hijos, finalmente retorna el parametro nro mas el nodo actual
	
	def nro_nodos (self, raiz = None, nro = 0):
		if (raiz == None):
			if (self.__raiz == None):
				return 0
			raiz = self.__raiz
		
		if (raiz.hizq != None):
			nro = self.nro_nodos(raiz.hizq,nro)
					
		if (raiz.hder != None):
			nro = self.nro_nodos(raiz.hder,nro)
		
		return 1 + nro
	
	# FORMA 3: la funcion recursiva n_nodos() crea un atributo al arbol self.__n donde sumará los valores
	# de los nodos a traves del recorrido, al final retorna el valor del atributo	
	
	def n_nodos (self, raiz = None):
		if (raiz == None):
			self.__n = 0
			if (self.__raiz == None):
				return self.__n
			raiz = self.__raiz
			
		self.__n = self.__n + 1
		if (raiz.hizq != None):
			self.n_nodos(raiz.hizq)
					
		if (raiz.hder != None):
			self.n_nodos(raiz.hder)
		
		return self.__n
					
	def preorden (self, raiz = None):
		if (raiz == None):
			if (self.__raiz == None):
				return
			raiz = self.__raiz
		
		print raiz.info,
		if (raiz.hizq != None):
			self.preorden (raiz.hizq)
		if (raiz.hder != None):
			self.preorden (raiz.hder)
			
	def postorden (self, raiz = None):
		if (raiz == None):
			if (self.__raiz == None):
				return
			raiz = self.__raiz

		if (raiz.hizq != None):
			self.postorden (raiz.hizq)
		if (raiz.hder != None):
			self.postorden (raiz.hder)
		print raiz.info,	

	def inorden (self, raiz = None):
		if (raiz == None):
			if (self.__raiz == None):
				return
			raiz = self.__raiz

		if (raiz.hizq != None):
			self.inorden (raiz.hizq)
		print raiz.info,
		if (raiz.hder != None):
			self.inorden (raiz.hder)

