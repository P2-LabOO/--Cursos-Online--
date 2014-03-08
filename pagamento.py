class Pagamento:
	def __init__(self,codigo,boleto,cartaoDebito,cartaoCredito):
		self.codigo = codigo
		self.boleto = boleto
		self.cartaoDebito = cartaoDebito
		self.cartaoCredito = cartaoCredito
		
	def calculoBoleto(self,valor):
		self.boleto = valor-(valor*0.15)
		return self.boleto

	def calculoCartaoDebito(self,valor):
		self.cartaoDebito = valor-(valor*0.05)
		return self.cartaoDebito

	def calculoCartaoCredito(self,valor,diasAtraso,juros):
		self.cartaoCredito = valor + (valor*juros*diasAtraso)


