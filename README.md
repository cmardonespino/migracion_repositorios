# 1. Migración de repositorios
Proyecto correspondiente al desarrollo de scripts escritos en python 2.7 para migrar repositorios [Github](https://github.com/) y [Gitlab](https://gitlab.com) a [Bitbucket Cloud](https://confluence.atlassian.com/get-started-with-bitbucket).
Los scripts fueron desarrollados el Sistema Operativo Windows 7, por lo que si usted utiliza otro sistema operativo, tendrá que descargar las dependencias de acuerdo al administrador de paquetes que usted puede o este utilizando.
# 2. Requerimientos
Como requerimientos necesarios para utilizar este proyecto, usted necesita tener instalado en su computador lo siguiente:
* python 2.7+
* pip 9.0.1+
* pygithub
* python-gitlab	
* make

Usted puede instalar lo mencionado anteriormente con el administrador de paquetes de acuerdo a su sistema operativo. Algunos ejemplos:
* [chocolatey](https://chocolatey.org) para windows
* [homebrew](https://brew.sh/) para MacOS

Usted además debe crear un directorio llamado "repositorios" en las carpetas [Gitlab](/Gitlab) y [Github](/Github).
Crear un ssh key vinculada con su cuenta Bitbucket Cloud.

## 2.1 Configuración variables.y
Como paso inicial, se debe configurar el archivo [variables.py Gitlab](Gitlab/variables.py) o [variables.py Github](Github/variables.py) dependiende del repositorio que se requiera migrar a [Bitbucket Cloud](https://confluence.atlassian.com/get-started-with-bitbucket).
### 2.1.1 Configuración variables.py para Gitlab
Para el archivo [variables.py](Gitlab/variables.py), se le solicitará una cierta cantidad de variables las cuales serán utilizadas en los scripts.

#### 2.1.1.1 URL_GIT_REPO
En esta variable, usted debe ingresar la URL del servidor que se requiera clonar los repositorios
#### 2.1.1.2 PRIVATE_TOKEN_REPO
En esta variable, usted debe [generar una access token](https://docs.gitlab.com/ee/user/profile/personal_access_tokens.html) desde su cuenta registrada en la URL que usted ingreso. Una vez generado el token, usted debe ingresarlo en la variable.
#### 2.1.1.3 API_VERSION
Esta variable ya viene por defecto ya que se utiliza la [API V3 de Gitlab](https://docs.gitlab.com/ee/api/).
#### 2.1.1.4 GRUPOS_REPOSITORIOS_A_CLONAR
En esta variable, usted debe ingresar los nombres de los grupos de los repositorios los cuales usted desee descargar.
#### 2.1.1.5 REPOSITORIOS_A_CLONAR
En esta variable, usted debe ingresar el nombre del grupo/nombre del repositorio al cual se desee clonar.

### 2.1.2 Configuración variables.py para Github
Para el archivo [variables.py](Github/variables.py), se le solicitará una cierta cantidad de variables las cuales serán utilizadas en los scripts.
#### 2.1.2.1 REPOS_TO_CLONE
En esta variable, usted debe ingresar el nombre del repositorio el cual se desee clonar.
#### 2.1.2.2 NAME_ORGANIZATION
En esta variable, usted debe ingresar el nombre de la organización donde se encuentren los repositorios a clonar
#### 2.1.2.3 PRIVATE_TOKEN_REPO
En esta variable, usted debe [generar una access token](https://help.github.com/articles/creating-a-personal-access-token-for-the-command-line/) desde su cuenta registrada en la URL que usted ingreso. Una vez generado el token, usted debe ingresarlo en la variable.

# 3. HOW-TO
## 3.1 Migración de Github a Bitbucket
En caso de que usted necesite migrar los repositorios de Github a Bitbucket, usted debe ejecutar desde la linea de comandos lo siguiente:
### 3.1.1 Migrar todos los repositorios
* `make all_repo_github`
### 3.1.2 Migrar repositorios en específico
* `make specifics_repo_github`
## 3.2 Migración de Gitlab a Bitbucket
En caso de que usted necesite migrar los repositorios de Gitlab a Bitbucket, usted debe ejecutar desde la linea de comandos lo siguiente:
### 3.2.1 Migrar todos los repositorios
* `make all_repo_gitlab`
### 3.2.2 Migrar repositorios de un grupo
* `make specifics_group_gitlab`
### 3.2.3 Migrar repositorios en específico
* `make specifics_repo_gitlab`

### Bibliografía utilizada
* [How do I cd in python](https://stackoverflow.com/questions/431684/how-do-i-cd-in-python)
* [API Github](https://developer.github.com/v3/)