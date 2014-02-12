class Aluno:
	def __init__(self, codigo, nome, telefone, endereco, email,pagamento=None,certificado=None):
		self.codigo = codigo
		self.nome = nome
		self.telefone = telefone
		self.endereco = endereco
		self.email = email
		
		self.pagamento = pagamento
		self.certificado = certificado