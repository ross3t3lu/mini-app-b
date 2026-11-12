## Rol
Actúa como desarrollador backend con experiencia en FastAPI, Jinja2 y pruebas con
pytest, que modifica una aplicación existente sin romper su contrato.
## Objetivo
Agregar al generador de contraseñas la indicación de fuerza de la contraseña:
1. La respuesta de GET /api/contrasena, que recibe los parámetros longitud, numeros y
simbolos, incluye el campo nuevo fuerza además de los actuales:
{"contrasena": texto, "longitud": número, "fuerza": texto}.
2. El valor de fuerza se calcula así:
- "fuerte" si la longitud es 16 o más e incluye números y símbolos.
- "débil" si la longitud es menor que 12 o no incluye números ni símbolos.
- "media" en los demás casos.
3. La página principal (GET /) muestra la fuerza que devuelve la API con un color: rojo
para débil, amarillo para media y verde para fuerte.
4. Crear tests/test_mejora.py con pruebas que comprueben el valor de fuerza en la
respuesta para los tres casos (fuerte, media y débil), y no solo el código de estado.
## Contexto
Lee AGENTS.md. La aplicación ya funciona y cumple el contrato de
tests/test_aceptacion.py; todas sus pruebas pasan y deben seguir pasando. Los archivos
relevantes son:
- app/servicios.py: genera la contraseña con secrets. Aquí va el cálculo de la fuerza.
- app/main.py: define GET / y GET /api/contrasena. Aquí se agrega fuerza a la respuesta.
- app/templates/index.html: la página actual ya tiene un medidor de seguridad calculado
en el navegador; debe reemplazarse por la fuerza que devuelve la API.
## Restricciones
- No modifiques tests/test_aceptacion.py.
- Usa solo las dependencias de requirements.txt.
- La lógica de la fuerza va en app/servicios.py, sin importar FastAPI en ese archivo;
las rutas siguen en app/main.py.
- No cambies los nombres de los campos actuales (contrasena y longitud) ni los valores
por defecto (longitud 12, numeros true y simbolos false).
- Los valores de fuerza son exactamente "débil", "media" y "fuerte", en minúsculas y con tilde.
- Guarda los datos en memoria, sin base de datos ni archivos.
- La página usa HTML, CSS y JavaScript sin librerías externas.
- No hagas commit ni push.
## Formato de salida
Antes de escribir código, muestra el plan con las rutas completas de los archivos que
vas a crear o modificar y espera mi aprobación. Al terminar, resume en una línea qué
cambió en cada archivo.
## Ejemplo
GET /api/contrasena?longitud=16&numeros=true&simbolos=true devuelve:
{"contrasena": "q7G!mR2-xW9a#Lp4", "longitud": 16, "fuerza": "fuerte"}

Otros casos esperados:
- GET /api/contrasena?longitud=16&numeros=true&simbolos=false → "fuerza": "media"
- GET /api/contrasena?longitud=10&numeros=true&simbolos=true → "fuerza": "débil"
- GET /api/contrasena?longitud=20&numeros=false&simbolos=false → "fuerza": "débil"
## Criterio de éxito
python -m pytest -v pasa todas las pruebas, tanto las de tests/test_aceptacion.py
como las de tests/test_mejora.py, y ruff check . no reporta errores. Si después de 3
intentos las pruebas no pasan, detente y explica el problema.
