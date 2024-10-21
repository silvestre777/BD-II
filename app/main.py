from services.usuario_service import UsuarioService
from repositories.usuario_repositories import UsuarioRepository
from config.connection import Session
import os

def main():
    session = Session()
    repository = UsuarioRepository(session)
    service = UsuarioService(repository)

    #Criando um usuário
    service.criar_usuario("Silvestre", "silvestre123@gmail.com", "123")
    #Listando todos os usuarios.

    print("\n Listando todos os usuarios.")
    lista_usuarios = service.listar_todos_usuario()
    for usuario in lista_usuarios:
        print(f"{usuario.id} - {usuario.nome} - {usuario.email} - {usuario.senha}")

os.system("cls || clear")
if __name__ == "__main__":
    main() #Chamada da função main
