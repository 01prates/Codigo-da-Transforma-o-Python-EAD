from faker import Faker

# Inicializa o gerador de dados em português do Brasil
fake = Faker('pt_BR')

print("=== GERADOR DE DADOS FALSOS PARA TESTES ===")
print(f"Nome     : {fake.name()}")
print(f"CPF      : {fake.cpf()}")
print(f"E-mail   : {fake.email()}")
print(f"Endereço : {fake.address()}")
print(f"Empresa  : {fake.company()}")