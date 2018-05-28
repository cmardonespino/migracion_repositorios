# -- coding: utf-8 --

'''

	Para el uso de este script, usted requiere de lo siguiente:
		* Token privado de algun usuario que tenga permisos para clonar repositorios
		* Tener instalado python 2.7 y pip en nuestro computador
		* Tener instalado pip install pygithub. En caso de no tenerlo, escribir lo siguiente:
			** pip install pip install pygithub
'''

# https://github.com/jmoiron/python-github
# https://github.com/PyGithub/PyGithub
#https://github.com/copitux/python-github3

import os
import requests
from github import Github

from variables import NAME_ORGANIZATION, PRIVATE_TOKEN_REPO

url = "{}?access_token={}".format(
	'https://api.github.com/orgs/'+NAME_ORGANIZATION+'/repos', 
	PRIVATE_TOKEN_REPO
)
request_json = requests.get(url).json()

if os.path.isdir("./repositorios") == False:
	os.system('mkdir repositorios')

os.chdir("./repositorios")
for repo in request_json:
	os.system("git clone --mirror https://"+PRIVATE_TOKEN_REPO+"@github.com/{}".format(repo["full_name"])+".git")
