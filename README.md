# Migración de repositorios
Proyecto correspondiente al desarrollo de scripts en python para migrar repositorios Github y Gitlab a [Bitbucket Cloud](https://www.google.com/search?q=bitbucket+cloud&ie=utf-8&oe=utf-8&client=firefox-b-ab).
Este se desarrolló en windows 7, por lo que si usted utiliza otro sistema operativo, tendrá que ir descargando las dependencias de acuerdo a su kernel.
## Requerimientos
Para correr los scripts, lo que se necesita en tu computador son:
* python 2.7
* pip 9.0.3
* Tener la SSH KEY del computador registrada en Github y Gitlab
### Dependencias
* [pygithub](https://github.com/PyGithub/PyGithub)
* [python-gitlab](https://github.com/python-gitlab/python-gitlab)
* [mingw](https://mingw-w64.org/doku.php)
* [administrador de paquetes Chocolatey](https://chocolatey.org)
* [make](https://chocolatey.org/packages/make)

Por otro lado, se necesita generar un [access token para Gitlab](https://docs.gitlab.com/ee/user/profile/personal_access_tokens.html) y [access token para Github](https://help.github.com/articles/creating-a-personal-access-token-for-the-command-line/) según archivos de carpetas correspondientes.

## HOW-TO
Como paso inicial, se debe configurar el archivo [variables.py Gitlab](Gitlab/variables.py) o [variables.py Github](Github/variables.py) dependiende del repositorio que se requiera migrar a [Bitbucket Cloud](https://www.google.com/search?q=bitbucket+cloud&ie=utf-8&oe=utf-8&client=firefox-b-ab)

### Variables para Gitlab
Para el archivo [variables.py](Gitlab/variables.py) se le solicitará una cierta cantidad de variables las cuales serán utilizadas en los scripts.

#### URL_GIT_REPO
En esta variable, usted debe ingresar la URL del servidor que se requiera clonar los repositorios
#### PRIVATE_TOKEN_REPO
En esta variable, usted debe [generar una access token](https://www.google.com/search?q=access+token+gitlab&ie=utf-8&oe=utf-8&client=firefox-b-ab) desde su cuenta registrada en la URL que usted ingreso. Una vez generado el token, usted debe ingresarlo en la variable.

## Migración de Gitlab a Bitbucket
## Migración de Github a Bitbucket

### Bibliografía utilizada
* [How do I cd in python](https://stackoverflow.com/questions/431684/how-do-i-cd-in-python)
* [API Github](https://developer.github.com/v3/)