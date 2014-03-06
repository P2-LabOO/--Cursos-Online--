class Aluno:
	def __init__(self,codigo,nome,telefone,endereco,email,alunoCursos=[]):
		self.codigo = codigo
		self.nome = nome
		self.telefone = telefone
		self.endereco = endereco
		self.email = email

		self. alunoCursos = alunoCursos

	def inserirAlunoCursos(self,alunoCurso):
		self.alunoCursos.append(alunoCurso)

	def verificaAlunoCursos(self,alunoCurso):
		return alunoCurso in self.alunoCursos