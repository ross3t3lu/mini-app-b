import secrets
import string

SIMBOLOS = "!@#$%&*?-_"


def generar_contrasena(
    longitud: int = 12,
    numeros: bool = True,
    simbolos: bool = False,
) -> str:
    if not 8 <= longitud <= 64:
        raise ValueError("La longitud debe estar entre 8 y 64.")

    letras_minusculas = string.ascii_lowercase
    letras_mayusculas = string.ascii_uppercase
    digitos = string.digits
    grupos_obligatorios = [letras_minusculas, letras_mayusculas]
    caracteres_permitidos = letras_minusculas + letras_mayusculas

    if numeros:
        grupos_obligatorios.append(digitos)
        caracteres_permitidos += digitos
    if simbolos:
        grupos_obligatorios.append(SIMBOLOS)
        caracteres_permitidos += SIMBOLOS

    caracteres = [secrets.choice(grupo) for grupo in grupos_obligatorios]
    caracteres.extend(
        secrets.choice(caracteres_permitidos)
        for _ in range(longitud - len(caracteres))
    )
    secrets.SystemRandom().shuffle(caracteres)
    return "".join(caracteres)


def calcular_fuerza(longitud: int, numeros: bool, simbolos: bool) -> str:
    if longitud >= 16 and numeros and simbolos:
        return "fuerte"
    if longitud < 12 or not (numeros or simbolos):
        return "débil"
    return "media"
