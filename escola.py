class Escola:
	def __init__(self, codigo, nome, email, site, curso=None):
		self.codigo = codigo
		self.nome = nome
		self.email = email
		self.site = site
		 
		self.curso = curso