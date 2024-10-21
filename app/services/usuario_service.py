from models.usuario import Usuario
from respositories.usuario_repositories import UsuarioRepository


class UsuarioService:
    def __init__(repository: UsuarioRepository) -> None:
        self.repository = repository

    def criar_usuario(self, nome: str, email: str, senha:str):
        try:
            usuario = Usuario(nome = nome, email = email, senha = senha)
            self.repository.salvar_usuario(usuario)
            print("Usuario salvo com sucesso!")
            except TypeError as erro:
                print(f"Erro ao salvar o usuario: {erro}")
            except Exception as erro:
                print(f"Ocorreu um erro inesperado: {erro}")
            
    
    def listar_todos_usuario(self):
        return self.repository.listar_todos_usuarios()