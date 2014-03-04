import unittest
from should_dsl import should
from curso import Curso
from escola import Escola

class CursoSpec(unittest.TestCase):
	
	def it_creates_a_curso_object(self):
		escola = Escola('001', 'IFF', 'iff@iff', 'iff.edu.br',[])
		curso = Curso(123,'curso',40,2,escola)
		curso.codigo |should| equal_to(123)
		curso.nome |should| equal_to('curso')
		curso.cargaHoraria |should| equal_to(40)
		curso.aulas |should| equal_to(2)
		curso.escola |should| equal_to(escola)