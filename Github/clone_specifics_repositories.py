# -- coding: utf-8 --

import os
import requests
from github import Github

repositorios_a_clonar = [
	'repoPrueba4',
	'repoPrueba5'
]

NAME_ORGANIZATION = 'ogranizacionPrueba123'
PRIVATE_TOKEN_REPO = 'a904517e3d38b85d6ae659c3410f9286738a8f69'

url = "{}?access_token={}".format(
	'https://api.github.com/orgs/'+NAME_ORGANIZATION+'/repos', 
	PRIVATE_TOKEN_REPO
)
request_json = requests.get(url).json()

for repositorio in repositorios_a_clonar:
	#os.system("git clone --mirror git@gitlab.bci.cl:"+repositorio+".git")
	#git@github.com:ogranizacionPrueba123/repoPrueba5.git
	#print("git clone {}".format(repositorio["ssh_url"]))
	os.system("git clone git@github.com:"+NAME_ORGANIZATION+"/"+repositorio+".git")
