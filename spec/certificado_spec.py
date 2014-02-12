import unittest
from should_dsl import should
from certificado import Certificado

class CertificadoSpec(unittest.TestCase):
    
    def it_Criar_objeto_Certificado(self):

    	certificado = Certificado(002, 'curso', 240)

        certificado.codigo |should| equal_to(002)
        certificado.curso |should| equal_to('curso')
        certificado.qtdHoras |should| equal_to(240)