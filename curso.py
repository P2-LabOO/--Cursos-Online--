class Curso:
	def __init__(self,codigo,nome,cargaHoraria,aulas,escola,alunoCursos=[]):
		self.codigo = codigo
		self.nome = nome
		self.cargaHoraria = cargaHoraria
		self.aulas = aulas	

		self.escola = escola
		self.alunoCursos = alunoCursos

	def inserirAlunoCursos(self,alunoCurso):
		self.alunoCursos.append(alunoCurso)

	def verificaAlunoCursos(self,alunoCurso):
		return alunoCurso in self.alunoCursos