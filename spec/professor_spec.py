import unittest
from should_dsl import should
from professor import Professor


class professorSpec(unittest.TestCase):

	def it_creates_a_Professor_object(self):

		professor = Professor('001', 'LG', 'lg@lg', '997865432')
		professor.codigo |should| equal_to('001')
		professor.nome |should| equal_to('LG')
		professor.email |should| equal_to('lg@lg')
		professor.telefone |should| equal_to('997865432')