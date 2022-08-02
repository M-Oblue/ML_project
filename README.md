# Start_ML_project.
## Pre-Requisites:

1. [Github Account](https://github.com/M-Oblue/ML_project)
2. [HerokuAccount](https://dashboard.heroku.com/apps)
3. [VS Code IDE](https://code.visualstudio.com/Download)
4. [GIT](https://git-scm.com/downloads)

## Project Setup:

conda not recognized --> add conda to path variable.

step 1: to check whether you have conda installed or not.
```
conda --version
```
step 2: to activate base environment.
```
conda activate
```
step 3: creating conda environment
--> --name or -n creates an env in anaconda directory.
--> -p creates an env in your home/project directory and -y is for automatic yes.
```
conda create --name <env_name> python==3.7
```
OR
```
conda create -p <env_name> python==3.7 -y
```
step 4:
--> to activate the environment if env is in anaconda directory.
--> to activate the environment if env is in your home/project directory.
```
conda activate <env_name> 
```
OR
```
conda activate <env_name/> 
```
step 5: installing requirements.txt
--> to install all the requirements.txt in the environment.
```
pip install -r requirements.txt 
```
step 6: adding changes to git.
```
git add .
```
OR
```
git add <file_name>
```
NOTE : to ignore a file or folder from git.
```
git ignore <file_name>
```
OR manually add file/folder to .gitignore file.

NOTE : to check the status of the git.
```
git status
```
NOTE : to commit the changes.
```
git commit -m "message"
```
NOTE : to push the changes to github.
```
git push origin main
```
NOTE : to check all versions/commits of the project.
```
git log
```
OR for compact form of version/commit history.
```
git log --graph --all --decorate --oneline
```
NOTE : to check the latest version of the project.
```
git log -1
```






