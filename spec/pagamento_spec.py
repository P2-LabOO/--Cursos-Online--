import unittest
from should_dsl import should
from pagamento import Pagamento

class PagamentoSpec(unittest.TestCase):
    
    def it_creates_a_pagamento_object(self):
        pagamento = Pagamento(123,100,100,100)
        pagamento.codigo |should| equal_to(123)
        pagamento.boleto |should| equal_to(100)
        pagamento.cartaoDebito |should| equal_to(100)
        pagamento.cartaoCredito |should| equal_to(100)

    def it_calculo_calculo_desconto_boleto(self):
        pagamento = Pagamento(123,100,100,100)
        pagamento.calculoBoleto(100)
        pagamento.boleto |should| equal_to(85)

    def it_calculo_cartao_debito(self):
        pagamento = Pagamento(123,100,100,100)
        pagamento.calculoCartaoDebito(100)
        pagamento.cartaoDebito |should| equal_to(95)

    def it_calculo_cartao_credito(self):
        pagamento = Pagamento(123,100,100,100)
        pagamento.calculoCartaoCredito(100,3,0.07)
        pagamento.cartaoCredito |should| equal_to(121)
