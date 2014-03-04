import unittest
from should_dsl import should
from curso import Curso

class CursoSpec(unittest.TestCase):
	
	def it_creates_a_curso_object(self):
		curso = Curso(123,'curso',40,2)
		curso.codigo |should| equal_to(123)
		curso.nome |should| equal_to('curso')
		curso.cargaHoraria |should| equal_to(40)
		curso.aulas |should| equal_to(2)