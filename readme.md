###### [PythonDevCourse-Udemy](https://www.udemy.com/course/python-developer-pythondjangoflaskpostgresqlmysqlapi/learn/lecture/25640228#overview)

###Pros y Contras de usar Flask

#### Pros
- Fácil para empezar
- Muy customizable, se le pueden agregar extensiones a la funcionalidad
- Altamente compatible con WSGI (Web Server Gateway Interface)

#### Contras
- Limitado si no agregamos features
- No database setup, tenemos que configurar una si la queremos usar

### ¿Qué vamos a hacer?
App con frases de distintas personas, con PostgreSQL como base de datos. La haré con Últimos Cartuchos y shows similares

#### - Bootstrap4: gratis, open source html/css/js framework para hacer web responsives.

#### - Framework: estructura sobre la que podemos hacer aplicaciones

#### - Responsive websites: sitios diseñados para automáticamente adaptarse a distintos dispositivos

#### - Bootstrap es compatible con todos los navegadores modernos

### Seteo variables de entorno de Flask

####Pasos a seguir

- pip install python-dotenv
- Crear un archivo .flaskenv:
  - FLASK_ENV=development # cada vez que realice un cambio se recargará en la página
  - FLASK_APP=quotes.py # módulo donde se alojará el código Flask

#### Endpoints
Endpoints son los nombres de las view function, una view function es una función que responde a requests de la aplicación

#### Templates
Permiten separar código HTML de código Python. Flask busca los templates dentro de la carpeta templates del project folder.

#### Ejecutar contenedor de Docker con PostgreSQL
`(venv) D:\Lautaro\Python\python-dev-course>docker-compose up -d --remove-orphans`

#### WSGI: protocolo de web servers para enviar request a web apps o frameworks escrito en Python

#### Guinocrn: es un wsgi http server que facilita la comunicación entre la web app y el seb server (`pip install gunicorn`)

#### Deploy de la app

- Creo archivo Procfile
- Creo archivo requirements.txt
- Creo archivo .gitignore
- Crear app en Heroku
- Crear instancia de Postgres en Heroku y apuntar la app a la DATABASE_URI de Heroku
- Crear tabla en Heroku
  - python
    - from quotes import db
    - db.create_all()
    - exit()
- 
