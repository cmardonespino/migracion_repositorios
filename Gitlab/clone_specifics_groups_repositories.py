# -- coding: utf-8 --

'''

	Para el uso de este script, usted requiere de lo siguiente:
		* Token privado de algun usuario que tenga permisos para clonar repositorios
		* Tener instalado python 2.7 y pip en nuestro computador
		* Tener instalado python-gitlab. En caso de no tenerlo, escribir lo siguiente:
			** pip install python-gitlab
'''

import json
import os
from subprocess import call
from gitlab import Gitlab
from variables import URL_GIT_REPO, PRIVATE_TOKEN_REPO, API_VERSION

grupos_repositorios_a_clonar = [
	'viajes-inversiones',
	'Integracion',
	'Ux-front-end'
]

gl = Gitlab(URL_GIT_REPO,  private_token=PRIVATE_TOKEN_REPO, api_version=API_VERSION)
gl.auth()

projects = gl.projects.list()

os.chdir("./repositorios")
for project in projects:
	for repositorio in grupos_repositorios_a_clonar:
		if(project.namespace.path==repositorio):
			os.system("git clone --mirror git@gitlab.bci.cl:"+project.namespace.path+"/"+project.path+".git")
