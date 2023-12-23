
### Setup
To get this repository, run the following command inside your git enabled terminal
```bash
git clone https://github.com/raya-mansouri/Django-Template-Structure/
```

### Getting ready
Create an enviroment in order to keep the repo dependencies seperated from your local machine.
```bash
python3 -m venv venv
```

Make sure to install the dependencies of the project through the requirements.txt file.
```bash
pip install -r requirements.txt
```

Once you have installed django and other packages, go to the cloned repo directory and run the following command

```bash
cd core
python3 manage.py migrate
```
### options
Project it self has the user creation form but still in order to use the admin you need to create a super user.you can use the createsuperuser option to make a super user.
```bash
python3 manage.py createsuperuser
