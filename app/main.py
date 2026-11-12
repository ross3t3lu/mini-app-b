from fastapi import FastAPI, Query, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

from app.servicios import calcular_fuerza, generar_contrasena

app = FastAPI()
templates = Jinja2Templates(directory="app/templates")


@app.get("/", response_class=HTMLResponse)
def pagina_principal(request: Request) -> HTMLResponse:
    return templates.TemplateResponse(
        request=request,
        name="index.html",
        context={},
    )


@app.get("/api/contrasena")
def obtener_contrasena(
    longitud: int = Query(default=12, ge=8, le=64),
    numeros: bool = True,
    simbolos: bool = False,
) -> dict[str, str | int]:
    contrasena = generar_contrasena(longitud, numeros, simbolos)
    fuerza = calcular_fuerza(longitud, numeros, simbolos)
    return {"contrasena": contrasena, "longitud": longitud, "fuerza": fuerza}
