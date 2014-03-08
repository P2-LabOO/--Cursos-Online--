import unittest
from should_dsl import should
from aluno import Aluno
from curso import Curso
from alunoCurso import AlunoCurso
from escola import Escola


class alunoSpec(unittest.TestCase):

	def it_creates_a_Aluno_object(self):

		aluno = Aluno('001', 'Grazi', '997876543', 'Rua das Flores', 'grazi@grazi',[])
		aluno.codigo |should| equal_to('001')
		aluno.nome |should| equal_to('Grazi')
		aluno.telefone |should| equal_to('997876543')
		aluno.endereco |should| equal_to('Rua das Flores')
		aluno.email |should| equal_to('grazi@grazi')

		aluno.alunoCursos |should| equal_to([])

	def it_inserir_aluno_curso(self):
		aluno = Aluno('001', 'Grazi', '997876543', 'Rua das Flores', 'grazi@grazi')
		escola = Escola('001', 'IFF', 'iff@iff', 'iff.edu.br')
		curso = Curso(123,'curso',40,2,1,150.00,escola)

		alunoCurso = AlunoCurso('001',6.8,1,aluno,curso)
		aluno.inserirAlunoCursos(alunoCurso)
		(alunoCurso in aluno.alunoCursos) |should| equal_to(True)

	def it_verificar_aluno_curso(self):
		aluno = Aluno('001', 'Grazi', '997876543', 'Rua das Flores', 'grazi@grazi')
		escola = Escola('001', 'IFF', 'iff@iff', 'iff.edu.br')
		curso = Curso(123,'curso',40,2,1,150.00,escola)

		alunoCurso = AlunoCurso('001',6.8,1,aluno,curso)
		aluno.inserirAlunoCursos(alunoCurso)
		aluno.verificaAlunoCursos(alunoCurso) |should| equal_to(True)
		