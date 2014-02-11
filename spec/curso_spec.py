import unittest
from should_dsl import should
from curso import Curso

class CursoSpec(unittest.TestCase):
    
    def it_Criar_objeto_Curso(self):

    	curso = Curso(002, 'alguem', 18, 2)

        curso.codigo |should| equal_to(002)
        curso.nome |should| equal_to('alguem')
        curso.cargaHoraria |should| equal_to(18)
        curso.aulas |should| equal_to(2)