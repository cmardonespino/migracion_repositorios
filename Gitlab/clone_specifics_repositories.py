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

os.chdir("./repositorios")
for repositorio in repositorios_a_clonar:
	os.system("git clone --mirror git@gitlab.bci.cl:"+repositorio+".git")
