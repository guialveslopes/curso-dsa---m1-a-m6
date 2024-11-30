class Pessoa():
    def __init__(self, nome = 'Guilherme', telefone = '87981131929', cidade = 'Ouricuri', email = 'alvesguilherme2323@gmail.com'):
        self.nome = nome
        self.telefone = telefone
        self.cidade = cidade
        self.email = email

    def setPessoa(self, novoNome, novoTelefone, novaCidade, novoEmail):
        #só serve se for o caso de redefinir todos os parametros
        self.nome = novoNome
        self.telefone = novoTelefone
        self.cidade = novaCidade
        self.email = novoEmail

    def getPessoa(self):
        print(self.nome, self.telefone, self.cidade, self.email)
    

pess = Pessoa()
pess.getPessoa()

pess = Pessoa('Jose', '87123456789', 'Araripina', 'jose24@gmail.com')
pess.getPessoa()

pess.setPessoa(novoNome= 'Guilherme', novoTelefone= '87987654321', novaCidade= 'Recife',novoEmail= 'devalvesguilherme@gmail.com')
pess.getPessoa()