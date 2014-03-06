import unittest
from should_dsl import should
from curso import Curso
from escola import Escola
from aluno import Aluno
from alunoCurso import AlunoCurso

class CursoSpec(unittest.TestCase):
	
	def it_creates_a_curso_object(self):
		escola = Escola('001', 'IFF', 'iff@iff', 'iff.edu.br',[])
		curso = Curso(123,'curso',40,2,escola,[])
		curso.codigo |should| equal_to(123)
		curso.nome |should| equal_to('curso')
		curso.cargaHoraria |should| equal_to(40)
		curso.aulas |should| equal_to(2)
		curso.escola |should| equal_to(escola)

		curso.alunoCursos |should| equal_to([])

	def it_inserir_aluno_curso(self):
		aluno = Aluno('001', 'Grazi', '997876543', 'Rua das Flores', 'grazi@grazi')
		escola = Escola('001', 'IFF', 'iff@iff', 'iff.edu.br')
		curso = Curso(123,'curso',40,2,escola)

		alunoCurso = AlunoCurso('001',aluno,curso)
		curso.inserirAlunoCursos(alunoCurso)
		(alunoCurso in curso.alunoCursos) |should| equal_to(True)

	def it_verificar_aluno_curso(self):
		aluno = Aluno('001', 'Grazi', '997876543', 'Rua das Flores', 'grazi@grazi')
		escola = Escola('001', 'IFF', 'iff@iff', 'iff.edu.br')
		curso = Curso(123,'curso',40,2,escola)

		alunoCurso = AlunoCurso('001',aluno,curso)
		curso.inserirAlunoCursos(alunoCurso)
		curso.verificaAlunoCursos(alunoCurso) |should| equal_to(True) 