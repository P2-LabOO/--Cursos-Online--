import unittest
from should_dsl import should
from curso import Curso
from escola import Escola
from aluno import Aluno
from alunoCurso import AlunoCurso

class AlunoCursoSpec(unittest.TestCase):

	def it_creates_a_aluno_curso_object(self):
		aluno = Aluno('001', 'Grazi', '997876543', 'Rua das Flores', 'grazi@grazi')
		escola = Escola('001', 'IFF', 'iff@iff', 'iff.edu.br')
		curso = Curso(123,'curso',40,2,1,150.00,escola)

		alunoCurso = AlunoCurso('001',6.8,1,aluno,curso)

		alunoCurso.codigo |should| equal_to('001')
		alunoCurso.nota |should| equal_to(6.8)
		alunoCurso.nivel |should| equal_to(1)
		alunoCurso.aluno |should| equal_to(aluno)
		alunoCurso.curso |should| equal_to(curso)

	def it_aprovacao(self):
		aluno = Aluno('001', 'Grazi', '997876543', 'Rua das Flores', 'grazi@grazi')
		escola = Escola('001', 'IFF', 'iff@iff', 'iff.edu.br')
		curso = Curso(123,'curso',40,2,1,150.00,escola)
		alunoCurso = AlunoCurso('001',6,1,aluno,curso)
		alunoCurso.aprovacao(alunoCurso.nota,alunoCurso.nivel)
		alunoCurso.nivel |should| equal_to(2)

