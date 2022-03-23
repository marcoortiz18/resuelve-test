# Resuelve Test

En el siguiente README describo los pasos necesarios para poder ejecutar el codigo de forma correcta.

## Installation

Asumiendo que tenemos python instalado en este caso uso la versión

```bash
Python 3.9.10
```

En caso contrario podemos descargarlo del siguiente enlace: [Python Download 3.9](https://www.python.org/downloads/release/python-3911/) y seguimos los pasos que indica el wizard. Una vez que todo se haya instalado procedemos a revisar si esta de forma correcta ejecutando lo siguiente en consola

```bash
python3 --version
```

Para poder hacer las pruebas al servicio de forma local necesitamos instalar *serverless-offline* este es un plugin que nos permite emular AWS λ and API Gateway en nuestro localhost para asegurarnos de que funciona de forma correcta para posterior crear nuestra API.

Para ello debemos ejecutar lo siguiente en la terminal:

```bash
npm install serverless-offline --save-dev
```

Adicional utilizamos *serverless-python-requirements* el cual nos ayuda a agrupar automaticamente las dependencias del archivo requierements.txt


Una vez instalado y si todo ok procedemos a revisar en el archivo: ***serverless.yml*** en el cual debemos tener lo siguiente en el apartado de plugins:

```yml
plugins:
  - serverless-offline
  - serverless-python-requirements
```

## Usage

Una vez realizado todo lo anterior procedemos a probar serveless de forma local para ello escribimos en la terminal lo siguiente:

```bash
sls offline
```
Esto nos deberia mostrar lo siguiente:

```bash
$ sls offline

Starting Offline at stage dev (us-east-1)

Offline [http for lambda] listening on http://localhost:3002
Function names exposed for local invocation by aws-sdk:
           * calculation: resuelve-dev-calculation
           * multi_calculation: resuelve-dev-multi_calculation
           * save_json: resuelve-dev-save_json

   ┌─────────────────────────────────────────────────────────────────────────────────────┐
   │                                                                                     │
   │   POST | http://localhost:3000/dev/salary_calculation                               │
   │   POST | http://localhost:3000/dev/multi_salary_calculation                         │
   │   POST | http://localhost:3000/dev/save_json_file                                   │
   │                                                                                     │
   └─────────────────────────────────────────────────────────────────────────────────────┘

Server ready: http://localhost:3000 🚀

Enter "rp" to replay the last request
```
 En donde se nos muestran los endpoint que hemos creado para crearlos necesitamos [Postman](https://www.postman.com/).

 A continuación comparto los json de prueba para cada uno de los endpoint mencionados:

* POST - *salary_calculation*: [players.json](https://resuelve-test.s3.amazonaws.com/json_files/players.json)
* POST - *multi_salary_calculation*: [multi_players.json](https://resuelve-test.s3.amazonaws.com/json_files/multi_players.json)
* POST - *save_json_file*: [levels.json](https://resuelve-test.s3.amazonaws.com/json_files/levels.json)

## Bonus

Habilite una API y los json de prueba en caso de tener algun problema para poder desplegar el proyecto en local.

* POST /salary_calculation
  * Endpoint: 
  ```bash 
  https://2eh8nagahc.execute-api.us-east-1.amazonaws.com/dev/salary_calculation
  ```
  * [players.json](https://resuelve-test.s3.amazonaws.com/json_files/players.json)

* POST /multi_salary_calculation
  * Endpoint: 
  ```bash 
  https://2eh8nagahc.execute-api.us-east-1.amazonaws.com/dev/multi_salary_calculation
  ```
  * [multi_players.json](https://resuelve-test.s3.amazonaws.com/json_files/multi_players.json)

* POST /save_json_file
  * Endpoint: 
  ```bash 
  https://2eh8nagahc.execute-api.us-east-1.amazonaws.com/dev/save_json_file
  ```
  * [levels.json](https://resuelve-test.s3.amazonaws.com/json_files/levels.json)

Para el correcto funcionamiento use postman y en la *Authorization* fue de tipo *AWS Signature*, asi mismo adjunto las keys necesarias. (Nota en la revision se las proveere)

 Access Key
 ```bash
 ACCESS KEY
 ``` 

 Secret Key
 ```bash
 SECRETE KEY
 ``` 
## Documentation

Adjunto las URL de la documentación usada para realizar el presente proyecto:

* [Serverless-Offline](https://www.serverless.com/plugins/serverless-offline)
* [Python 3.9](https://docs.python.org/3.9/)
* [Pytest](https://docs.pytest.org/en/7.1.x/)
* [Postman](https://learning.postman.com/docs/getting-started/introduction/)
