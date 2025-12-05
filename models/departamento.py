class Departamento:
    def __init__(self, id=None, nome=None):
        self.id = id
        self.nome = nome

    def __repr__(self):
        return f"Departamento(id={self.id}, nome='{self.nome}')"
