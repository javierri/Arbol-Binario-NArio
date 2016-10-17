# Arbol Binario
# Autor: Javier Rivera (UNEFA)
# https://repl.it/Dkvj/11

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
	
	def __hijoMayor (self, raiz = None):
		if (raiz == None):
			if (self.__raiz == None):
				return
			raiz = self.__raiz
			self.__padre = None
		
		if (raiz.hder != None):
			self.__padre = raiz
			self.__dir = "D"
			return self.__hijoMayor(raiz.hder)
			
		return raiz
		
	def __hijoMenor (self, raiz = None):
		if (raiz == None):
			if (self.__raiz == None):
				return
			raiz = self.__raiz
			self.__padre = None
		
		if (raiz.hizq != None):
			self.__padre = raiz
			self.__dir = "I"
			return self.__hijoMenor(raiz.hizq)
			
		return raiz
		
	def prof (self, raiz = None):
		if (raiz == None):
			if (self.__raiz == None):
				return 0
			raiz = self.__raiz

		pizq = pder = 0
		if (raiz.hizq != None):
			pizq = self.prof (raiz.hizq)
			
		if (raiz.hder != None):
			pder = self.prof (raiz.hder)

		if (pizq > pder):
			return pizq + 1
		return pder + 1
		
	def eliminar (self, valor, raiz = None):
		if (raiz == None):
			if (self.__raiz == None):
				return
			raiz = self.__raiz
			self.__padre = None
			self.__dir = None
			
		if (raiz.info == valor):
			if (raiz.hizq == None or raiz.hder == None):
				# Caso 1: Es una Hoja
				if (raiz.hizq == None and raiz.hder == None):
			
					if (not(self.__padre)): # Es la raiz
						del raiz 
						self.__raiz = None
						return True
					
					nieto = None
					
				# Caso 2: Una rama con una sola Hoja	
				else:
					if (raiz.hizq != None):
						nieto = raiz.hizq
					else:
						nieto = raiz.hder
				
				# Elimina nodo y acomoda hijo (izq o der)
				del raiz		
				if (self.__dir == "I"): 
					self.__padre.hizq = nieto
				elif (self.__dir == "D"):
					self.__padre.hder = nieto 
				else: 
					self.__raiz = nieto
					
				return True
				
			# Caso 3: Una rama completa
			self.__padre = raiz
			if (self.prof(raiz.hizq) > self.prof(raiz.hder)):
				nodoCambio = self.__hijoMayor(raiz.hizq)
			else:
				nodoCambio = self.__hijoMenor(raiz.hder)

			raiz.info = nodoCambio.info
			self.eliminar(nodoCambio.info, nodoCambio) # Elimina nodo cambiado

			return True
					
		# Busca Nodo
		self.__padre = raiz
		if (valor < raiz.info and raiz.hizq != None):
			self.__dir = "I"
			return self.eliminar(valor,raiz.hizq)
		
		if (raiz.hder != None):
			self.__dir = "D"
			return self.eliminar(valor,raiz.hder)
			
		return False
	
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
			if (not(cons) or (self.__mayor + 1) != raiz.info):
				return False 
			self.__mayor = M
		
		if (raiz.hder != None):
			m = self.__menor 
			cons = self.esConsecutivo (raiz.hder)
			if (not(cons) or raiz.info != (self.__menor - 1)):
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
	
	# FORMA 1 (A): la funcion recursiva num_nodos() retorna el numeros de nodos del arbol izquierdo 
	# y del arbol derecho y los suma EN UNA MISMA VARIABLE al nodo donde se encuentra  
	
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

	# FORMA 1 (B): a funcion recursiva num_nodos() retorna el numeros de nodos del arbol izquierdo 
	# y del arbol derecho y los suma al nodo donde se encuentra  
	
	def num_nodos_B (self, raiz = None):
		if (raiz == None):
			if (self.__raiz == None):
				return 0
			raiz = self.__raiz
		
		numI,numD = 0,0
		if (raiz.hizq != None):
			numI = self.num_nodos(raiz.hizq)
					
		if (raiz.hder != None):
			numD + self.num_nodos(raiz.hder)
		
		return 1 + numI + numD


	# FORMA 2: la funcion recursiva nro_nodos() envia por paranetro el numero de nodos encontrados el recorrido  
	# (iniciado por cero en la raiz) luego lo envia por parametro a sus ramas izquierda y derecha 
	# para que los retornen con la suma de sus hijos, finalmente retorna el parametro nro mas el nodo actual
	
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
	
	# Metodos de recorrido de un arbol binario
					
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

	#suma el valor de los nodos izquierdos	 colaborador Antony duque
	def SNizq(self , raiz = None ):	
		if (raiz == None):
			self.__siz = 0	
			if (self.__raiz == None):
				return
			raiz = self.__raiz
	
		if (raiz.hizq!=None):
			self.__siz = self.__siz + raiz.hizq.info			
			self.SNizq(raiz.hizq)
			

		if (raiz.hder!=None):
			self.SNizq(raiz.hder)

		return self.__siz 
