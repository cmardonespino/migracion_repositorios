# -- coding: utf-8 --

import os
from variables import REPOSITORIOS_A_CLONAR

path_principal = os.getcwd()
if os.path.isdir(path_principal+"/repositorios") == False:
	os.system('mkdir repositorios')

os.chdir(path_principal+"/repositorios")
for repositorio in REPOSITORIOS_A_CLONAR:
	os.system("git clone --mirror git@gitlab.bci.cl:"+repositorio+".git")
