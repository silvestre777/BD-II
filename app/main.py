from services.usuario_service import UsuarioService
from respositories.usuario_repository import UsuarioRepository
from config.connection import Session

def main():
    session = Session()
    repository = UsuarioReposity(session)
    service = UsuarioService(repository)

    ser