# Django-Entrega2


## Segunda Entrega de Django: Playground Intermedio

*Nombre: Villafañe, Roxana Noelia*

### Instalación

Instalación de Django

`$ python3 -m pip install Django`

Para correr el proyecto 

`$ python3 ./manage.py runserver`

En caso de necesitar realizar las migraciones

`$ python3 manage.py migrate`

`$ python3 manage.py makemigrations`


### Vistas

Para acceder al sitio, la url correspondiente 


`http://127.0.0.1:8000/coderapp/`


![inicio](inicio.png)




#### Vista de Cursos

La vista incluye un form de búsqueda incluido. 

`http://127.0.0.1:8000/coderapp/cursos/`

![cursos](cursos.png)



#### Vista de Estudiantes

La vista incluye un form de búsqueda incluido. 

`http://127.0.0.1:8000/coderapp/estudiantes/`


![estudiantes](estudiantes.png)



#### Vista de Profesores

La vista incluye un form de búsqueda incluido. 

`http://127.0.0.1:8000/coderapp/profesores/`


![profesores](profesores.png)



#### Formularios de ingreso de datos

Estos formularios se encuentran en vistas separadas

Para ingresar datos de **Estudiantes**


`http://127.0.0.1:8000/coderapp/agregar_estudiante/`

![agregar_estudiante](ag_est.png)



Para ingresar datos de **Profesores**

`http://127.0.0.1:8000/coderapp/agregar_profesor/`

![agregar_profesor](ag_prof.png)



Para ingresar datos de **Cursos**

`http://127.0.0.1:8000/coderapp/crear_curso/`


![agregar_curso](ag_curso.png)




