## Rol
Actúa como desarrollador backend con experiencia en FastAPI, Jinja2 y pruebas con
pytest.
## Objetivo
Construir la mini-aplicación web [ generador de conraseñas] con estos requisitos:
[1. GET / muestra un formulario para elegir la longitud y si se incluyen números y símbolos, un botón para generar y un botón para copiar la contraseña.
2. GET /api/contrasena recibe los parámetros longitud, numeros y simbolos, y devuelve {"contrasena": texto, "longitud": número}. Valores por defecto: longitud 12, numeros true y simbolos false.
3. La contraseña siempre incluye letras minúsculas y mayúsculas. Si numeros es true, incluye al menos un número; si es false, no incluye ninguno. Si simbolos es true, incluye al menos un símbolo de este grupo: !@#$%&*?-_; si es false, no incluye ninguno.
4. La longitud debe estar entre 8 y 64; fuera de ese rango responde con el código 422.
5. La contraseña se genera con el módulo secrets de Python, no con random.]
## Contexto
Lee AGENTS.md. El contrato de la API está en tests/test_aceptacion.py: las rutas, los
nombres de los campos y los códigos de estado deben coincidir con esas pruebas.
## Restricciones
- Usa solo las dependencias de requirements.txt.
- Define las rutas en app/main.py y la lógica en app/servicios.py, sin importar
FastAPI en servicios.
- Guarda los datos en memoria, sin base de datos ni archivos.
- No modifiques tests/test_aceptacion.py.
- La página usa HTML, CSS y JavaScript sin librerías externas.
## Formato de salida
Antes de escribir código, muestra el plan con las rutas completas de los archivos que
vas a crear y espera mi aprobación. Al terminar, resume en una línea qué hace cada
archivo.
## Ejemplo
[GET /api/contrasena?longitud=16&numeros=true&simbolos=true devuelve:
{"contrasena": "q7G!mR2-xW9a#Lp4", "longitud": 16}]
## Criterio de éxito
python -m pytest -v pasa todas las pruebas y ruff check . no reporta errores. Si
después de 3 intentos las pruebas no pasan, detente y explica el problema.