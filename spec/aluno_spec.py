import unittest
from should_dsl import should
from aluno import Aluno


class alunoSpec(unittest.TestCase):

	def it_creates_a_Aluno_object(self):

		aluno = Aluno('001', 'Grazi', '997876543', 'Rua das Flores', 'grazi@grazi')
		aluno.codigo |should| equal_to('001')
		aluno.nome |should| equal_to('Grazi')
		aluno.telefone |should| equal_to('997876543')
		aluno.endereco |should| equal_to('Rua das Flores')
		aluno.email |should| equal_to('grazi@grazi')