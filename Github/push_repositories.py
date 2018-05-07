# -- coding: utf-8 --

import os, sys
import requests
from variables import NAME_ORGANIZATION, USER_NAME

# https://developer.atlassian.com/bitbucket/api/2/reference/meta/filtering

carpetas_en_el_directorio = os.listdir("./repositorios")

'''
	GUARDAMOS EL PATH DONDE SE ENCUENTRAN LOS .PY PARA VOLVER
	DE LA CARPETA REPOSITORIOS A CARPETA GITX
'''

path_principal = os.getcwd()

for name in carpetas_en_el_directorio:
	os.chdir("./repositorios/"+name)
	#os.system("git init")
	os.system("git remote add origen git@bitbucket.org:"+USER_NAME+"/"+name.lower()+".git")
	os.system("git push origen")
	os.chdir(path_principal)
