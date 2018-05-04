# Migración de repositorios
Proyecto correspondiente al desarrollo de scripts escritos en python 2.7 para migrar repositorios Github y Gitlab a [Bitbucket Cloud](https://confluence.atlassian.com/get-started-with-bitbucket).
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

# HOW-TO
Como paso inicial, se debe configurar el archivo [variables.py Gitlab](Gitlab/variables.py) o [variables.py Github](Github/variables.py) dependiende del repositorio que se requiera migrar a [Bitbucket Cloud](https://confluence.atlassian.com/get-started-with-bitbucket)

## Configuración variables.py para Gitlab
Para el archivo [variables.py](Gitlab/variables.py), se le solicitará una cierta cantidad de variables las cuales serán utilizadas en los scripts.

### URL_GIT_REPO
En esta variable, usted debe ingresar la URL del servidor que se requiera clonar los repositorios
### PRIVATE_TOKEN_REPO
En esta variable, usted debe [generar una access token](https://docs.gitlab.com/ee/user/profile/personal_access_tokens.html) desde su cuenta registrada en la URL que usted ingreso. Una vez generado el token, usted debe ingresarlo en la variable.
### API_VERSION
Esta variable ya viene por defecto ya que se utiliza la [API V3 de Gitlab](https://docs.gitlab.com/ee/api/).
### GRUPOS_REPOSITORIOS_A_CLONAR
En esta variable, usted debe ingresar los nombres de los grupos de los repositorios los cuales usted desee descargar.
### REPOSITORIOS_A_CLONAR
En esta variable, usted debe ingresar el nombre del grupo/nombre del repositorio al cual se desee clonar.

## Configuración variables.py para Github
Para el archivo [variables.py](Github/variables.py), se le solicitará una cierta cantidad de variables las cuales serán utilizadas en los scripts.
### REPOS_TO_CLONE
En esta variable, usted debe ingresar el nombre del repositorio el cual se desee clonar.
### NAME_ORGANIZATION
En esta variable, usted debe ingresar el nombre de la organización donde se encuentren los repositorios a clonar
### PRIVATE_TOKEN_REPO
En esta variable, usted debe [generar una access token](https://help.github.com/articles/creating-a-personal-access-token-for-the-command-line/) desde su cuenta registrada en la URL que usted ingreso. Una vez generado el token, usted debe ingresarlo en la variable.
### USER_NAME
En esta variable, usted debe ingresar el nombre de usuario del repositorio desde el cual se clonaran los repositorios.

## Migración de Gitlab a Bitbucket
## Migración de Github a Bitbucket

### Bibliografía utilizada
* [How do I cd in python](https://stackoverflow.com/questions/431684/how-do-i-cd-in-python)
* [API Github](https://developer.github.com/v3/)