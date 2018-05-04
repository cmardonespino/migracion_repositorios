#!/usr/bin/env bash

NORMAL=$(tput sgr0)
GREEN=$(tput setaf 2; tput bold)
YELLOW=$(tput setaf 3)
RED=$(tput setaf 1)

function red() {
  echo -e "$RED$*$NORMAL"
}

function green() {
  echo -e "$GREEN$*$NORMAL"
}

function yellow() {
  echo -e "$YELLOW$*$NORMAL"
}

case "$1" in
  all_repo_github)
    green "CLONANDO TODOS LOS REPOSITORIOS DE GITHUB"
    python clone_all_repositories.py
    green "PUSHEANDO LOS REPOSITORIOS A BITBUCKET"
    python push_repositories.py
    ;;
  specifics_repo_github)
    green "CLOANDO REPOSITORIOS DEFINIDOS"
    python clone_specifics_repositories.py
    green "PUSHEANDO LOS REPOSITORIOS A BITBUCKET"
    python push_repositories.py
    ;;
  all_repo_gitlab)
    green "CLONANDO TODOS LOS REPOSITORIOS DE GITLAB"
    python clone_all_repositories.py
    green "PUSHEANDO LOS REPOSITORIOS A BITBUCKET"
    python push_repositories.py
    ;;
  specifics_group_gitlab)
    ;;
  specifics_repo_gitlab)
    ;;
esac