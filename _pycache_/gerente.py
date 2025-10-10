from funcionario.funcionario import Funcionario

class Gerente(Funcionario):

    def __init__(self, nome, cpf, salario, senha, qtd_gerenciaveis):
        self._nome = nome
        self._cpf = cpf
        self._salario = salario
        self._senha = senha
        self._qtd_gerenciaveis = qtd_gerenciaveis

        def get_bonificacao(self):
            return self._salario * 0.2
        
        def_str_(self):
            return f'{super()._str_()}\nGerente(Senha: {self._senha}, Qtd Gerenciaveis: {self._qtd_gerenciaveis})'
    
        @property
        def senha(self):
            return self._senha

        @senha.setter
        def senha(self, senha):
            self._senha = senha
        
        @property
        def qtd_gerenciaveis(self):
            return self._qtd_gerenciaveis
        
        @qtd_gerenciaveis.setter
        def qtd_gerenciaveis(self, qtd_gerenciaveis):
            self._qtd_gerenciaveis = qtd_gerenciaveis
