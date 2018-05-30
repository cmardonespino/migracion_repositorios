# -- coding: utf-8 --

import os
from variables import REPOSITORIOS_A_CLONAR

if os.path.isdir("./repositorios") == False:
	os.system('mkdir repositorios')

os.chdir("./repositorios")
for repositorio in REPOSITORIOS_A_CLONAR:
	os.system("git clone --mirror git@gitlab.bci.cl:"+repositorio+".git")
