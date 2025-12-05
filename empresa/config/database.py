from supabase import create_client, Client
import os

class SupabaseConnection:
    _instance = None
    
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            # Variáveis de ambiente ou valores padrão
            url = os.getenv("SUPABASE_URL")
            key = os.getenv("SUPABASE_KEY")
            
            if url and key:
                try:
                    cls._instance.client = create_client(url, key)
                except Exception as e:
                    print(f"Aviso: Não foi possível conectar ao Supabase: {e}")
                    print("Usando cliente mock para testes...")
                    cls._instance.client = MockSupabaseClient()
            else:
                print("Aviso: Credenciais do Supabase não encontradas.")
                print("Usando cliente mock para testes...")
                cls._instance.client = MockSupabaseClient()
        return cls._instance


class MockTable:
    def __init__(self):
        self.data = {}
        self.id_counter = 1
    
    def insert(self, data):
        new_id = self.id_counter
        self.id_counter += 1
        data_with_id = {**data, "id": new_id}
        self.data[new_id] = data_with_id
        return MockResponse([data_with_id])
    
    def select(self, *args):
        return self
    
    def execute(self):
        return MockResponse(list(self.data.values()))
    
    def eq(self, key, value):
        filtered = [v for v in self.data.values() if v.get(key) == value]
        return MockResponse(filtered)
    
    def update(self, data):
        self._update_data = data
        return self
    
    def delete(self):
        return self


class MockResponse:
    def __init__(self, data):
        self.data = data
    
    def eq(self, key, value):
        filtered = [v for v in self.data if v.get(key) == value]
        return MockResponse(filtered)
    
    def execute(self):
        if isinstance(self.data, list) and self._update_data if hasattr(self, '_update_data') else False:
            for item in self.data:
                item.update(self._update_data)
        return self


class MockSupabaseClient:
    def __init__(self):
        self.tables = {}
    
    def table(self, name):
        if name not in self.tables:
            self.tables[name] = MockTable()
        return self.tables[name]