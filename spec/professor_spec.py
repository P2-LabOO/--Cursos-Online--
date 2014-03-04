import unittest
from should_dsl import should
from professor import Professor
from curso import Curso
from escola import Escola


class professorSpec(unittest.TestCase):

	def it_creates_a_Professor_object(self):
		escola = Escola('001', 'IFF', 'iff@iff', 'iff.edu.br')
		curso = Curso(123,'curso',40,2,escola)
		professor = Professor('001', 'LG', 'lg@lg', '997865432',curso)
		professor.codigo |should| equal_to('001')
		professor.nome |should| equal_to('LG')
		professor.email |should| equal_to('lg@lg')
		professor.telefone |should| equal_to('997865432')

		professor.curso |should| equal_to(curso)