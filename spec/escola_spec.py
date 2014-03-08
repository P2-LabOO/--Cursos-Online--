import unittest
from should_dsl import should
from escola import Escola
from curso import Curso


class EscolaSpec(unittest.TestCase):

	def it_creates_a_Escola_object(self):

		escola = Escola('001', 'IFF', 'iff@iff', 'iff.edu.br')
		escola.codigo |should| equal_to('001')
		escola.nome |should| equal_to('IFF')
		escola.email |should| equal_to('iff@iff')
		escola.site |should| equal_to('iff.edu.br')
		escola.cursos |should| equal_to([])

	def it_inserir_cursos(self):
		escola = Escola('001', 'IFF', 'iff@iff', 'iff.edu.br',[])
		curso = Curso(123,'curso',40,2,1,150.00,escola)
		escola.inserir_cursos(curso)
		(curso in escola.cursos) |should| equal_to(True)

	def it_verificar_cursos(self):
		escola = Escola('001', 'IFF', 'iff@iff', 'iff.edu.br',[])
		curso = Curso(123,'curso',40,2,1,150.00,escola)
		escola.inserir_cursos(curso)
		escola.verificar_cursos(curso) |should| equal_to(True)
