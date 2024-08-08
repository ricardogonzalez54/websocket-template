## Para crear el entorno virtual y poder ejecutar main.py:

cd ./websocket-template
py -m venv env
./env/Scripts/activate
(Si la línea anterior no se puede ejecutar en Windows debes hacer: Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass)

pip install -r requirements.txt

## Para Levantar el servidor

uvicorn main:app --port 3054 --reload