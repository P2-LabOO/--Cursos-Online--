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
		curso = Curso(123,'curso',40,2,escola)

		alunoCurso = AlunoCurso('001',aluno,curso)

		alunoCurso.codigo |should| equal_to('001')
		alunoCurso.aluno |should| equal_to(aluno)
		alunoCurso.curso |should| equal_to(curso)