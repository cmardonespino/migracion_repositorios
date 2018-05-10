# -- coding: utf-8 --

'''

	Para el uso de este script, usted requiere de lo siguiente:
		* Token privado de algun usuario que tenga permisos para clonar repositorios
		* Tener instalado python 2.7 y pip en nuestro computador
		* Tener instalado python-gitlab. En caso de no tenerlo, escribir lo siguiente:
			** pip install python-gitlab

'''

import json
import os
from subprocess import call
from gitlab import Gitlab
from variables import REPOSITORIOS_A_CLONAR

if os.path.isdir("./repositorios") == False:
	os.system('mkdir repositorios')

os.chdir("./repositorios")
for repositorio in REPOSITORIOS_A_CLONAR:
	os.system("git clone --mirror git@gitlab.bci.cl:"+repositorio+".git")
