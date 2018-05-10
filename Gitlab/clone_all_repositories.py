# -- coding: utf-8 --

'''

	Para el uso de este script, usted requiere de lo siguiente:
		* Token privado de algun usuario que tenga permisos para clonar repositorios
		* Tener instalado python 2.7 y pip en nuestro computador
		* Tener instalado python-gitlab. En caso de no tenerlo, escribir lo siguiente:
			** pip install python-gitlab
'''
# http://gitlab.bci.cl/api/v3/projects/
# https://github.com/python-gitlab/python-gitlab/tree/0.10

import json
import os, sys
from subprocess import call
from gitlab import Gitlab
from variables import URL_GIT_REPO, PRIVATE_TOKEN_REPO, API_VERSION

gl = Gitlab(URL_GIT_REPO,  private_token=PRIVATE_TOKEN_REPO, api_version=API_VERSION)
gl.auth()

projects = gl.projects.list()								
					
if os.path.isdir("./repositorios") == False:
	os.system('mkdir repositorios')

os.chdir("./repositorios")											
for project in projects:									
	os.system("git clone "+project.ssh_url_to_repo)
