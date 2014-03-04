class Escola:
	def __init__(self,codigo,nome,email,site, cursos=[]):
		self.codigo = codigo
		self.nome = nome
		self.email = email
		self.site = site

		self.cursos = cursos

	def inserir_cursos(self,curso):
		if not curso in self.cursos:
			self.cursos.append(curso)


	def verificar_cursos(self,curso):
		return (curso in self.cursos)