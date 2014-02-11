import unittest
from should_dsl import should
from aluno import Aluno

class AlunoSpec(unittest.TestCase):
	def it_creates_a_Aluno(self):
		aluno = Aluno('001', 'Grazih', '2732-9876', 'Rua das Flores', 'grazinha@hotmail.com')
		aluno.codigo |should| equal_to('001')
		aluno.nome |should| equal_to('Grazih')
		aluno.telefone |should| equal_to('2732-9876')
		aluno.endereco |should| equal_to('Rua das Flores')
		aluno.email |should| equal_to('grazinha@hotmail.com')