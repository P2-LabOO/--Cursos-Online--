import unittest
from should_dsl import should
from pagamento import Pagamento

class PagamentoSpec(unittest.TestCase):
    
    def it_Criar_objeto_Pagamento(self):

    	pagamento = Pagamento(002, 1919191919, 18)

        pagamento.codigo |should| equal_to(002)
        pagamento.boleto |should| equal_to(1919191919)
        pagamento.cartaoDebito |should| equal_to(18)