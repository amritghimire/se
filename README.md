# Software Engineering Project

[![Build Status](https://travis-ci.com/amritghimire/se.svg?token=g2nJ3eUfEWGpEUycZyGP&branch=testing)](https://travis-ci.com/amritghimire/se)
## Recommendation and feedback system

### Dependencies
 * [Python]
 * [VirtualEnv]
 * [Django]
 
 ### Installation Instruction
 
* Install [Python]3 if not installed already
* Clone this repo to your working directory by `git clone https://github.com/amritghimire/se.git`
* This will create a directory *se*. Go to this directory by `cd se`
* Type `git update-index --assume-unchanged conf/database.json` to skip your further changes to database config.
* Install [VirtualEnv] and (`sudo apt install virtualenv`) and _pip3_ if you don't have.
* Install [PostgreSQL] by downloading it and setup a database `rafs` with you as **owner** 
* If you set your postgres user anything except **postgres** and password empty, change the value in conf/database.json 	with following content.
  ```json
   {
	 "user": "<user>",
	 "secret": "<password>"
    }
  ```
* Make a [VirtualEnv] by ` virtualenv --python=python3 venv`
* Activate _virtual environment_ by `source venv/bin/activate` or `venv\Scripts\activate`
* Then, install all dependencies with `pip3 install -r requirements.txt`.
* You are good to go now.

### How to run

* Go to the project directory
* Activate _virtual environment_ by `source venv/bin/activate` or `venv\Scripts\activate`
* Run `python manage.py runserver`



[Python]: <https://www.python.org/downloads/>
[VirtualEnv]: <https://virtualenv.pypa.io/en/stable/installation/>
[Django]: <https://www.djangoproject.com/download/>

