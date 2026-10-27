from unittest.mock import patch
from usuario import obter_nome

def test_obter_nome(usuario_id):
    with patch("usuario.buscar_usuario") as mock_buscar_usuario:
        mock_buscar_usuario.return_value = {
            "id":1,
            "nome":"Gabriel"
        }
        nome = obter_nome(1)

        assert nome == "Gabriel"
        mock_buscar_usuario.assert_called_once_with(1)