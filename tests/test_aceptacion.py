from fastapi.testclient import TestClient
from app.main import app

cliente = TestClient(app)
SIMBOLOS = set("!@#$%&*?-_")

def generar(**parametros):
    return cliente.get("/api/contrasena", params=parametros)

def test_pagina_principal():
    respuesta = cliente.get("/")
    assert respuesta.status_code == 200
    assert "text/html" in respuesta.headers["content-type"]

def test_longitud_pedida():
    datos = generar(longitud=20).json()
    assert len(datos["contrasena"]) == 20
    assert datos["longitud"] == 20

def test_con_numeros_y_simbolos():
    contrasena = generar(longitud=16, numeros="true", simbolos="true").json()["contrasena"]
    assert any(caracter.islower() for caracter in contrasena)
    assert any(caracter.isupper() for caracter in contrasena)
    assert any(caracter.isdigit() for caracter in contrasena)
    assert any(caracter in SIMBOLOS for caracter in contrasena)

def test_solo_letras():
    contrasena = generar(longitud=16, numeros="false", simbolos="false").json()["contrasena"]
    assert contrasena.isalpha()

def test_valores_por_defecto():
    contrasena = generar().json()["contrasena"]
    assert len(contrasena) == 12
    assert contrasena.isalnum()
    assert any(caracter.isdigit() for caracter in contrasena)

def test_longitud_fuera_de_rango():
    assert generar(longitud=4).status_code == 422
    assert generar(longitud=100).status_code == 422

def test_contrasenas_distintas():
    primera = generar(longitud=16).json()["contrasena"]
    segunda = generar(longitud=16).json()["contrasena"]
    assert primera != segunda