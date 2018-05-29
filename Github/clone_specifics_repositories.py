# -- coding: utf-8 --

import os
from variables import NAME_ORGANIZATION_GITHUB, REPOS_TO_CLONE

if os.path.isdir("./repositorios") == False:
	os.system('mkdir repositorios')

print("nombre organizacion: "+NAME_ORGANIZATION_GITHUB)
os.chdir("./repositorios")
for repositorio in REPOS_TO_CLONE:
	os.system("git clone --mirror git@github.com:"+NAME_ORGANIZATION_GITHUB+"/"+repositorio)
