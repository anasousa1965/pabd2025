from empresa.dao.base_dao import BaseDAO
from empresa.config.database import SupabaseConnection

class FuncionarioSimples:
    def __init__(self, id=None, nome=None, cargo=None, salario=None):
        self.id = id
        self.nome = nome
        self.cargo = cargo
        self.salario = salario

    def __repr__(self):
        return f"Funcionario(id={self.id}, nome='{self.nome}', cargo='{self.cargo}', salario={self.salario})"

class FuncionarioDAO(BaseDAO):
    def __init__(self):
        client = SupabaseConnection().client
        super().__init__(client, "funcionario")

    def to_model(self, data: dict):
        return FuncionarioSimples(
            id=data.get("id"),
            nome=data.get("nome"),
            cargo=data.get("cargo"),
            salario=data.get("salario")
        )

    def to_dict(self, model) -> dict:
        result = {}
        if hasattr(model, 'nome') and model.nome:
            result["nome"] = model.nome
        if hasattr(model, 'cargo') and model.cargo:
            result["cargo"] = model.cargo
        if hasattr(model, 'salario') and model.salario:
            result["salario"] = model.salario
        return result

    def inserir(self, funcionario):
        return self.create(funcionario)

    def listar(self):
        return self.read_all()

    def atualizar(self, funcionario):
        if hasattr(funcionario, 'id') and funcionario.id:
            return self.update("id", funcionario.id, funcionario)
        return None

    def remover(self, id):
        return self.delete("id", id)