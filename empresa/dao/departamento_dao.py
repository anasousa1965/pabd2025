from empresa.dao.base_dao import BaseDAO
from empresa.config.database import SupabaseConnection
from models.departamento import Departamento

class DepartamentoDAO(BaseDAO):
    def __init__(self):
        client = SupabaseConnection().client
        super().__init__(client, "departamento")

    def to_model(self, data: dict) -> Departamento:
        return Departamento(id=data.get("id"), nome=data.get("nome"))

    def to_dict(self, model: Departamento) -> dict:
        return {"nome": model.nome}

    def inserir(self, departamento: Departamento):
        return self.create(departamento)

    def listar(self):
        return self.read_all()

    def atualizar(self, departamento: Departamento):
        if departamento.id:
            return self.update("id", departamento.id, departamento)
        return None

    def remover(self, id):
        return self.delete("id", id)