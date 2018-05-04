test-all: all_repo_github specifics_repo_github all_repo_gitlab specifics_group_gitlab specifics_repo_gitlab

all_repo_github:
	./test-env.sh all_repo_github
specifics_repo_github:
	./test-env.sh specifics_repo_github
all_repo_gitlab:
	./test-env.sh all_repo_gitlab
specifics_group_gitlab:
	./test-env.sh specifics_group_gitlab
specifics_repo_gitlab:
	./test-env.sh specifics_repo_gitlab