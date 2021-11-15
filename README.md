# network-analysis-itu-fall-2021

:hand: Hi, this repository serves as a means to save our work for network-analysis course project.

# Get started

## Virtual env

- use venv to create virtual env for this project as follows: `python3 -m venv [name of venv]`

- activate the venv using: `source [name of env]/bin/activate`. You can decativate it by `deactivate`

- make sure your pip is updated: `pip install --upgrade pip`

- intall all needed packages using `pip install -r <path/to/requirement.txt>`

## Github API

- In our project, we use github api to get additional metadata
- The setup is easy, first, go to [this page](https://github.com/settings/tokens)
- create a new personal token, set the scope to be `public_repo`.

- Save the token and put it into `cscripts/envvars.py` (If the file does not exist, create it) By putting I precisely mean declare a variable `GITHUB_TOKEN` and set it equal to your token

- That is all. You do not need to worry, the token will stay locally since the .gitignore is supposed to ignore this file.
