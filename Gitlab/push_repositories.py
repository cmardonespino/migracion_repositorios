# -- coding: utf-8 --

import os, sys
import requests
from variables import USER_NAME

# https://developer.atlassian.com/bitbucket/api/2/reference/meta/filtering

if os.path.isdir("./repositorios") == False:
	os.system('mkdir repositorios')

carpetas_en_el_directorio = os.listdir("./repositorios")

'''
	GUARDAMOS EL PATH DONDE SE ENCUENTRAN LOS .PY PARA VOLVER
	DE LA CARPETA REPOSITORIOS A CARPETA GITX
'''

path_principal = os.getcwd()
ID_ORIGEN = 0

for name in carpetas_en_el_directorio:
	os.chdir("./repositorios/"+name)
	#os.system("git init")
	os.system("git remote add origin-"+str(ID_ORIGEN)+" git@bitbucket.org:"+USER_NAME+"/"+name.lower())
	print("git remote add origin-"+str(ID_ORIGEN)+" git@bitbucket.org:"+USER_NAME+"/"+name.lower())
	os.system("git push origin-"+str(ID_ORIGEN)+" --mirror")
	os.chdir(path_principal)
	ID_ORIGEN += 1

os.system('rm -rf repositorios/')
