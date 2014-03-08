class AlunoCurso:

	def __init__(self,codigo,nota,nivel,aluno,curso):
		
		self.codigo = codigo
		self.aluno = aluno
		self.curso = curso
		self.nota = nota
		self.nivel = nivel


	def aprovacao(self,nota,nivel):
		if nota>=6.0:
			self.nivel = nivel+1
			print "Aprovado!"
		else:
			print "Reprovado!"


