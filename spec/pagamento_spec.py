import unittest
from should_dsl import should
from pagamento import Pagamento

class PagamentoSpec(unittest.TestCase):
	
	def it_creates_a_pagamento_object(self):
		pagamento = Pagamento(123,987654321,123456789,123987123)
		pagamento.codigo |should| equal_to(123)
		pagamento.boleto |should| equal_to(987654321)
		pagamento.cartaoDebito |should| equal_to(123456789)
		pagamento.cartaoCredito |should| equal_to(123987123)