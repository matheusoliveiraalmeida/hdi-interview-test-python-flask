## PARA RODAR

python app.py

## REQUISITOS

aniso8601==8.1.0
attrs==20.3.0
click==7.1.2
flask-marshmallow==0.14.0
flask-restplus==0.13.0
flask-sqlalchemy==2.4.4
flask==1.1.2
itsdangerous==1.1.0
jinja2==2.11.2
jsonschema==3.2.0
markupsafe==1.1.1
marshmallow-sqlalchemy==0.24.1
marshmallow==3.9.1
pyrsistent==0.17.3
pytz==2020.4
six==1.15.0
sqlalchemy==1.3.20
werkzeug==0.16.1
zipp==3.4.0

## API Swagger: 
http://localhost:5000/api/doc


## CURL POSTMAN

curl --location --request POST 'http://localhost:5000/api/usuario' \
--header 'Content-Type: application/json' \
--data-raw '{
  "documento": 0,
  "nome": "string",
  "contatos": [
    {
      "email": "string",
      "telefone": 0,
      "flagPrincipal": 0
    }
  ]
}'