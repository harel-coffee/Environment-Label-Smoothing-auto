
# Quick Installation

WOODS is still under active developpement so it is still only available by cloning the repository on your local machine. 

## Installing requirements

### With Conda
First, have conda installed on your machine (see their [installation page](https://docs.anaconda.com/anaconda/install/) if that is not the case). Then create a conda environment with the following command:
```sh
conda create --name woods python=3.7
```
Then activate the environment with the following command:
```sh
conda activate woods
```

### With venv
You can use the python virtual environment manager [virtualenv](https://virtualenv.pypa.io/en/latest/) to create a virtual environment for the project. IMPORTANT: Make sure you are using python >3.7. 
```sh
virtualenv /path/to/woods/env
```
Then activate the virtual environment with the following command:
```sh
source /path/to/env/woods/bin/activate
```

## Clone locally
Once you've created the virtual environment, clone the repository. 
```sh
git clone https://github.com/jc-audet/WOODS.git
cd WOODS
```
Then install the requirements with the following command:
```sh
pip install -r requirements.txt
```

## Run tests
Run the tests to make sure everything is in order. More tests are coming soon.
```sh
pytest
```