# -- coding: utf-8 --

import os, sys
from variables import NAME_ORGANIZATION_BITBUCKET

# https://developer.atlassian.com/bitbucket/api/2/reference/meta/filtering

carpetas_en_el_directorio = os.listdir("./repositorios")

'''
	GUARDAMOS EL PATH DONDE SE ENCUENTRAN LOS .PY PARA VOLVER
	DE LA CARPETA REPOSITORIOS A CARPETA GITX
'''

path_principal = os.getcwd()
ID_ORIGEN = 0

for name in carpetas_en_el_directorio:
	os.chdir("./repositorios/"+name)
	os.system("git remote add origin-"+str(ID_ORIGEN)+" git@bitbucket.org:"+NAME_ORGANIZATION_BITBUCKET+"/"+name.lower())
	print("git remote add origin-"+str(ID_ORIGEN)+" git@bitbucket.org:"+NAME_ORGANIZATION_BITBUCKET+"/"+name.lower())
	os.system("git push origin-"+str(ID_ORIGEN)+" --mirror")
	os.chdir(path_principal)
	ID_ORIGEN += 1
