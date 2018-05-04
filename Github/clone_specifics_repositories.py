import os
import requests
from github import Github

repositorios_a_clonar = [
	'onboarding/ms-datosBasicosCliente-neg',
	'viajes-inversiones/ms-depositosAPlazo-neg',
	'onboarding/ms-creacionClaveCliente-orq',
	'onboarding/ms-direccionesCliente-neg',
	'onboarding/ms-seguridadCliente-neg',
	'onboarding/ig-tdm-clientes',
	'onboarding/ig-ibm-direccionescliente',
	'onboarding/onboarding-assets',
	'Integracion/ig-ibm-clientes',
	'viajes-inversiones/ms-estadoEnrolamientoInversiones-exp',
	'Ux-front-end/webkit'
]

'''
for repositorio in repositorios_a_clonar:
	os.system("git clone --mirror git@gitlab.bci.cl:"+repositorio+".git")
'''

URL_GIT_REPO = 'https://api.github.com/user/repos'
PRIVATE_TOKEN_REPO = 'c894c78b7ed57fe45e1c39152e359327e22a41e0'

url = "{}?access_token={}".format(URL_GIT_REPO, PRIVATE_TOKEN_REPO)
request_json = requests.get(url).json()

for repo in request_json:
	os.system("git clone {}".format(repo["ssh_url"]))

