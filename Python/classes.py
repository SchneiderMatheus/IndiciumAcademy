class User:
    def __init__(self,name,age):
        self.name = name
        self.age =age
    
    def exibir_info(self):
        status = "Adulto" if self.age >= 18 else "menor"
        print(f"Usuário: {self.name} | Idade: {self.age} | Status: {status}")

user1 = User("Duarte Junior",27)
user2 = User("Matheus Schneider",29)

print("\n---Sistema de Usuários ---")
user1.exibir_info()
user2.exibir_info()

