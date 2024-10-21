from models.usuario import Usuario
from repositories.usuario_repositories import UsuarioRepository


class UsuarioService:
    def __init__(self, repository: UsuarioRepository) -> None:
        self.repository = repository

    def criar_usuario(self, nome: str, email: str, senha:str):
        try:
            usuario = Usuario(nome = nome, email = email, senha = senha)

            consulta_usuario = self.repository.pesquisar_usuario(usuario.email)
            if consulta_usuario:
                print(f"Usuario ja existe")
                return
        
        
            self.repository.salvar_usuario(usuario)
            print("Usuario salvo com sucesso!")
        except TypeError as erro:
            print(f"Erro ao salvar o usuario: {erro}")
        except Exception as erro:
            print(f"Ocorreu um erro inesperado: {erro}")
            
    def listar_todos_usuarios(self):
        return self.repository.listar_todos_usuarios()