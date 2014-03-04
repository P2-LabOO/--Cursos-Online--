import unittest
from should_dsl import should
from escola import Escola


class EscolaSpec(unittest.TestCase):

	def it_creates_a_Escola_object(self):

		escola = Escola('001', 'IFF', 'iff@iff', 'iff.edu.br')
		escola.codigo |should| equal_to('001')
		escola.nome |should| equal_to('IFF')
		escola.email |should| equal_to('iff@iff')
		escola.site |should| equal_to('iff.edu.br')