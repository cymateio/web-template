### PRE-REQUISITE: Must already installed:
### - Python3 (https://www.python.org/downloads/release/python-3100/)
### - pip3 (https://www.activestate.com/resources/quick-reads/how-to-install-and-use-pip3/)
### - virtualenv (https://packaging.python.org/en/latest/guides/installing-using-pip-and-virtual-environments/)


### CREATE A NEW VIRTUAL ENV
virtualenv venv

### ACTIVATE VIRTUAL ENV
source venv/bin/activate

### INSTALLING DEPENDENCIES
pip3 install -r requirements.txt

### DEACTIVATE VIRTUAL ENV
deactivate

### TO REMOVE CURRENT ENV, run: "rm -r venv"
### Note that virtualenv is hardcoded with project name, if you rename your project name, you have to reinstall virtualenv and all its dependencies
### Read more at: https://medium.com/@jisosceles/don-t-rename-your-virtualenv-projects-1049e47e1261