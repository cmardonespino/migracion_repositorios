# -- coding: utf-8 --

'''

	Para el uso de este script, usted requiere de lo siguiente:
		* Token privado de algun usuario que tenga permisos para clonar repositorios
		* Tener instalado python 2.7 y pip en nuestro computador
		* Tener instalado pip install pygithub. En caso de no tenerlo, escribir lo siguiente:
			** pip install pip install pygithub
'''

# https://github.com/jmoiron/python-github
# https://github.com/PyGithub/PyGithub
# https://github.com/copitux/python-github3

##########################################
########### I M P O R T A N T E ##########
###########################################################################################################################
#http://www.inanzzz.com/index.php/post/wa1f/solution-for-ssh-connect-to-host-github-com-port-22-connection-timed-out-error#
###########################################################################################################################
import os
import requests
from github import Github

URL_GIT_REPO = 'https://api.github.com/user/repos'
PRIVATE_TOKEN_REPO = 'c894c78b7ed57fe45e1c39152e359327e22a41e0'

url = "{}?access_token={}".format(URL_GIT_REPO, PRIVATE_TOKEN_REPO)
request_json = requests.get(url).json()

for repo in request_json:
	os.system("git clone {}".format(repo["ssh_url"]))
