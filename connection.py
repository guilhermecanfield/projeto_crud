from sqlalchemy import create_engine

# Conecta ao SQLite em memória
engine = create_engine('sqlite:///banco_ecommerce.db', echo=True)

print("Conexão estabelecida!")