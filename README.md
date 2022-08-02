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
```
conda create -p <env_name> python==3.7 -y
```
step 4:
--> to activate the environment if env is in anaconda directory.
--> to activate the environment if env is in your home/project directory.
```
conda activate <env_name> 
```
```
conda activate <env_name/> 
```
step 5: installing requirements.txt
--> to install all the requirements.txt in the environment.
```
pip install -r requirements.txt 
```







