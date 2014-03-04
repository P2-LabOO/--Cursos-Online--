import unittest
from should_dsl import should
from certificado import Certificado

class CertificadoSpec(unittest.TestCase):
	
	def it_creates_a_certificado_object(self):
		certificado = Certificado(123,'curso',40,2)
		certificado.codigo |should| equal_to(123)
		certificado.curso |should| equal_to('curso')
		certificado.qtdHoras|should| equal_to(40)