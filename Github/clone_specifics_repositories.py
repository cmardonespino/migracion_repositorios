# -- coding: utf-8 --

import os
import requests
from github import Github
from variables import NAME_ORGANIZATION, PRIVATE_TOKEN_REPO

repositorios_a_clonar = [
	'repoPrueba4',
	'repoPrueba5'
]

url = "{}?access_token={}".format(
	'https://api.github.com/orgs/'+NAME_ORGANIZATION+'/repos', 
	PRIVATE_TOKEN_REPO
)
request_json = requests.get(url).json()

os.chdir("./repositorios")
for repositorio in repositorios_a_clonar:
	#os.system("git clone --mirror git@gitlab.bci.cl:"+repositorio+".git")
	#git@github.com:ogranizacionPrueba123/repoPrueba5.git
	#print("git clone {}".format(repositorio["ssh_url"]))
	os.system("git clone git@github.com:"+NAME_ORGANIZATION+"/"+repositorio+".git")
