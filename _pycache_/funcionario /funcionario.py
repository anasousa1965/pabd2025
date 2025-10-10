class Funcionario:
    
    _slot__ = ['_nome', '_cpf', '_salario']
    
    def __init__(self, nome, cpf, salario):
        self._nome = nome
        self._cpf = cpf
        self._salario = salario
    
     @property
    def nome(self):
        return self._nome
    
    @nome.setter
    def nome(self, nome):