from fastapi.testclient import TestClient

from app.main import app
from app.servicios import calcular_fuerza

cliente = TestClient(app)


def generar(**parametros):
    return cliente.get("/api/contrasena", params=parametros)


def test_fuerte_con_longitud_16_numeros_y_simbolos():
    datos = generar(longitud=16, numeros="true", simbolos="true").json()
    assert datos["fuerza"] == "fuerte"
    assert len(datos["contrasena"]) == 16


def test_media_sin_simbolos():
    datos = generar(longitud=16, numeros="true", simbolos="false").json()
    assert datos["fuerza"] == "media"


def test_media_con_longitud_entre_12_y_15():
    datos = generar(longitud=14, numeros="true", simbolos="true").json()
    assert datos["fuerza"] == "media"


def test_debil_con_longitud_menor_que_12():
    datos = generar(longitud=10, numeros="true", simbolos="true").json()
    assert datos["fuerza"] == "débil"


def test_debil_sin_numeros_ni_simbolos():
    datos = generar(longitud=20, numeros="false", simbolos="false").json()
    assert datos["fuerza"] == "débil"


def test_valores_por_defecto_son_media():
    datos = generar().json()
    assert datos["fuerza"] == "media"
    assert datos["longitud"] == 12


def test_calcular_fuerza_en_los_limites():
    assert calcular_fuerza(16, True, True) == "fuerte"
    assert calcular_fuerza(15, True, True) == "media"
    assert calcular_fuerza(12, False, True) == "media"
    assert calcular_fuerza(11, True, True) == "débil"
    assert calcular_fuerza(64, False, False) == "débil"
