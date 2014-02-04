import unittest
from should_dsl import should
from escola import Escola
from curso import Curso


class EscolaSpec(unittest.TestCase):
	def it_creates_a_Escola(self):
		curso = Curso(002, 'alguem', 18, 2)
		escola = Escola('001', 'IFF', 'iff.com.br', 'iff.edu.br', curso)
		escola.codigo |should| equal_to('001')
		escola.nome |should| equal_to('IFF')
		escola.email |should| equal_to('iff.com.br')
		escola.site |should| equal_to('iff.edu.br')

		escola.curso |should| equal_to(curso)