# django_board
My first expreince of django project
To use this project do as follows:
1- downlowd project or cloan it using this command:
git clone https://github.com/javadadabi/django_board
2- install virtual environment for python using this command:
for unix or mac: python3 -m pip install --user virtualenv
for windows: py -m pip install --user virtualenv
3- create a virtualenv using this command:
for unix or mac:python3 -m venv env
for windows:py -m venv env
4- activate env :
unix/mac: source env/bin/activate
windows: .\env\Scripts\activate
5- install requirements using requirements.txt file:
unix/mac: python3 -m pip install -r requirements.txt
windows:  py -m pip install -r requirements.txt
6- make migrations:
python manage.py makemigrations
7- migrate to database:
python mange.py migrate
8- create super user:
python manage.py createsuperuser
8- run server:
python manage.py runserver


