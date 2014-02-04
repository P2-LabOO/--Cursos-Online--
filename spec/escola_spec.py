import unittest
from should_dsl import should
from escola import Escola


class EscolaSpec(unittest.TestCase):
	def it_creates_a_Escola(self):
		escola = Escola('001', 'IFF', 'iff.com.br', 'iff.edu.br')
		escola.id |should| equal_to('001')
		escola.nome |should| equal_to('IFF')
		escola.email |should| equal_to('iff.com.br')
		escola.site |should| equal_to('iff.edu.br')