# Migración de repositorios
Proyecto correspondiente al desarrollo de scripts en python para migrar repositorios Github y Gitlab a Bitbucket Cloud.
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
Como paso inicial, se debe configurar el archivo [variables.py Gitlab](Gitlab/variables.py)

## Migración de Gitlab a Bitbucket
## Migración de Github a Bitbucket

### Bibliografía utilizada
* [How do I cd in python](https://stackoverflow.com/questions/431684/how-do-i-cd-in-python)
* [API Github](https://developer.github.com/v3/)